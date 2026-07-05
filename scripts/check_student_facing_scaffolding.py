from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STUDENT_DIRS = [
    ROOT / "modules",
    ROOT / "labs",
    ROOT / "course-templates",
    ROOT / "assessments",
]

FORBIDDEN_PHRASES = [
    "# unzip/copy the package",
    "python scripts\\apply_",
    "python scripts/apply_",
    "README_PACKAGE.md",
    "Applied Round",
    "this package adds",
    "checked it twice",
]

ALLOWED_PATH_PARTS = {
    "archive",
    "release-readiness",
    "worked-examples",  # examples may discuss before/after package history in rare cases
}


def should_skip(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    return bool(parts & ALLOWED_PATH_PARTS)


def main() -> None:
    findings: list[str] = []

    for base in STUDENT_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if should_skip(path):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            original = path.read_text(encoding="utf-8", errors="ignore")
            for phrase in FORBIDDEN_PHRASES:
                if phrase.lower() in text or phrase in original:
                    findings.append(f"{path.relative_to(ROOT)} contains package-scaffolding phrase: {phrase}")

    if findings:
        print("Student-facing scaffolding check failed:")
        for finding in findings:
            print(f"- {finding}")
        raise SystemExit(1)

    print("Student-facing scaffolding check passed.")


if __name__ == "__main__":
    main()
