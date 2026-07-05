from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = ROOT / "instructor" / "release-readiness"
PRE_RELEASE_ARCHIVE = ARCHIVE_ROOT / "archived-pre-release-docs"
BROKENPILOT_ARCHIVE = ROOT / "labs" / "brokenpilot" / "prototype" / "archive"

ROOT_PRE_RELEASE_DOCS = [
    "COURSE_CONTENT_AUDIT.md",
    "COURSE_DRY_RUN_PLAN_40H.md",
    "COURSE_FLOW_REVIEW.md",
    "COURSE_COMPLETION_SCORECARD.md",
    "COURSE_VOICE_AND_COHESION_REVIEW.md",
    "ROUND3_CONTENT_QUALITY_FIXES.md",
    "RELEASE_CLEANUP_PHASE1_REPORT.md",
    "README_PACKAGE.md",
]

LAB_READINESS_DOCS = [
    ROOT / "labs" / "FINAL_LAB_READINESS_REVIEW.md",
    ROOT / "instructor" / "FINAL_LAB_READINESS_REVIEW.md",
]

BROKENPILOT_SUPERSEDED_PLAN_DOCS = [
    "build-backlog.md",
    "control-toggle-plan.md",
    "vulnerability-implementation-plan.md",
    "fake-data-plan.md",
    "docker-compose-plan.md",
    "api-contract.md",
]


def ensure_dirs() -> None:
    ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)
    PRE_RELEASE_ARCHIVE.mkdir(parents=True, exist_ok=True)
    BROKENPILOT_ARCHIVE.mkdir(parents=True, exist_ok=True)


def write_if_changed(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = text.rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        return
    path.write_text(normalized, encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def move_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        # Keep the archive stable and idempotent. If the source and destination both
        # exist, preserve the destination and remove the duplicate source only when
        # the content is identical. Otherwise keep both by suffixing the new copy.
        try:
            if src.read_text(encoding="utf-8") == dst.read_text(encoding="utf-8"):
                src.unlink()
                print(f"removed duplicate: {src.relative_to(ROOT)}")
                return
        except UnicodeDecodeError:
            pass
        stem, suffix = dst.stem, dst.suffix
        counter = 2
        candidate = dst.with_name(f"{stem}-{counter}{suffix}")
        while candidate.exists():
            counter += 1
            candidate = dst.with_name(f"{stem}-{counter}{suffix}")
        dst = candidate
    shutil.move(str(src), str(dst))
    print(f"moved: {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def archive_root_pre_release_docs() -> None:
    for name in ROOT_PRE_RELEASE_DOCS:
        move_file(ROOT / name, PRE_RELEASE_ARCHIVE / name)


def archive_lab_readiness_docs() -> None:
    for src in LAB_READINESS_DOCS:
        move_file(src, PRE_RELEASE_ARCHIVE / src.name)


def archive_brokenpilot_plan_docs() -> None:
    prototype_dir = ROOT / "labs" / "brokenpilot" / "prototype"
    if not prototype_dir.exists():
        return
    for name in BROKENPILOT_SUPERSEDED_PLAN_DOCS:
        move_file(prototype_dir / name, BROKENPILOT_ARCHIVE / name)

    write_if_changed(
        BROKENPILOT_ARCHIVE / "README.md",
        """
# BrokenPilot archived prototype planning notes

These files are preserved as design history. They are not the current student lab path.

Use `labs/brokenpilot/prototype-app/` for the tested BrokenPilot implementation and current labs.
""",
    )


def write_release_readiness_index() -> None:
    write_if_changed(
        ARCHIVE_ROOT / "README.md",
        """
# Release readiness archive

This directory holds pre-release review material, package worklogs, and build-time notes that are useful for maintainers but should not be part of the normal student path.

Student-facing course material should remain in:

- `modules/`
- `labs/`
- `course-templates/`
- `assessments/`
- selected `docs/start-here/` pages

Before a public release, review this directory and decide what to keep as instructor-only history, what to fold into durable course material, and what to delete.
""",
    )
    write_if_changed(
        PRE_RELEASE_ARCHIVE / "README.md",
        """
# Archived pre-release documents

These documents were useful during v1.1-dev construction and review. They are archived so they do not appear as part of the student course path.

Do not treat these files as required student reading. They can inform release notes, instructor retrospectives, or future course maintenance.
""",
    )


def write_published_course_view() -> None:
    write_if_changed(
        ROOT / "PUBLISHED_COURSE_VIEW.md",
        """
# Published course view

This file defines what should feel student-facing in the final v1.1 release.

## Student-facing by default

- `README.md`
- `syllabus.md`
- `course-map.md`
- `modules/`
- `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md`
- `labs/STUDENT_LAB_JOURNAL_GUIDE.md`
- runnable lab folders under `labs/`
- `course-templates/`
- `assessments/` that students use to understand grading expectations

## Instructor-facing by default

- `instructor/`
- grading calibration notes
- strong and weak answer anchors
- debrief guides
- release-readiness notes

## Maintainer-only or release-readiness material

- temporary apply scripts
- package-specific check scripts
- package release notes
- pre-release audit documents
- build-time prototype plans superseded by runnable labs

## Cleanup rule

If a document describes how the course was built, reviewed, packaged, or repaired, it does not belong in the student path. Move it to `instructor/release-readiness/` or delete it during final cleanup.

If a document helps a student understand a concept, perform a lab, complete a deliverable, or interpret feedback, keep it in the course path.
""",
    )


def update_cleanup_before_release() -> None:
    path = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Cleanup before release\n"
    marker = "## Release cleanup phase 2 status"
    if marker in existing:
        return
    addition = """

## Release cleanup phase 2 status

Completed during the student-facing tree cleanup pass:

- moved pre-release audit documents out of the repository root when present
- moved final lab readiness review material out of the student-facing `labs/` path when present
- archived superseded BrokenPilot prototype planning notes when present
- added `PUBLISHED_COURSE_VIEW.md`
- added `instructor/release-readiness/` as the archive for maintainer-only material

Still pending for final cleanup:

- remove or archive temporary `apply_*`, `repair_*`, and package-specific `check_*` scripts after all content is stable
- decide whether package-level `release-notes/` should stay, move to `instructor/release-readiness/`, or collapse into the changelog
- finish MkDocs navigation and strict build
- stabilize GitHub workflows
- perform final prose cleanup for repeated/generated-looking phrasing
"""
    write_if_changed(path, existing.rstrip() + addition)


def update_legacy_lab_readmes() -> None:
    updates = {
        ROOT / "labs" / "agent-labs" / "README.md": """
# Agent labs

BrokenPilot is the primary runnable path for agent and tool-security labs.

Use these notes only as optional tabletop prompts or instructor discussion material. The assessed path should use:

- `labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md`
- `labs/brokenpilot/prototype-app/MEMORY_POISONING_LAB.md`
- `modules/07-agent-tool-security/lab-path.md`
""",
        ROOT / "labs" / "rag-labs" / "README.md": """
# RAG labs

BrokenPilot is the primary runnable path for RAG authorization and indirect prompt-injection labs.

Use this folder only for optional reasoning prompts. The assessed path should use:

- `labs/brokenpilot/prototype-app/LAB_GUIDE.md`
- `modules/06-rag-security/lab-path.md`
""",
        ROOT / "labs" / "dvaia-guides" / "README.md": """
# DVAIA guides

DVAIA is optional appendix material. It is useful for extra practice, but it is not the primary assessed path for the 40-hour course.

The primary runnable path is course-owned BrokenPilot:

- `labs/brokenpilot/prototype-app/`
- `labs/brokenpilot/STANDALONE_CORE_LAB_PATH.md`

Keep DVAIA references as supplementary only so the course does not depend on an external project during delivery.
""",
    }
    for path, text in updates.items():
        if path.parent.exists():
            write_if_changed(path, text)


def main() -> None:
    ensure_dirs()
    write_release_readiness_index()
    archive_root_pre_release_docs()
    archive_lab_readiness_docs()
    archive_brokenpilot_plan_docs()
    write_published_course_view()
    update_cleanup_before_release()
    update_legacy_lab_readmes()
    print("\nApplied release cleanup phase 2.")


if __name__ == "__main__":
    main()
