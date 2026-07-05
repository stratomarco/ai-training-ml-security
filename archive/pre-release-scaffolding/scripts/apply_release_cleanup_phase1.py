from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "archive" / "pre-release-scaffolding"
SCRIPT_ARCHIVE = ARCHIVE / "scripts"
NOTE_ARCHIVE = ARCHIVE / "release-notes"
PACKAGE_ARCHIVE = ARCHIVE / "package-readmes"

DURABLE_SCRIPT_ALLOWLIST = {
    "sync_mkdocs_content.py",
    "check_repo_structure.py",
    "check_release_cleanup_phase1.py",
    "check_content_readiness.py",
    "check_lab_targets.py",
    "check_round2_release_readiness.py",
    "check_delivery_profiles.py",
    "check_standalone_path.py",
    "cleanup_duplicate_content.ps1",
    "cleanup_duplicate_content.sh",
}

PACKAGE_README_NAMES = {"README_PACKAGE.md", "README_PART6.md"}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def move_file(src: Path, dst: Path) -> None:
    if not src.exists() or not src.is_file():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    shutil.move(str(src), str(dst))
    print(f"archived: {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def archive_temporary_scripts() -> list[str]:
    archived: list[str] = []
    if not SCRIPTS.exists():
        return archived
    for path in sorted(SCRIPTS.glob("*.py")):
        name = path.name
        temporary = (
            name.startswith("apply_")
            or name.startswith("repair_")
            or name.startswith("add_")
            or name.startswith("fix_")
            or (name.startswith("check_") and name not in DURABLE_SCRIPT_ALLOWLIST)
        )
        if temporary and name not in DURABLE_SCRIPT_ALLOWLIST:
            move_file(path, SCRIPT_ARCHIVE / name)
            archived.append(name)
    return archived


def archive_package_readmes() -> list[str]:
    archived: list[str] = []
    for name in PACKAGE_README_NAMES:
        path = ROOT / name
        if path.exists():
            move_file(path, PACKAGE_ARCHIVE / name)
            archived.append(name)
    return archived


def consolidate_release_notes() -> list[str]:
    release_notes = ROOT / "release-notes"
    moved: list[str] = []
    if not release_notes.exists():
        return moved
    entries: list[str] = []
    for path in sorted(release_notes.glob("v1.1-dev-*.md")):
        if path.name == "v1.1-dev-release-cleanup-phase1.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        title = next((line.strip("# ").strip() for line in text.splitlines() if line.startswith("#")), path.stem)
        entries.append(f"- {title} ({path.name})")
        move_file(path, NOTE_ARCHIVE / path.name)
        moved.append(path.name)
    if entries:
        worklog = release_notes / "v1.1-dev-worklog.md"
        existing = worklog.read_text(encoding="utf-8") if worklog.exists() else "# v1.1-dev worklog\n"
        marker = "## Consolidated package notes"
        section = marker + "\n\n" + "\n".join(entries) + "\n"
        if marker not in existing:
            write(worklog, existing.rstrip() + "\n\n" + section)
    return moved


def create_durable_checks() -> None:
    write(SCRIPTS / "check_content_readiness.py", r'''
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "COURSE_STORYLINE.md",
    "COURSE_CONTENT_AUDIT.md",
    "COURSE_COMPLETION_SCORECARD.md",
    "COURSE_DRY_RUN_PLAN_40H.md",
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md",
    "labs/LAB_QUALITY_STANDARD.md",
    "labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md",
    "labs/brokenpilot/CAPSTONE_FINAL_REPORT_CURRENT_PATH.md",
    "labs/brokenpilot/worked-examples/current-complete-final-report.md",
    "labs/toy-ml-attacks/toy-classifier-app/README.md",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py",
    "labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md",
    "assessments/END_TO_END_ASSESSMENT_MAP.md",
    "instructor/teaching-the-course-as-one-journey.md",
]
MODULES = [
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
MODULE_REQUIRED = ["README.md", "student-reading-guide.md", "cohesion-note.md"]
DEPTH_REQUIRED = ["deep-dive.md", "attack-anatomy.md", "controls-and-remediations.md", "common-mistakes.md", "worked-example.md"]
def require(path: str, errors: list[str]) -> None:
    if not (ROOT / path).exists():
        errors.append(f"missing: {path}")
def main() -> None:
    errors: list[str] = []
    for path in REQUIRED_FILES:
        require(path, errors)
    for module in MODULES:
        for filename in MODULE_REQUIRED:
            require(f"modules/{module}/{filename}", errors)
        for filename in DEPTH_REQUIRED:
            require(f"modules/{module}/{filename}", errors)
    if errors:
        print("Content readiness check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Content readiness check passed.")
if __name__ == "__main__":
    main()
''')
    write(SCRIPTS / "check_lab_targets.py", r'''
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "labs/brokenpilot/prototype-app/app/main.py",
    "labs/brokenpilot/prototype-app/app/mock_llm.py",
    "labs/brokenpilot/prototype-app/app/controls.py",
    "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md",
    "labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md",
    "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md",
    "labs/toy-ml-attacks/toy-classifier-app/train.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/poisoning.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/extraction.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/output_integrity.py",
    "labs/mlops-supply-chain-labs/evidence-pack-review/README.md",
    "labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md",
]
TEXT_EXPECTATIONS = {
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py": ["run_evasion", "malicious", "phish", "safe"],
    "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md": ["POST /render", "ENABLE_OUTPUT_ENCODING=false", "ENABLE_OUTPUT_ENCODING=true"],
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md": ["BrokenPilot", "toy-classifier", "MLOps"],
}
def main() -> None:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")
    for rel, needles in TEXT_EXPECTATIONS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing text target: {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} missing expected text: {needle}")
    if errors:
        print("Lab target check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Lab target check passed.")
if __name__ == "__main__":
    main()
''')


def update_cleanup_doc(archived_scripts: list[str], archived_notes: list[str]) -> None:
    path = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Cleanup before release\n"
    section = f"""

## Release cleanup phase 1 completed

Temporary package scaffolding has been archived under `archive/pre-release-scaffolding/` instead of being left in the active course tree.

Archived scripts: {len(archived_scripts)}
Archived package release notes: {len(archived_notes)}

Keep active during the remaining release work:

- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/sync_mkdocs_content.py`

Still pending for final release cleanup:

- remove or delete `archive/pre-release-scaffolding/` once the release branch is stable;
- finish MkDocs navigation and re-enable strict site build;
- stabilize GitHub workflows for final release;
- run a voice pass on module README files if review finds generated-looking phrasing;
- remove generated `site/`, `.mkdocs-src/`, caches, and local virtual environments.
"""
    if "## Release cleanup phase 1 completed" not in existing:
        write(path, existing.rstrip() + section)


def write_report(archived_scripts: list[str], archived_readmes: list[str], archived_notes: list[str]) -> None:
    script_list = "\n".join(f"- `{name}`" for name in archived_scripts) or "- None"
    readme_list = "\n".join(f"- `{name}`" for name in archived_readmes) or "- None"
    note_list = "\n".join(f"- `{name}`" for name in archived_notes) or "- None"
    write(ROOT / "RELEASE_CLEANUP_PHASE1_REPORT.md", f"""
# Release cleanup phase 1 report

This cleanup pass reduces active development scaffolding without changing course content, labs, or assessments.

## What changed

- Temporary package `apply_*`, `repair_*`, `add_*`, and package-specific `check_*` scripts were archived.
- Package-level `README_PACKAGE.md` files were archived when present.
- Package-level `release-notes/v1.1-dev-*.md` files were consolidated into `release-notes/v1.1-dev-worklog.md` and archived.
- Durable readiness checks were added:
  - `scripts/check_content_readiness.py`
  - `scripts/check_lab_targets.py`

## Archived scripts

{script_list}

## Archived package README files

{readme_list}

## Archived package release notes

{note_list}

## What this pass intentionally did not do

- It did not fight MkDocs strict navigation.
- It did not delete the archive directory.
- It did not rewrite module prose.
- It did not change runnable lab code.
- It did not change GitHub workflows.

Those are later release-hardening tasks.
""")


def write_release_note() -> None:
    write(ROOT / "release-notes" / "v1.1-dev-release-cleanup-phase1.md", """
# v1.1-dev release cleanup phase 1

This pass reduces active development scaffolding now that the major content and lab work is stable.

## Added

- `RELEASE_CLEANUP_PHASE1_REPORT.md`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`

## Changed

- Archived temporary package apply/check/repair scripts under `archive/pre-release-scaffolding/`.
- Consolidated package-level release notes into `release-notes/v1.1-dev-worklog.md`.

## Not included

- MkDocs strict navigation cleanup.
- GitHub workflow hardening.
- Final prose cleanup.
- Archive deletion.
""")


def main() -> None:
    archived_scripts = archive_temporary_scripts()
    archived_readmes = archive_package_readmes()
    archived_notes = consolidate_release_notes()
    create_durable_checks()
    write_release_note()
    update_cleanup_doc(archived_scripts, archived_notes)
    write_report(archived_scripts, archived_readmes, archived_notes)
    print("\nRelease cleanup phase 1 applied.")

if __name__ == "__main__":
    main()
