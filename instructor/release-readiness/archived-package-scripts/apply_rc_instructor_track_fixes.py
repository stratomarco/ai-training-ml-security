from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

ROOT = Path.cwd()
ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-pre-release-docs"
CONSOLIDATED_ARCHIVE = ARCHIVE / "consolidated-instructor-guides"


def rel_link(from_file: Path, target_rel: str, label: str | None = None) -> str:
    target = ROOT / target_rel
    label = label or target_rel
    if target.exists():
        link = os.path.relpath(target, start=from_file.parent).replace("\\", "/")
        return f"[{label}]({link})"
    return f"`{label}`"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def move_if_exists(src_rel: str, dst_dir: Path | None = None) -> None:
    src = ROOT / src_rel
    if not src.exists():
        return
    dst_dir = dst_dir or ARCHIVE
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if dst.exists():
        # Preserve the newer destination and archive the source with a suffix.
        stem = src.stem
        suffix = src.suffix
        i = 2
        while True:
            candidate = dst_dir / f"{stem}-{i}{suffix}"
            if not candidate.exists():
                dst = candidate
                break
            i += 1
    shutil.move(str(src), str(dst))


def patch_40_hour_plan() -> None:
    path = ROOT / "instructor" / "40-hour-delivery-plan.md"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")

    replacements = {
        "Local laptop, DVAIA, BrokenPilot": "Local laptop, BrokenPilot, toy classifier, and MLOps evidence pack; DVAIA optional",
        "Local laptop, DVAIA, and BrokenPilot": "Local laptop, BrokenPilot, toy classifier, and MLOps evidence pack; DVAIA optional",
        "Deep coverage + DVAIA lab": "Deep coverage + BrokenPilot lab",
        "DVAIA/BrokenPilot lab": "Deep coverage + BrokenPilot lab, DVAIA optional",
        "DVAIA / BrokenPilot lab": "Deep coverage + BrokenPilot lab, DVAIA optional",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Make row-level fixes resilient to small table wording changes.
    text = re.sub(
        r"(\|\s*0?5\s*\|[^\n|]*\|[^\n|]*)(DVAIA[^\n|]*lab)([^\n]*\|)",
        lambda m: m.group(1) + "BrokenPilot lab" + m.group(3),
        text,
        flags=re.I,
    )
    text = re.sub(
        r"(\|\s*0?6\s*\|[^\n|]*\|[^\n|]*)(DVAIA\s*/?\s*BrokenPilot[^\n|]*lab)([^\n]*\|)",
        lambda m: m.group(1) + "BrokenPilot lab, DVAIA optional" + m.group(3),
        text,
        flags=re.I,
    )

    path.write_text(text, encoding="utf-8", newline="\n")


def write_instructor_readme() -> None:
    path = ROOT / "instructor" / "README.md"

    start_items = [
        ("COURSE_STORYLINE.md", "Course storyline", "the argument the course makes from foundations to capstone"),
        ("teaching-the-course-narrative.md", "Teaching the course narrative", "how to explain the through-line live"),
        ("40-hour-delivery-plan.md", "40-hour delivery plan", "the week, hour by hour"),
        ("40-hour-student-experience-runbook.md", "Student experience runbook", "daily rhythm, student flow, and checkpoints"),
        ("../assessments/anchor-based-grading-guide.md", "Anchor-based grading guide", "how to grade consistently"),
        ("../assessments/40-hour-checkpoint-rubric.md", "40-hour checkpoint rubric", "daily evidence quality expectations"),
    ]

    start_lines = []
    for i, (rel, title, why) in enumerate(start_items, start=1):
        start_lines.append(f"{i}. {rel_link(path, rel, title)} - {why}.")

    modules = [
        "01-security-engineering-for-ai",
        "02-ml-system-architecture",
        "03-owasp-ml-top-10",
        "04-biml-architectural-risk-analysis",
        "05-llm-application-security",
        "06-rag-security",
        "07-agent-tool-security",
        "08-secure-mlops-supply-chain",
        "09-privacy-attacks",
        "10-adversarial-ml-robustness",
        "11-ai-red-team-methodology",
        "12-capstone-brokenpilot",
    ]
    module_lines = []
    for mod in modules:
        module_lines.append(f"- {rel_link(path, f'../modules/{mod}/instructor-notes.md', mod)}")

    text = f"""
# Instructor Guide

This folder is the instructor track for the course. It contains delivery guidance, facilitation notes, debrief prompts, grading support, and release-readiness material. Start with the files below instead of browsing the directory alphabetically.

## Start here: read in this order

{chr(10).join(start_lines)}

## Per-module teaching notes

Use the module instructor notes when preparing a specific session. They give teaching intent, timing, framing, key points, likely student mistakes, and the expected handoff to the next module.

{chr(10).join(module_lines)}

Depth-pass support:

- {rel_link(path, 'teaching-modules-01-04-depth-pass.md', 'Teaching Modules 01-04 depth pass')}
- {rel_link(path, 'teaching-modules-08-11-depth-pass.md', 'Teaching Modules 08-11 depth pass')}

## Per-lab facilitation entry points

Use exactly one facilitation guide per major lab family:

- {rel_link(path, 'toy-classifier-guide.md', 'Toy classifier guide')} - Modules 03 and 10. Covers setup, run flow, common failure modes, debrief prompts, and pointers to the model reports.
- {rel_link(path, 'brokenpilot-guide.md', 'BrokenPilot guide')} - Modules 05, 06, 07, 09, 11, and 12. Covers the supported runnable app, attack/fix flow, capstone evidence, and instructor debrief.
- {rel_link(path, 'mlops-evidence-pack-guide.md', 'MLOps evidence pack guide')} - Module 08. Covers the evidence-pack review, facilitation flow, expected findings, and model-answer debrief.

## Delivery and support

- {rel_link(path, 'delivery-formats.md', 'Delivery formats')} - choose live, compressed, self-study, or blended delivery.
- {rel_link(path, 'timing-guide.md', 'Timing guide')} - keep each module inside the expected time box.
- {rel_link(path, 'module-cut-expand-guide.md', 'Module cut/expand guide')} - decide what to cut or expand without breaking the storyline.
- {rel_link(path, 'lab-troubleshooting-and-reset-guide.md', 'Lab troubleshooting and reset guide')} - recover student environments and reset labs.
- {rel_link(path, 'executive-communication-guide.md', 'Executive communication guide')} - help students translate technical findings into leadership language.
- {rel_link(path, 'finding-rewrite-facilitation-guide.md', 'Finding rewrite facilitation guide')} - coach students from raw observations to defensible findings.

## Assessment and calibration

Use the assessment files as the grading source of truth. The instructor track should explain how to use them, not duplicate them.

- {rel_link(path, '../assessments/40-hour-daily-checkpoints.md', '40-hour daily checkpoints')}
- {rel_link(path, '../assessments/40-hour-checkpoint-rubric.md', '40-hour checkpoint rubric')}
- {rel_link(path, '../assessments/lab-deliverable-quality-checklist.md', 'Lab deliverable quality checklist')}
- {rel_link(path, '../assessments/anchor-based-grading-guide.md', 'Anchor-based grading guide')}
- {rel_link(path, '../assessments/brokenpilot-current-final-report-rubric.md', 'BrokenPilot final report rubric')}

## Release-readiness archive

Build-time review notes, release cleanup reports, and pre-release readiness checks live under {rel_link(path, 'release-readiness/', 'release-readiness/')}. They are useful history, but they are not the teaching path for a new instructor.
"""
    write(path, text)


def write_toy_classifier_guide() -> None:
    path = ROOT / "instructor" / "toy-classifier-guide.md"
    text = f"""
# Toy Classifier Instructor Guide

This is the single instructor entry point for the toy-classifier labs used in Modules 03 and 10. Use the student-facing lab material for instructions, and use this guide for facilitation, debrief, and grading emphasis.

## Where this lab fits

- Module 03 uses the lab to make OWASP ML risks concrete with a small, inspectable classifier.
- Module 10 uses the same environment to discuss evasion, poisoning, model extraction, output-integrity failures, and robustness tradeoffs.
- The purpose is not to teach machine-learning performance tuning. The purpose is to show that security properties can fail around a model even when the model is small and deterministic.

## Instructor preparation

Before class, run the lab once from the app directory:

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
pytest
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
```

Expected outcome: tests pass, the model trains locally, and each attack script prints a deterministic observation students can include in their lab report.

Student-facing entry points:

- {rel_link(path, '../labs/toy-ml-attacks/classical-ml-attack-lab.md', 'Classical ML attack lab')}
- {rel_link(path, '../labs/adversarial-ml-labs/evasion-robustness-lab.md', 'Evasion and robustness lab')}
- {rel_link(path, '../labs/toy-ml-attacks/toy-classifier-app/README.md', 'Toy classifier app README')}
- {rel_link(path, '../labs/toy-ml-attacks/toy-classifier-app/DEBRIEF_GUIDE.md', 'Student debrief guide')}

## How to run the session

1. Start by showing the baseline classifier and the data shape. Keep this short; students only need enough ML detail to understand what changes.
2. Have students run evasion first. The important observation is an intent-preserving input change that flips the classifier decision.
3. Move to poisoning. Ask students to separate model-quality degradation from security impact.
4. Run extraction. Emphasize that repeated queries can reveal boundary behavior even without direct model access.
5. Run output-integrity tampering. This is where students should notice that the system decision can be compromised without changing the trained model.
6. End with defense-in-depth: data validation, evaluation, provenance, monitoring, approval gates, output contracts, and rollback.

## Debrief prompts

Use these prompts after students have evidence from the scripts:

- Which attack changed the input, which changed the training process, which inferred behavior, and which changed the decision layer?
- Which failures would a normal accuracy metric miss?
- What would you log to make the failure explainable later?
- Which mitigations belong in the model pipeline, and which belong in the surrounding product system?
- What is the smallest control that would have prevented the demonstrated failure? What would still remain exposed?

## Common instructor corrections

- Do not let students describe the evasion as just a funny word swap. It is only security-relevant because malicious intent remains while the decision changes.
- Do not let poisoning become a pure data-science discussion. The security question is who can influence training data, labels, evaluation, and promotion.
- Do not let extraction be framed as only model theft. It is also reconnaissance against the decision boundary.
- Do not let output-integrity failures be dismissed as outside ML security. A model-containing system can be compromised after inference.

## Evidence students should produce

A strong submission includes:

- baseline behavior
- attack observation
- why the observed behavior matters
- control recommendation
- residual risk
- one naive mitigation that would not be enough

Reference material:

- {rel_link(path, '../labs/toy-ml-attacks/toy-classifier-app/worked-examples/strong-toy-classifier-lab-report.md', 'Strong toy-classifier lab report')}
- {rel_link(path, '../labs/toy-ml-attacks/toy-classifier-app/worked-examples/weak-toy-classifier-lab-report.md', 'Weak toy-classifier lab report')}
- {rel_link(path, '../assessments/lab-deliverable-quality-checklist.md', 'Lab deliverable quality checklist')}
"""
    write(path, text)


def write_brokenpilot_guide() -> None:
    path = ROOT / "instructor" / "brokenpilot-guide.md"
    text = f"""
# BrokenPilot Instructor Guide

This is the single instructor entry point for BrokenPilot. BrokenPilot is the supported runnable environment for Modules 05, 06, 07, 09, 11, and 12.

## What BrokenPilot teaches

BrokenPilot is an internal AI-agent scenario with retrieval, tool use, memory, controls, and audit evidence. It is designed to make students reason about security engineering decisions around an ML-enabled system, not to reward prompt-hacking tricks.

The lab family covers:

- direct prompt injection
- insecure output handling
- RAG authorization and cross-tenant leakage
- tool authorization and confused-deputy behavior
- approval gates
- memory poisoning and memory isolation
- audit evidence and final reporting

## Instructor preparation

Run the supported app and tests from the current target directory:

```powershell
cd labs/brokenpilot/prototype-app
pytest
uvicorn app.main:app --reload --port 8010
```

Supported entry points:

- {rel_link(path, '../labs/brokenpilot/prototype-app/README.md', 'Prototype app README')}
- {rel_link(path, '../labs/brokenpilot/prototype-app/LAB_GUIDE.md', 'Main lab guide')}
- {rel_link(path, '../labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md', 'Direct prompt injection lab')}
- {rel_link(path, '../labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md', 'Output handling lab')}
- {rel_link(path, '../labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md', 'Tool calling lab')}
- {rel_link(path, '../labs/brokenpilot/prototype-app/MEMORY_POISONING_LAB.md', 'Memory poisoning lab')}
- {rel_link(path, '../labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md', 'Cross-tenant privacy leakage lab')}
- {rel_link(path, '../labs/brokenpilot/CAPSTONE_CHECKPOINTS.md', 'Capstone checkpoints')}
- {rel_link(path, '../labs/brokenpilot/CAPSTONE_FINAL_REPORT_CURRENT_PATH.md', 'Capstone final report path')}

## How to run the lab family

Use BrokenPilot as a progressive system, not as isolated tricks.

1. Start with the system model: users, tenants, retrieval, memory, tool execution, controls, and audit logs.
2. Demonstrate one failure with controls off.
3. Turn on the relevant control and require students to explain what changed.
4. Ask what the control does not solve.
5. Capture evidence as students go: request, response, control state, observed impact, and residual risk.
6. Use the final capstone to force prioritization across multiple failures.

## Module mapping

- Module 05: direct prompt injection and output handling.
- Module 06: RAG authorization and indirect/contextual injection risks.
- Module 07: tool authorization, approval gates, and agent action boundaries.
- Module 09: cross-tenant leakage and privacy impact.
- Module 11: red-team methodology, evidence collection, and finding quality.
- Module 12: capstone synthesis and final report.

## Debrief prompts

Use these prompts after each BrokenPilot segment:

- What failed: instruction handling, authorization, output handling, memory, tool execution, or auditability?
- Was the model the root cause, or did the surrounding system give the model unsafe authority?
- Which control reduced the risk? What did it not cover?
- What evidence would you need to convince an engineering lead this is worth fixing?
- What would a naive fix look like, and how would it fail?

## Common instructor corrections

- Do not frame the prompt-injection filter as the real defense. It is a teaching stand-in. The stronger lesson is instruction/data separation, least privilege, and constrained authority.
- Do not let students stop at exploit reproduction. The deliverable is a defensible security finding with evidence, impact, recommendation, and residual risk.
- Do not describe tool authorization as an LLM feature. It is application authorization around an LLM-mediated action.
- Do not treat memory poisoning as only a prompt problem. It is also a storage, review, scope, isolation, and provenance problem.

## Solution and grading references

- {rel_link(path, '../labs/brokenpilot/instructor-solution.md', 'BrokenPilot instructor solution')}
- {rel_link(path, '../labs/brokenpilot/worked-examples/current-complete-final-report.md', 'Complete final report example')}
- {rel_link(path, '../labs/brokenpilot/worked-examples/current-final-report-evidence-map.md', 'Final report evidence map')}
- {rel_link(path, '../assessments/brokenpilot-current-final-report-rubric.md', 'BrokenPilot final report rubric')}
- {rel_link(path, '../modules/12-capstone-brokenpilot/instructor-notes.md', 'Module 12 instructor notes')}
"""
    write(path, text)


def write_mlops_guide() -> None:
    path = ROOT / "instructor" / "mlops-evidence-pack-guide.md"
    text = f"""
# MLOps Evidence Pack Instructor Guide

This is the single instructor entry point for the Module 08 MLOps and AI supply-chain evidence-pack lab.

## What the lab teaches

The lab teaches students to review an ML delivery path as a security evidence problem. Students should identify where artifact identity, dependency provenance, dataset provenance, storage controls, promotion gates, validation, rollback, and approval are weak.

This is intentionally a reasoning lab, not a fake CI/CD system. The evidence pack gives students enough material to produce a realistic review without spending the session debugging infrastructure.

## Instructor preparation

Review the evidence pack and model answer before class:

- {rel_link(path, '../labs/mlops-supply-chain-labs/evidence-pack-review/README.md', 'Evidence pack README')}
- {rel_link(path, '../labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md', 'Student lab')}
- {rel_link(path, '../labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md', 'Complete model answer')}
- {rel_link(path, '../labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-evidence-map.md', 'Evidence map')}
- {rel_link(path, '../labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-executive-readout.md', 'Executive readout')}
- {rel_link(path, '../assessments/mlops-evidence-pack-model-answer-rubric.md', 'Model-answer rubric')}

## How to run the session

1. Start from the release decision: should this model be promoted?
2. Give students time to inspect the evidence pack before naming controls.
3. Ask them to separate facts from assumptions.
4. Require every finding to cite a concrete artifact in the pack.
5. Push students beyond dependency pinning. The strongest reviews connect artifact identity, training data, evaluation, promotion, rollback, and ownership.
6. End with a go/no-go recommendation and a staged remediation plan.

## Debrief prompts

- Which finding would stop release immediately, and why?
- Which risks are supply-chain risks, and which are governance or operational risks?
- What evidence is missing but required for a defensible promotion decision?
- Which control gives the highest risk reduction with the least developer friction?
- What would you monitor after deployment if leadership accepted the residual risk?

## Common instructor corrections

- Do not let the lab become a checklist exercise. Students must explain why each weakness matters to release integrity.
- Do not reward generic advice without evidence. Every strong finding should point to a file, field, or workflow in the pack.
- Do not make perfect security the target. The target is a defensible release decision with prioritized remediation.

## Expected student output

A strong submission includes:

- release recommendation
- prioritized findings
- evidence references
- remediation sequence
- residual risk
- owner or decision point
- one executive-readable summary
"""
    write(path, text)


def write_redirect_stub(rel: str, guide_rel: str, title: str) -> None:
    path = ROOT / rel
    if not path.exists():
        return
    # Avoid duplicated facilitation content while keeping links from old references from breaking.
    guide = rel_link(path, guide_rel, title)
    write(path, f"""
# Superseded instructor note

This file no longer carries standalone facilitation guidance.

Use {guide} as the single instructor entry point.
""")


def main() -> None:
    if not (ROOT / "modules").exists() or not (ROOT / "labs").exists() or not (ROOT / "instructor").exists():
        raise SystemExit("Run this script from the repository root.")

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    CONSOLIDATED_ARCHIVE.mkdir(parents=True, exist_ok=True)

    # Archive release-process docs from the instructor teaching root.
    move_if_exists("instructor/FINAL_INSTRUCTOR_READINESS_REVIEW.md", ARCHIVE)
    move_if_exists("instructor/final-voice-cohesion-review-guide.md", ARCHIVE)

    # Archive superseded root-level instructor fragments once the consolidated guides are created.
    # Student-facing debrief files and model answers remain in place.
    move_if_exists("instructor/toy-classifier-facilitation-guide.md", CONSOLIDATED_ARCHIVE)
    move_if_exists("instructor/toy-classifier-debrief-guide.md", CONSOLIDATED_ARCHIVE)
    move_if_exists("instructor/brokenpilot-standalone-facilitation-guide.md", CONSOLIDATED_ARCHIVE)
    move_if_exists("instructor/current-brokenpilot-capstone-debrief-guide.md", CONSOLIDATED_ARCHIVE)
    move_if_exists("instructor/mlops-evidence-pack-facilitation-guide.md", CONSOLIDATED_ARCHIVE)
    move_if_exists("instructor/mlops-evidence-pack-model-answer-debrief.md", CONSOLIDATED_ARCHIVE)

    # Prototype-era instructor runbook is not the supported teaching path.
    move_if_exists("labs/brokenpilot/prototype/instructor-runbook.md", CONSOLIDATED_ARCHIVE)

    write_toy_classifier_guide()
    write_brokenpilot_guide()
    write_mlops_guide()
    write_instructor_readme()

    # Replace app-local instructor note with a pointer if it exists. Keep student DEBRIEF_GUIDE.md untouched.
    write_redirect_stub(
        "labs/toy-ml-attacks/toy-classifier-app/INSTRUCTOR_NOTES.md",
        "../../../instructor/toy-classifier-guide.md",
        "Toy classifier instructor guide",
    )

    patch_40_hour_plan()

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists():
        text = cleanup.read_text(encoding="utf-8")
        marker = "## RC instructor track alignment"
        addition = """
## RC instructor track alignment

Status: completed by the RC instructor-track fix pass.

- `instructor/README.md` is now the instructor spine.
- Major lab families have one facilitation entry point each: toy classifier, BrokenPilot, and MLOps evidence pack.
- Release-process review docs were moved under `instructor/release-readiness/archived-pre-release-docs/`.
- The 40-hour delivery plan now aligns with BrokenPilot-primary module lab paths, with DVAIA optional.
"""
        if marker not in text:
            cleanup.write_text(text.rstrip() + "\n\n" + addition.strip() + "\n", encoding="utf-8", newline="\n")

    print("applied RC instructor-track alignment fixes")


if __name__ == "__main__":
    main()
