from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def append_once(path: Path, marker: str, text: str) -> None:
    current = read_text(path)
    if marker in current:
        return
    if current and not current.endswith("\n"):
        current += "\n"
    write_text(path, current.rstrip() + "\n\n" + text.strip() + "\n")


def prepend_notice_once(path: Path, marker: str, notice: str) -> None:
    current = read_text(path)
    if not current or marker in current:
        return
    write_text(path, notice.strip() + "\n\n" + current.lstrip())


def replace_in_file(path: Path, replacements: dict[str, str]) -> None:
    if not path.exists():
        return
    current = read_text(path)
    updated = current
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != current:
        write_text(path, updated)


def replace_in_markdown_tree(replacements: dict[str, str]) -> None:
    skip = {".git", ".venv", "site", ".mkdocs-src", "__pycache__"}
    for path in ROOT.rglob("*.md"):
        if any(part in skip for part in path.parts):
            continue
        replace_in_file(path, replacements)


def fix_toy_evasion() -> None:
    attack_path = ROOT / "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py"
    evasion_py = r'''
from __future__ import annotations

"""
Intent-preserving evasion demonstration for the toy classifier.

This script is deliberately small and synthetic. It does not show a real-world
phishing bypass. It shows the security property: an input can preserve the same
malicious intent while perturbations move the model decision across the boundary.
"""

import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "messages.json"

ORIGINAL = "urgent password reset verify account credential token"
BENIGN_FILLER = (
    "project status update meeting notes roadmap planning sprint backlog "
    "lunch calendar documentation release safe normal internal update"
)


def _field(item: dict[str, Any], names: list[str]) -> str:
    for name in names:
        value = item.get(name)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise KeyError(f"missing one of {names} in dataset item: {item}")


def load_dataset() -> tuple[list[str], list[str]]:
    data = json.loads(DATASET.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("messages") or data.get("samples") or data.get("data")
    if not isinstance(data, list):
        raise ValueError("messages.json must contain a list or an object with messages/samples/data")

    texts: list[str] = []
    labels: list[str] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        texts.append(_field(item, ["text", "message", "content", "body"]))
        labels.append(_field(item, ["label", "class", "target"]).lower())
    if len(set(labels)) < 2:
        raise ValueError("dataset must contain at least two labels")
    return texts, labels


def positive_label(labels: list[str]) -> str:
    for candidate in ["phish", "phishing", "malicious", "spam", "attack"]:
        if candidate in set(labels):
            return candidate
    # Fall back to any label that is not the common benign class.
    for label in sorted(set(labels)):
        if label not in {"safe", "benign", "ham", "normal"}:
            return label
    return sorted(set(labels))[0]


def train_model() -> tuple[Pipeline, str]:
    texts, labels = load_dataset()
    pos = positive_label(labels)
    model = Pipeline(
        steps=[
            ("vectorizer", CountVectorizer(ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1000, random_state=7)),
        ]
    )
    model.fit(texts, labels)
    return model, pos


def score(model: Pipeline, positive: str, text: str) -> tuple[str, float]:
    pred = str(model.predict([text])[0])
    classes = list(model.named_steps["classifier"].classes_)
    probs = model.predict_proba([text])[0]
    if positive not in classes:
        raise ValueError(f"positive label {positive!r} not found in classes {classes}")
    return pred, float(probs[classes.index(positive)])


def find_intent_preserving_evasion(model: Pipeline, positive: str) -> str:
    """Return a perturbed input that keeps the malicious core text intact."""
    # The malicious sentence remains as a literal substring. Only benign-looking
    # context is added around it. This demonstrates evasion, not a swap to a
    # different benign message.
    candidates = []
    for repeats in range(1, 81):
        filler = " ".join([BENIGN_FILLER] * repeats)
        candidates.append(f"{ORIGINAL} {filler}")
        candidates.append(f"{filler} {ORIGINAL} {filler}")

    original_pred, _ = score(model, positive, ORIGINAL)
    for candidate in candidates:
        pred, probability = score(model, positive, candidate)
        if ORIGINAL in candidate and original_pred == positive and pred != positive and probability < 0.50:
            return candidate

    # If the exact flip is not reachable on a future dataset, return the lowest
    # scoring intent-preserving perturbation so the instructor can discuss why
    # this model resisted the simple attack. The test suite uses the shipped
    # deterministic dataset, where the flip is expected.
    return min(candidates, key=lambda candidate: score(model, positive, candidate)[1])


def run_demo() -> dict[str, Any]:
    model, positive = train_model()
    perturbed = find_intent_preserving_evasion(model, positive)

    original_pred, original_prob = score(model, positive, ORIGINAL)
    perturbed_pred, perturbed_prob = score(model, positive, perturbed)

    return {
        "positive_label": positive,
        "original": ORIGINAL,
        "perturbed": perturbed,
        "intent_preserved": ORIGINAL in perturbed,
        "original_prediction": original_pred,
        "original_positive_probability": round(original_prob, 3),
        "perturbed_prediction": perturbed_pred,
        "perturbed_positive_probability": round(perturbed_prob, 3),
        "decision_flipped": original_pred != perturbed_pred,
        "teaching_point": (
            "The perturbed input preserves the malicious core text but adds enough "
            "benign-looking context to move the classifier decision. This is evasion; "
            "it is not a comparison between unrelated malicious and benign messages."
        ),
    }


def main() -> None:
    result = run_demo()
    print("Intent-preserving evasion demo")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
'''
    write_text(attack_path, evasion_py)

    test_path = ROOT / "labs/toy-ml-attacks/toy-classifier-app/tests/test_toy_classifier.py"
    marker = "test_evasion_preserves_malicious_intent_before_decision_flip"
    test_text = r'''

def test_evasion_preserves_malicious_intent_before_decision_flip():
    from attacks.evasion import ORIGINAL, run_demo

    result = run_demo()
    assert result["intent_preserved"] is True
    assert ORIGINAL in result["perturbed"]
    assert result["original_prediction"] == result["positive_label"]
    assert result["decision_flipped"] is True
    assert result["perturbed_positive_probability"] < result["original_positive_probability"]
'''
    append_once(test_path, marker, test_text)

    append_once(
        ROOT / "labs/toy-ml-attacks/toy-classifier-app/README.md",
        "Round 3 evasion correctness note",
        """
## Round 3 evasion correctness note

The evasion script uses an intent-preserving perturbation. The malicious core text remains inside the perturbed message, and benign-looking context is added until the classifier decision crosses the threshold. This is different from comparing one phishing sentence with an unrelated benign sentence. The lab should teach that evasion changes the model decision while preserving the attacker's intent.
""",
    )
    append_once(
        ROOT / "labs/toy-ml-attacks/classical-ml-attack-lab.md",
        "Round 3 correction: evasion must preserve intent",
        """
## Round 3 correction: evasion must preserve intent

Use `toy-classifier-app/attacks/evasion.py` as the runnable evasion example. The corrected script keeps the malicious core message intact and adds benign-looking context until the model decision flips. Do not describe evasion as comparing a phishing message with an unrelated safe message; that teaches the wrong concept.
""",
    )
    append_once(
        ROOT / "labs/adversarial-ml-labs/evasion-robustness-lab.md",
        "Round 3 correction: observable evasion",
        """
## Round 3 correction: observable evasion

The observable evasion path is `../toy-ml-attacks/toy-classifier-app/attacks/evasion.py`. The malicious intent is preserved by keeping the original phishing core text in the perturbed input. The exercise is to decide whether this classifier can be used as a hard gate, what fallback is required when confidence shifts, and how the control should be validated.
""",
    )


def consolidate_legacy_labs() -> None:
    brokenpilot_primary = """
# BrokenPilot-primary lab path

This folder is no longer the primary guided lab path for the 40-hour course.

Use BrokenPilot as the primary runnable target for LLM, RAG, agent, privacy, and red-team exercises. These files are kept only as optional background prompts or appendix material. They are not graded as standalone labs unless an instructor explicitly assigns them.

Primary paths:

- Module 05: `labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md` and `labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md`
- Module 06: BrokenPilot retrieval authorization and indirect prompt injection path
- Module 07: `labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md` and `labs/brokenpilot/prototype-app/MEMORY_POISONING_LAB.md`
- Module 09: `labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md`
- Module 11 and 12: BrokenPilot attack chain and capstone final report

Graded deliverables should be taken from the BrokenPilot lab guides, rubrics, and capstone report templates, not from this legacy folder.
"""
    write_text(ROOT / "labs/agent-labs/README.md", brokenpilot_primary.replace("# BrokenPilot-primary lab path", "# Agent labs: consolidated into BrokenPilot"))
    write_text(ROOT / "labs/rag-labs/README.md", brokenpilot_primary.replace("# BrokenPilot-primary lab path", "# RAG labs: consolidated into BrokenPilot"))

    dvaia_readme = """
# DVAIA guides: optional appendix

DVAIA is useful supplementary material, but it is no longer the critical path for the 40-hour course.

The primary runnable target for Modules 05, 06, 07, 09, 11, and 12 is BrokenPilot because it is local, deterministic, course-owned, and covered by tests. DVAIA may be used as an optional comparison lab when the pinned external revision is available and the instructor has time to support it.

Use this folder only as an appendix:

- Do not grade DVAIA as the main lab path.
- Do not make course completion depend on DVAIA availability.
- If DVAIA behavior differs from BrokenPilot, teach the difference as tool comparison, not as a course requirement.
- Keep evidence and graded deliverables aligned to the BrokenPilot-primary path.
"""
    write_text(ROOT / "labs/dvaia-guides/README.md", dvaia_readme)

    notice = """
> **Round 3 consolidation note:** This legacy paper lab is no longer the primary 40-hour course path. Use the BrokenPilot runnable lab for observable failure/fix behavior. Keep this file only as optional background or a discussion prompt.
"""
    for folder in [ROOT / "labs/agent-labs", ROOT / "labs/rag-labs", ROOT / "labs/dvaia-guides"]:
        if not folder.exists():
            continue
        for path in folder.rglob("*.md"):
            if path.name == "README.md":
                continue
            prepend_notice_once(path, "Round 3 consolidation note", notice)

    replace_in_markdown_tree(
        {
            "DVAIA and BrokenPilot validation": "BrokenPilot-primary validation, with DVAIA optional",
            "DVAIA + BrokenPilot validation": "BrokenPilot-primary validation, with DVAIA optional",
            "DVAIA and BrokenPilot labs": "BrokenPilot-primary labs, with DVAIA optional",
        }
    )


def archive_superseded_build_docs() -> None:
    src = ROOT / "labs/brokenpilot/prototype"
    if not src.exists():
        return
    archive = src / "archive"
    archive.mkdir(parents=True, exist_ok=True)
    retired = [
        "build-backlog.md",
        "control-toggle-plan.md",
        "vulnerability-implementation-plan.md",
        "fake-data-plan.md",
        "docker-compose-plan.md",
        "api-contract.md",
    ]
    moved = []
    for name in retired:
        old = src / name
        new = archive / name
        if old.exists():
            if new.exists():
                old.unlink()
            else:
                shutil.move(str(old), str(new))
            moved.append(name)
    if moved:
        write_text(
            archive / "README.md",
            """
# Archived BrokenPilot build planning notes

These files were useful while the runnable prototype was being designed. They are no longer the student or instructor entry point now that `labs/brokenpilot/prototype-app/` is the working implementation.

Keep these notes only for project history. Students should use the prototype app guides and capstone materials instead.
""",
        )


def fold_privacy_duplicate() -> None:
    path = ROOT / "labs/privacy-labs/privacy-leakage-cross-tenant-rag-lab.md"
    if path.exists():
        prepend_notice_once(
            path,
            "Round 3 privacy consolidation note",
            """
> **Round 3 privacy consolidation note:** The primary runnable version of this concept is now `brokenpilot-cross-tenant-leakage-lab.md`. Use this older paper lab only as an optional design reflection if it adds discussion value beyond the runnable BrokenPilot exercise.
""",
        )
    append_once(
        ROOT / "labs/privacy-labs/README.md",
        "Round 3 primary privacy lab path",
        """
## Round 3 primary privacy lab path

Use `brokenpilot-cross-tenant-leakage-lab.md` as the primary privacy leakage lab. It demonstrates the failure and the fix against BrokenPilot. Older cross-tenant RAG paper material is optional background only.
""",
    )


def move_final_lab_readiness_review() -> None:
    old = ROOT / "labs/FINAL_LAB_READINESS_REVIEW.md"
    new = ROOT / "instructor/FINAL_LAB_READINESS_REVIEW.md"
    if old.exists():
        new.parent.mkdir(parents=True, exist_ok=True)
        if new.exists():
            old.unlink()
        else:
            shutil.move(str(old), str(new))
        print("moved: labs/FINAL_LAB_READINESS_REVIEW.md -> instructor/FINAL_LAB_READINESS_REVIEW.md")


def ensure_output_handling_student_path() -> None:
    output_lab = ROOT / "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md"
    if not output_lab.exists():
        write_text(
            output_lab,
            """
# BrokenPilot output handling lab

## Goal

Show that model output becomes dangerous when a downstream component treats it as trusted content for a specific sink.

## Vulnerable run

1. Start BrokenPilot.
2. Set `ENABLE_OUTPUT_ENCODING=false`.
3. Send a render request to `POST /render` with a message that retrieves the output sink training document.
4. Observe that the response contains the raw marker `<b>OUTPUT_SINK_TRIGGERED</b>`.

## Controlled run

1. Set `ENABLE_OUTPUT_ENCODING=true`.
2. Repeat the same `POST /render` request.
3. Observe that the marker is escaped for the HTML context.

## Teaching point

The vulnerability is not that the model produced text. The vulnerability is that a downstream component embedded model-derived text into an HTML context without output encoding. The correct control is context-aware encoding or validation at the sink, not stronger prompt wording.

## Graded artifact

Submit a short output-handling finding with evidence, sink context, control, validation method, and residual risk.
""",
        )
    append_once(
        ROOT / "modules/05-llm-application-security/brokenpilot-direct-injection-output-lab.md",
        "Round 3 output-handling student path confirmation",
        """
## Round 3 output-handling student path confirmation

The insecure output-handling portion of this module must be run through `POST /render`.

- Vulnerable mode: `ENABLE_OUTPUT_ENCODING=false`; the rendered response includes the raw benign marker `<b>OUTPUT_SINK_TRIGGERED</b>`.
- Controlled mode: `ENABLE_OUTPUT_ENCODING=true`; the same marker is HTML-escaped for the sink context.
- Graded artifact: explain why the problem is downstream trust of model output, not the model producing text.
""",
    )
    append_once(
        ROOT / "modules/05-llm-application-security/README.md",
        "Round 3 Module 05 output-handling confirmation",
        """
## Round 3 Module 05 output-handling confirmation

Module 05 includes two BrokenPilot paths: direct prompt injection and insecure output handling. The output-handling path uses `POST /render` and the `ENABLE_OUTPUT_ENCODING` control so students can observe raw versus encoded output in a deterministic HTML sink.
""",
    )


def ensure_foundation_anchors() -> None:
    anchors = {
        "01-security-engineering-for-ai": (
            "Security Engineering Foundation Deliverable",
            "threat model",
            """
# Security Engineering Foundation Deliverable

## Graded artifact

Submit a short threat model for a simple AI-assisted workflow.

The artifact must include:

- the asset or decision being protected
- the trust boundary where untrusted model-controlled text enters the system
- at least three abuse cases
- the control that enforces the boundary outside the model
- how the control would be validated
- residual risk after the control is added

The goal is not to list every possible AI failure. The goal is to show that the student can separate model behavior from system enforcement.
""",
        ),
        "02-ml-system-architecture": (
            "ML System Architecture Deliverable",
            "architecture and data-flow map",
            """
# ML System Architecture Deliverable

## Graded artifact

Submit an architecture and data-flow map for an ML-enabled application.

The artifact must include:

- users, services, model calls, tools, retrieval stores, logs, and artifact stores
- trust boundaries for user input, retrieved content, model output, tool calls, and training artifacts
- where authorization, validation, output handling, logging, and approval controls live
- one abuse path showing how data or authority crosses a boundary
- one control placement decision and how it would be validated
- residual risk after the proposed design

The goal is to show that the student can reason about the ML system as a distributed application, not as a standalone model.
""",
        ),
    }
    for module, (title, artifact, body) in anchors.items():
        path = ROOT / "modules" / module / "exercise-deliverable-anchor.md"
        write_text(path, body)
        append_once(
            ROOT / "modules" / module / "README.md",
            f"Round 3 {title}",
            f"""
## Round 3 graded artifact confirmation

This module ends in a graded artifact: a **{artifact}**. Use `exercise-deliverable-anchor.md` as the submission anchor.
""",
        )


def write_round3_docs() -> None:
    write_text(
        ROOT / "ROUND3_CONTENT_QUALITY_FIXES.md",
        """
# Round 3 Content Quality Fixes

This pass closes the small quality gaps found after the final content review.

## Decisions

- BrokenPilot is the primary runnable target for LLM, RAG, agent, privacy, red-team, and capstone labs.
- DVAIA is optional appendix material, not a critical-path lab dependency.
- Legacy paper RAG and agent labs are consolidated into BrokenPilot-primary guidance.
- Toy-classifier evasion must preserve malicious intent while changing the model decision.
- Module 05 output handling must be student-facing through `POST /render` and `ENABLE_OUTPUT_ENCODING`.
- Modules 01 and 02 must end in explicit graded artifacts.

## Not part of this pass

- MkDocs strict navigation
- final CI cleanup
- removal of temporary apply scripts
- broad prose normalization

Those belong to the release-hardening phase.
""",
    )
    append_once(
        ROOT / "CLEANUP_BEFORE_RELEASE.md",
        "Round 3 cleanup reminders",
        """
## Round 3 cleanup reminders

Before release, verify that legacy DVAIA, RAG, and agent paper labs are either clearly optional or removed from student navigation. Keep BrokenPilot as the primary path for those modules. Also verify that archived BrokenPilot prototype planning notes are not presented as current student instructions.
""",
    )
    write_text(
        ROOT / "release-notes/v1.1-dev-round3-content-quality-fixes.md",
        """
# v1.1-dev Round 3 Content Quality Fixes

This update fixes the final content-quality issues found in the Round 3 review:

- corrects the toy-classifier evasion demo so the malicious intent is preserved
- consolidates legacy agent, RAG, and DVAIA paths into BrokenPilot-primary guidance
- confirms the Module 05 output-handling lab path
- confirms Modules 01 and 02 graded deliverables
- archives superseded BrokenPilot planning notes when present
- moves final lab readiness review material out of the student-facing lab root when present
""",
    )


def main() -> None:
    fix_toy_evasion()
    consolidate_legacy_labs()
    archive_superseded_build_docs()
    fold_privacy_duplicate()
    move_final_lab_readiness_review()
    ensure_output_handling_student_path()
    ensure_foundation_anchors()
    write_round3_docs()
    print("\nApplied Round 3 content quality fixes.")


if __name__ == "__main__":
    main()
