from __future__ import annotations

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {
    ".git",
    ".venv",
    ".mkdocs-src",
    "site",
    "__pycache__",
    ".pytest_cache",
    "archive",
    "release-notes",
    "releases",
    "release-readiness",
}

STUDENT_ROOTS = {
    "README.md",
    "syllabus.md",
    "PUBLISHED_COURSE_VIEW.md",
    "COURSE_STORYLINE.md",
    "labs",
    "modules",
    "assessments",
    "course-templates",
}

SCAFFOLD_LINE_MARKERS = [
    "# unzip/copy the package",
    "unzip/copy the package",
    "No MkDocs fight",
    "no MkDocs fight",
    "checked twice",
    "Download: [",
    "sandbox:/mnt/data",
    "python scripts\\apply_",
    "python scripts/apply_",
    "The apply script creates",
    "the apply script creates",
    "The apply script adds",
    "the apply script adds",
]

SAFE_REPLACEMENTS = {
    "This package adds": "This release update adds",
    "This package creates": "This release update creates",
    "This package does": "This release update does",
    "apply script": "course update",
    "Apply script": "Course update",
}

STYLE_GUIDE = """
# Final Human Voice Polish

This course should read like a practical security engineering course, not like a generated content bundle.

The final edit should preserve the technical argument and remove only the wording that distracts from it. Do not make broad rewrites for style alone. Keep evidence, root cause, control placement, validation, and residual risk intact.

## Voice principles

- Use direct engineering language: inspect, enforce, validate, approve, log, monitor, rollback.
- Explain why a control changes the security property.
- Keep the distinction between runnable labs and reasoning labs explicit.
- Keep BrokenPilot, the toy classifier, and the MLOps evidence pack in their correct roles.
- Avoid vague phrases such as "add guardrails" unless the next sentence names the actual enforcing control.

## Course storyline

The course teaches one idea across different ML system shapes: the model may influence behavior, but the system must enforce security boundaries. Students practice that idea through architecture review, runnable failures, tabletop reasoning, graded findings, and a capstone report.

## What to leave alone

Do not remove repeated structure from rubrics, templates, or checklists when the repetition helps grading. Those files should be predictable. Polish explanatory prose first.

## Final manual review order

1. `README.md` and `PUBLISHED_COURSE_VIEW.md`
2. `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md`
3. Module README files
4. Student reading guides
5. Lab guides
6. Worked examples and model answers
7. Instructor-only material
"""

POLISH_REPORT = """
# Final Human Polish Report

This phase applies conservative cleanup only. It removes package-era lines from student-facing Markdown and records the editing standard for the final release candidate.

## What changed

- Student-facing files were scanned for package-era lines such as download links, apply-script instructions, and "checked twice" validation phrasing.
- Root `README_PACKAGE.md` files were archived when present.
- The final voice guide was refreshed with release-candidate language.

## What did not change

- Lab behavior was not changed.
- MkDocs strict navigation was not changed.
- CI behavior was not changed.
- Course prose was not broadly rewritten.

## Next phase

After this pass, the next work should be the MkDocs/navigation release candidate pass.
"""


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {rel}")


def append_once(rel: str, marker: str, text: str) -> None:
    path = ROOT / rel
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in current:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(current.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8", newline="\n")
        print(f"updated: {rel}")


def is_student_facing(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    first = rel.split("/", 1)[0]
    return rel in STUDENT_ROOTS or first in STUDENT_ROOTS


def cleanup_student_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Remove single-line package-era instructions from student-facing files.
    lines = []
    for line in text.splitlines():
        if any(marker in line for marker in SCAFFOLD_LINE_MARKERS):
            continue
        lines.append(line)
    text = "\n".join(lines)

    # Apply only conservative replacements to remaining text.
    for old, new in SAFE_REPLACEMENTS.items():
        text = text.replace(old, new)

    # Collapse excessive blank lines introduced by line removal.
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    if text != original:
        path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
        print(f"polished: {path.relative_to(ROOT)}")
        return True
    return False


def archive_root_package_readme() -> None:
    src = ROOT / "README_PACKAGE.md"
    if not src.exists():
        return
    dst = ROOT / "instructor/release-readiness/archived-package-readmes/README_PACKAGE.phase6-manual-voice-polish.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    print(f"archived: {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.md"):
        if is_student_facing(path):
            if cleanup_student_file(path):
                changed += 1

    write("STYLE_AND_VOICE_FINAL_PASS.md", STYLE_GUIDE)
    write("FINAL_HUMAN_POLISH_REPORT.md", POLISH_REPORT)
    write("instructor/release-readiness/final-human-polish-report.md", POLISH_REPORT)

    append_once(
        "CLEANUP_BEFORE_RELEASE.md",
        "## Phase 6 manual voice polish",
        """
## Phase 6 manual voice polish

Status: started.

- Package-era lines are removed from student-facing Markdown.
- Final voice guidance is recorded in `STYLE_AND_VOICE_FINAL_PASS.md`.
- Broad automatic prose rewrites are intentionally avoided.
- Remaining release work: MkDocs strict navigation, final workflow hardening, and release candidate validation.
""",
    )

    archive_root_package_readme()
    print(f"\nManual voice polish complete. Student-facing files changed: {changed}")


if __name__ == "__main__":
    main()
