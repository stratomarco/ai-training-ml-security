from __future__ import annotations

import subprocess
import sys
import re
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
    "mkdocs.yml",
    ".github/workflows/course-quality.yml",
]

REQUIRED_TEXT = {
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

    version_path = ROOT / "VERSION"
    version = version_path.read_text(encoding="utf-8").strip() if version_path.exists() else ""
    if not re.fullmatch(r"v\d+\.\d+\.\d+", version):
        errors.append(f"VERSION must contain one stable semantic version, got: {version!r}")
    else:
        for rel in (f"release-notes/{version}.md", f"docs/releases/{version}.md"):
            if not (ROOT / rel).is_file():
                errors.append(f"missing current release notes: {rel}")
        if f"Version: `{version}`" not in (ROOT / "COURSE_RELEASE_MANIFEST.md").read_text(encoding="utf-8"):
            errors.append("COURSE_RELEASE_MANIFEST.md version does not match VERSION")
        if f"Current release: {version}." not in (ROOT / "README.md").read_text(encoding="utf-8"):
            errors.append("README.md current release does not match VERSION")
        if f"## {version} " not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
            errors.append("CHANGELOG.md lacks a current release section")

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
        print("release check failed:")
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

    print("release check passed.")


if __name__ == "__main__":
    main()
