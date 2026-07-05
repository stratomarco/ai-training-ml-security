from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_PROCESS = "instructor/release-readiness/release-process-docs"

REQUIRED_FILES = [
    "VERSION",
    "COURSE_RELEASE_MANIFEST.md",
    f"{RELEASE_PROCESS}/RELEASE_CANDIDATE_CHECKLIST.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    f"{RELEASE_PROCESS}/QUALITY_GATE_BASELINE.md",
    "PUBLISHED_COURSE_VIEW.md",
    "CHANGELOG.md",
    "release-notes/v1.1-dev-release-candidate.md",
    "mkdocs.yml",
    ".github/workflows/course-quality.yml",
]

REQUIRED_TEXT = {
    "VERSION": ["v1.1-dev-rc1"],
    "COURSE_RELEASE_MANIFEST.md": [
        "mkdocs build --strict",
        "BrokenPilot",
        "toy classifier",
        "labs/brokenpilot/prototype-app/",
    ],
    f"{RELEASE_PROCESS}/QUALITY_GATE_BASELINE.md": [
        "scripts/check_repo_structure.py",
        "scripts/check_content_readiness.py",
        "scripts/check_lab_targets.py",
        "mkdocs build --strict",
    ],
    "USAGE_AND_LICENSING_GUIDE.md": [
        "Creative Commons Attribution-NonCommercial-ShareAlike",
        "PolyForm Noncommercial",
        "not be described as OSI open source",
    ],
}


def run(command: list[str], cwd: Path = ROOT) -> None:
    print("+ " + " ".join(command))
    completed = subprocess.run(command, cwd=cwd)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> None:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")

    for rel, needles in REQUIRED_TEXT.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} missing required text: {needle}")

    if errors:
        print("release candidate check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    durable_checks = [
        "scripts/check_repo_structure.py",
        "scripts/check_content_readiness.py",
        "scripts/check_lab_targets.py",
        "scripts/check_workflow_validation_baseline.py",
        "scripts/check_root_process_docs.py",
    ]

    for rel in durable_checks:
        if (ROOT / rel).exists():
            run([sys.executable, rel])

    print("release candidate phase 8 check passed.")


if __name__ == "__main__":
    main()
