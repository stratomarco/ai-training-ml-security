from __future__ import annotations

import os
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-package-scaffolding"
SCRIPT_ARCHIVE = ARCHIVE / "scripts"
DOC_ARCHIVE = ARCHIVE / "docs"

DURABLE_SCRIPT_NAMES = {
    "sync_mkdocs_content.py",
    "check_repo_structure.py",
    "check_content_readiness.py",
    "check_lab_targets.py",
    "check_workflow_validation_baseline.py",
    "check_student_facing_scaffolding.py",
    "check_release_cleanup_phase4.py",
    "apply_release_cleanup_phase4.py",
    "check_no_em_dash.py",  # optional style helper, not a release gate
}

ROOT_DOCS_TO_ARCHIVE = [
    "README_PACKAGE.md",
    "ROUND3_CONTENT_QUALITY_FIXES.md",
    "COURSE_CONTENT_AUDIT.md",
    "COURSE_DRY_RUN_PLAN_40H.md",
    "COURSE_FLOW_REVIEW.md",
    "COURSE_COMPLETION_SCORECARD.md",
    "COURSE_CONTENT_AUDIT.md",
]

BUILD_ARTIFACT_DIRS = [
    ".pytest_cache",
    "__pycache__",
    "site",
]

GITIGNORE_ENTRIES = [
    "",
    "# Generated local artifacts",
    ".mkdocs-src/",
    "site/",
    "**/__pycache__/",
    "**/.pytest_cache/",
    "labs/toy-ml-attacks/toy-classifier-app/model.pkl",
    "labs/toy-ml-attacks/toy-classifier-app/*.pkl",
]

STYLE_GUIDE = """# Final Voice and Prose Cleanup Guide

This guide is for the final manual polish pass before v1.1 is tagged.

The goal is not to make the course sound casual. The goal is to make it sound like a senior security engineer teaching a practical professional course.

## Keep

- Direct explanations of security properties.
- Concrete evidence, controls, validation, and residual risk.
- Plain language about weak controls and tradeoffs.
- The distinction between runnable attack labs and reasoning review labs.
- The central rule: the model may propose, but the system must enforce.

## Reduce

- Repeated phrases such as "this package adds", "this pass creates", and "checked twice" in student-facing content.
- Long enumerations where a short paragraph would be clearer.
- Overly symmetrical sections that make every module sound machine-generated.
- Claims that something is complete, robust, or production-ready without evidence.
- Release-build notes in student-facing module and lab folders.

## Rewrite patterns

Instead of:

> This module provides a comprehensive overview of controls, risks, and remediation strategies.

Use:

> In this module, students decide where the control must live and how they would validate that it works.

Instead of:

> The lab demonstrates the vulnerability and the mitigation.

Use:

> Run the vulnerable path first, then enable the control and show which security property changed.

Instead of:

> Students should understand the importance of X.

Use:

> By the end, students should be able to decide whether X is enforceable, measurable, and safe enough for release.

## Manual pass order

1. README files in the root, modules, and labs.
2. Student reading guides.
3. Lab guides.
4. Worked examples and rubrics.
5. Instructor-only material.

Do not rewrite code comments or test names unless they are confusing.
"""

SCAFFOLDING_REPORT = """# Generated Scaffolding Cleanup Report

Release cleanup phase 4 starts the move from buildout mode to release mode.

## What was archived

- Root package readme files from generated patch packages when present.
- Temporary apply, repair, add, and fix scripts from `scripts/` when present.
- Package-specific check scripts from earlier buildout phases when present.

## What stays active

- `scripts/sync_mkdocs_content.py`
- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/check_workflow_validation_baseline.py`
- `scripts/check_student_facing_scaffolding.py`

## What is not done yet

- MkDocs strict navigation cleanup.
- Public deploy workflow hardening.
- Manual prose polish across all modules.
- Permanent deletion of archived buildout history.

Archived material is kept under `instructor/release-readiness/archived-package-scaffolding/` until final release review decides what to delete.
"""

STUDENT_CHECKLIST = """# Student-Facing Cleanup Checklist

Use this checklist before tagging v1.1.

## Student-facing paths

- `README.md`
- `syllabus.md`
- `course-map.md`
- `modules/`
- `labs/`
- `course-templates/`
- `assessments/`

## Check for

- Buildout package language.
- Temporary script instructions.
- Release-note noise in lab instructions.
- Duplicate lab paths where BrokenPilot or the toy classifier is now primary.
- Lab steps that do not end in a graded artifact.
- Claims that external dependencies are required for the core path.

## Keep out of student path

- Pre-release audits.
- Package readmes.
- Temporary apply scripts.
- Repair scripts.
- Generated source folders such as `.mkdocs-src/` and `site/`.
"""

SCaffolding_CHECK_SCRIPT = r'''from __future__ import annotations

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
'''

PHASE4_CHECK_SCRIPT = r'''from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-package-scaffolding"

REQUIRED = [
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "GENERATED_SCAFFOLDING_CLEANUP_REPORT.md",
    "instructor/release-readiness/student-facing-cleanup-checklist.md",
    "scripts/check_student_facing_scaffolding.py",
    "VALIDATION_BASELINE.md",
]

DURABLE = [
    "scripts/sync_mkdocs_content.py",
    "scripts/check_repo_structure.py",
    "scripts/check_content_readiness.py",
    "scripts/check_lab_targets.py",
]

ALLOWED_ACTIVE_PREFIXES = (
    "check_",
    "sync_",
    "apply_release_cleanup_phase4.py",
)

FORBIDDEN_ACTIVE_PREFIXES = (
    "repair_",
    "fix_",
    "add_",
)


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def main() -> None:
    missing: list[str] = []
    problems: list[str] = []

    for rel in REQUIRED + DURABLE:
        if not exists(rel):
            missing.append(rel)

    if (ROOT / "README_PACKAGE.md").exists():
        problems.append("root README_PACKAGE.md should be archived, not student-facing")

    if SCRIPTS.exists():
        for path in SCRIPTS.glob("*.py"):
            name = path.name
            if name.startswith(FORBIDDEN_ACTIVE_PREFIXES):
                problems.append(f"temporary helper still active: scripts/{name}")
            if name.startswith("apply_") and name != "apply_release_cleanup_phase4.py":
                problems.append(f"old apply script still active: scripts/{name}")

    if not ARCHIVE.exists():
        problems.append("archive directory missing")

    if missing or problems:
        print("Release cleanup phase 4 check failed:")
        for item in missing:
            print(f"- missing: {item}")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)

    print("Release cleanup phase 4 checks passed.")


if __name__ == "__main__":
    main()
'''


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def archive_file(path: Path, target_dir: Path) -> None:
    if not path.exists() or path.is_dir():
        return
    ensure_dir(target_dir)
    target = target_dir / path.name
    if target.exists():
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        target = target_dir / f"{path.stem}-{stamp}{path.suffix}"
    shutil.move(str(path), str(target))
    print(f"archived: {path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")


def archive_temporary_scripts() -> None:
    scripts = ROOT / "scripts"
    if not scripts.exists():
        return
    ensure_dir(SCRIPT_ARCHIVE)

    for path in sorted(scripts.glob("*.py")):
        name = path.name
        if name in DURABLE_SCRIPT_NAMES:
            continue
        if name.startswith(("apply_", "repair_", "add_", "fix_")):
            archive_file(path, SCRIPT_ARCHIVE)
            continue
        if name.startswith("check_") and name not in DURABLE_SCRIPT_NAMES:
            # Package-era checks are useful history but should not remain active.
            archive_file(path, SCRIPT_ARCHIVE)


def archive_root_docs() -> None:
    ensure_dir(DOC_ARCHIVE)
    for rel in ROOT_DOCS_TO_ARCHIVE:
        archive_file(ROOT / rel, DOC_ARCHIVE)


def remove_generated_artifacts() -> None:
    # Remove cache/build artifacts, but leave .mkdocs-src alone because the team is postponing MkDocs cleanup.
    for path in ROOT.rglob("__pycache__"):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
            print(f"removed cache: {path.relative_to(ROOT)}")
    for path in ROOT.rglob(".pytest_cache"):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
            print(f"removed cache: {path.relative_to(ROOT)}")

    model = ROOT / "labs" / "toy-ml-attacks" / "toy-classifier-app" / "model.pkl"
    if model.exists():
        model.unlink()
        print(f"removed generated model artifact: {model.relative_to(ROOT)}")


def update_gitignore() -> None:
    path = ROOT / ".gitignore"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = existing.splitlines()
    changed = False
    for entry in GITIGNORE_ENTRIES:
        if entry == "":
            continue
        if entry not in lines:
            lines.append(entry)
            changed = True
    if changed or not path.exists():
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
        print("updated: .gitignore")


def write_docs_and_checks() -> None:
    (ROOT / "STYLE_AND_VOICE_FINAL_PASS.md").write_text(STYLE_GUIDE, encoding="utf-8", newline="\n")
    (ROOT / "GENERATED_SCAFFOLDING_CLEANUP_REPORT.md").write_text(SCAFFOLDING_REPORT, encoding="utf-8", newline="\n")
    checklist = ROOT / "instructor" / "release-readiness" / "student-facing-cleanup-checklist.md"
    ensure_dir(checklist.parent)
    checklist.write_text(STUDENT_CHECKLIST, encoding="utf-8", newline="\n")

    (ROOT / "scripts" / "check_student_facing_scaffolding.py").write_text(SCaffolding_CHECK_SCRIPT, encoding="utf-8", newline="\n")
    (ROOT / "scripts" / "check_release_cleanup_phase4.py").write_text(PHASE4_CHECK_SCRIPT, encoding="utf-8", newline="\n")
    print("wrote phase 4 docs and checks")


def update_cleanup_doc() -> None:
    path = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    text = path.read_text(encoding="utf-8") if path.exists() else "# Cleanup Before Release\n"
    marker = "## Release cleanup phase 4"
    if marker not in text:
        text = text.rstrip() + "\n\n" + marker + "\n\n- Archived package-era scaffolding and temporary scripts.\n- Added final voice cleanup guidance.\n- Added student-facing scaffolding check.\n- Kept MkDocs strict cleanup postponed until navigation is intentionally finalized.\n"
        path.write_text(text, encoding="utf-8", newline="\n")
        print("updated: CLEANUP_BEFORE_RELEASE.md")


def main() -> None:
    ensure_dir(ARCHIVE)
    archive_root_docs()
    write_docs_and_checks()
    archive_temporary_scripts()
    remove_generated_artifacts()
    update_gitignore()
    update_cleanup_doc()
    print("\nApplied release cleanup phase 4.")


if __name__ == "__main__":
    main()
