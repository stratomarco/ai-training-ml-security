from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "FINAL_HUMAN_POLISH_REPORT.md",
    "instructor/release-readiness/final-human-polish-report.md",
]

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

BLOCKED_STUDENT_PHRASES = [
    "unzip/copy the package",
    "No MkDocs fight",
    "no MkDocs fight",
    "checked twice",
    "sandbox:/mnt/data",
    "Download: [",
    "The apply script creates",
    "the apply script creates",
    "python scripts\\apply_",
    "python scripts/apply_",
]


def is_student_facing(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    first = rel.split("/", 1)[0]
    return rel in STUDENT_ROOTS or first in STUDENT_ROOTS


def main() -> None:
    failures: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            failures.append(f"missing: {rel}")

    for path in ROOT.rglob("*.md"):
        if not is_student_facing(path):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for phrase in BLOCKED_STUDENT_PHRASES:
            if phrase in text:
                failures.append(f"student-facing scaffold phrase in {path.relative_to(ROOT)}: {phrase}")

    if failures:
        print("Manual voice polish check failed:")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)

    print("Manual voice polish checks passed.")


if __name__ == "__main__":
    main()
