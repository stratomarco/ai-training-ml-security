from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {rel}")


def append_once(rel: str, marker: str, text: str) -> None:
    path = ROOT / rel
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in current:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(current.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8", newline="\n")
        print(f"updated: {rel}")


STYLE_GUIDE = """
# Final Voice and Content Polish Pass

This pass is for the final human edit before release. Do not treat it as a rewrite of the course. The goal is to make the material feel authored, coherent, and practical without weakening the technical content.

## Editing principles

1. Preserve the security argument.
   - Do not remove evidence, root cause, control, validation, or residual-risk language.
   - Do not simplify a finding into vague advice.

2. Prefer concrete engineering language.
   - Say what the engineer should inspect, enforce, test, or document.
   - Avoid generic lines that could fit any security course.

3. Reduce repeated generated-looking patterns.
   - Avoid starting many adjacent sections with the same phrase.
   - Replace repeated boilerplate with context-specific transitions.
   - Keep repeated structure where it helps grading, but vary explanatory prose.

4. Keep the course voice.
   - Direct, practical, security-engineering oriented.
   - Reading-first, lab-supported.
   - Honest about what is runnable, what is tabletop, and why.

5. Do not overclaim.
   - BrokenPilot demonstrates LLM/RAG/agent/privacy/red-team application risk.
   - The toy classifier demonstrates classical ML attack concepts.
   - The MLOps evidence pack demonstrates review of supply-chain evidence.
   - Tabletops are reasoning labs, not failed runnable labs.

## High-value files to review manually

Review these first because they shape the student experience:

- `README.md`
- `syllabus.md`
- `PUBLISHED_COURSE_VIEW.md`
- `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md`
- `labs/LAB_QUALITY_STANDARD.md`
- `modules/*/README.md`
- `modules/*/student-reading-guide.md`
- `labs/brokenpilot/worked-examples/current-complete-final-report.md`
- `labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md`
- `labs/toy-ml-attacks/toy-classifier-app/README.md`

## Phrases to treat as review prompts, not automatic errors

The style reporter flags phrases such as:

- "This package"
- "checked twice"
- "apply script"
- "the apply script creates"
- "generated"
- "placeholder"
- "TODO"
- "student should"
- repeated openings such as "This module" or "This lab"

These are not always wrong. They are prompts for a human editor to inspect context.

## What good final prose looks like

Good final prose answers:

- What decision is the student learning to make?
- What evidence would change that decision?
- What control would actually enforce the boundary?
- How would the student validate the control?
- What residual risk remains?

## What to avoid

Avoid prose that only says:

- "Add guardrails."
- "Use monitoring."
- "Improve security."
- "The model can be tricked."
- "Follow best practices."

Those phrases are acceptable only when followed by concrete control placement, validation, and residual risk.
"""

CHECKLIST = """
# Student-Facing Voice Polish Checklist

Use this checklist when reviewing the course after all content and lab packages are applied.

## Course-level checks

- The course introduction explains why ML security is security engineering for systems that contain ML.
- The 40-hour course path is easy to understand.
- The student can tell which labs are required and which are optional.
- DVAIA is clearly optional appendix material, not the primary hands-on path.
- BrokenPilot, toy classifier, and MLOps evidence pack each have a clear teaching role.

## Module checks

For each module:

- The opening paragraph is specific to the module.
- The module states the decision students must learn to make.
- The module links to the right lab or reasoning exercise.
- The graded artifact is named.
- The module does not overclaim what the lab demonstrates.
- The handoff to the next module is clear.

## Lab checks

For each attack lab:

- The failure is observable.
- The fix or control changes observable behavior.
- The naive fix is discussed or shown to be insufficient.
- The graded artifact is a control or review deliverable, not just proof of exploitation.

For each reasoning lab:

- The tabletop modality is justified.
- The evidence or scenario is concrete.
- The deliverable includes recommendation, validation, and residual risk.
- Strong and weak anchors are available or explicitly linked.

## Cleanup checks

- Student-facing pages do not mention temporary package scripts.
- Student-facing pages do not mention local validation history unless it is useful to learners.
- Release notes and pre-release audit reports are not part of the normal learning path.
- Archived scaffolding is not linked as required student material.
"""

REPORT = """
# Voice Polish Hotspot Report

This file is intentionally a working report. Run `python scripts/report_voice_polish_hotspots.py` to generate a fresh terminal report while editing.

## Current status

Phase 5 adds the human-editing tools but does not rewrite content automatically.

## Review order

1. Course entry points.
2. Module README files.
3. Student reading guides.
4. Lab guides.
5. Worked examples and model answers.
6. Instructor-only material.

## Decision

Do not begin MkDocs strict navigation cleanup until the human voice pass is complete.
"""

HOTSPOT_SCRIPT = r'''
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

STUDENT_PATHS = [
    "README.md",
    "syllabus.md",
    "PUBLISHED_COURSE_VIEW.md",
    "labs",
    "modules",
    "course-templates",
    "assessments",
]

SKIP_PARTS = {
    ".git",
    ".venv",
    ".mkdocs-src",
    "site",
    "archive",
    "release-notes",
    "releases",
    "release-readiness",
    "__pycache__",
}

PHRASES = [
    "this package",
    "checked twice",
    "apply script",
    "the apply script",
    "generated",
    "placeholder",
    "todo",
    "fix later",
    "mkdocs fight",
    "no mkdocs fight",
    "student should",
    "students should",
    "best practices",
    "add guardrails",
    "improve security",
]

OPENING_PATTERNS = [
    re.compile(r"^this module\b", re.I),
    re.compile(r"^this lab\b", re.I),
    re.compile(r"^this exercise\b", re.I),
    re.compile(r"^students will\b", re.I),
]


def is_student_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    if path.suffix.lower() != ".md":
        return False
    return any(rel == item or rel.startswith(item.rstrip("/") + "/") for item in STUDENT_PATHS)


def line_numbered_matches(path: Path) -> list[tuple[int, str, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: list[tuple[int, str, str]] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        low = line.lower()
        for phrase in PHRASES:
            if phrase in low:
                out.append((idx, phrase, line.strip()))
    return out


def opening_stats(path: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        for pattern in OPENING_PATTERNS:
            if pattern.search(stripped):
                counts[pattern.pattern] += 1
    return counts


def main() -> None:
    files = [path for path in ROOT.rglob("*.md") if is_student_file(path)]
    print(f"Student-facing Markdown files scanned: {len(files)}")

    phrase_hits: list[tuple[str, int, str, str]] = []
    opening_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        for line_no, phrase, line in line_numbered_matches(path):
            phrase_hits.append((rel, line_no, phrase, line))
        counts = opening_stats(path)
        if counts:
            opening_counts[rel].update(counts)

    print("\nPhrase hotspots, review manually:")
    if not phrase_hits:
        print("- none")
    else:
        for rel, line_no, phrase, line in phrase_hits[:200]:
            print(f"- {rel}:{line_no}: [{phrase}] {line}")
        if len(phrase_hits) > 200:
            print(f"- ... {len(phrase_hits) - 200} more")

    print("\nRepeated opening patterns, review manually:")
    any_openings = False
    for rel, counts in sorted(opening_counts.items()):
        total = sum(counts.values())
        if total >= 3:
            any_openings = True
            print(f"- {rel}: {dict(counts)}")
    if not any_openings:
        print("- none above threshold")

    print("\nResult: report complete. These are review prompts, not automatic failures.")


if __name__ == "__main__":
    main()
'''

CHECK_SCRIPT = r'''
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "VOICE_POLISH_PASS_REPORT.md",
    "instructor/release-readiness/student-facing-cleanup-checklist.md",
    "instructor/release-readiness/final-human-editor-pass.md",
    "scripts/report_voice_polish_hotspots.py",
]


def main() -> None:
    missing = [rel for rel in REQUIRED if not (ROOT / rel).exists()]
    if missing:
        print("Release cleanup phase 5 check failed:")
        for rel in missing:
            print(f"- missing: {rel}")
        raise SystemExit(1)

    guide = (ROOT / "STYLE_AND_VOICE_FINAL_PASS.md").read_text(encoding="utf-8")
    for phrase in ["Preserve the security argument", "Do not overclaim", "What good final prose looks like"]:
        if phrase not in guide:
            raise SystemExit(f"Release cleanup phase 5 check failed: style guide missing {phrase!r}")

    print("Release cleanup phase 5 checks passed.")


if __name__ == "__main__":
    main()
'''


def main() -> None:
    write("STYLE_AND_VOICE_FINAL_PASS.md", STYLE_GUIDE)
    write("instructor/release-readiness/student-facing-cleanup-checklist.md", CHECKLIST)
    write("instructor/release-readiness/final-human-editor-pass.md", STYLE_GUIDE)
    write("VOICE_POLISH_PASS_REPORT.md", REPORT)
    write("scripts/report_voice_polish_hotspots.py", HOTSPOT_SCRIPT)
    write("scripts/check_release_cleanup_phase5.py", CHECK_SCRIPT)

    append_once(
        "CLEANUP_BEFORE_RELEASE.md",
        "Release cleanup phase 5",
        """
## Release cleanup phase 5

Status: voice and content polish toolkit added.

Before the release candidate, run:

```powershell
python scripts/report_voice_polish_hotspots.py
python scripts/check_release_cleanup_phase5.py
```

Use the hotspot report as a manual editing aid, not as a hard failure gate.
""",
    )

    print("Applied release cleanup phase 5 voice polish toolkit.")


if __name__ == "__main__":
    main()
