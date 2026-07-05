from __future__ import annotations

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-package-scripts"
DOC_ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-package-docs"

ACTIVE_SCRIPTS = {
    "check_repo_structure.py",
    "check_content_readiness.py",
    "check_lab_targets.py",
    "check_workflow_validation_baseline.py",
    "check_release_candidate_phase8.py",
    "check_student_facing_scaffolding.py",
    "check_instructor_track.py",
    "check_final_release_artifacts.py",
    "generate_mkdocs_nav.py",
    "sync_mkdocs_content.py",
    "run_final_release_gate.py",
    "prepare_final_release_artifacts.py",
}

PACKAGE_SCRIPT_PREFIXES = (
    "apply_",
    "repair_",
    "add_",
    "fix_",
)

PACKAGE_SCRIPT_NAMES = {
    "check_release_cleanup_phase1.py",
    "check_release_cleanup_phase2.py",
    "check_release_cleanup_phase3.py",
    "check_release_cleanup_phase4.py",
    "check_release_cleanup_phase5.py",
    "check_release_cleanup_phase6_manual_voice_polish.py",
    "check_release_cleanup_phase7_mkdocs_strict.py",
    "check_release_cleanup_phase8.py",
    "check_rc_instructor_track_fixes.py",
    "check_pre_rc_review_package.py",
    "run_pre_rc_review.py",
    "apply_pre_rc_review.py",
    "report_voice_polish_hotspots.py",
}


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def append_once(path: str, marker: str, block: str) -> None:
    target = ROOT / path
    if not target.exists():
        target.write_text(block.strip() + "\n", encoding="utf-8", newline="\n")
        return

    text = target.read_text(encoding="utf-8")
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
        target.write_text(text, encoding="utf-8", newline="\n")


def archive_file(path: Path, archive_root: Path) -> None:
    archive_root.mkdir(parents=True, exist_ok=True)
    destination = archive_root / path.name

    if destination.exists():
        stem = destination.stem
        suffix = destination.suffix
        counter = 2
        while True:
            candidate = archive_root / f"{stem}-{counter}{suffix}"
            if not candidate.exists():
                destination = candidate
                break
            counter += 1

    shutil.move(str(path), str(destination))


def archive_package_scripts() -> None:
    if not SCRIPTS.exists():
        return

    for path in sorted(SCRIPTS.glob("*.py")):
        name = path.name
        if name in ACTIVE_SCRIPTS:
            continue

        package_like = (
            name.startswith(PACKAGE_SCRIPT_PREFIXES)
            or name.startswith("check_release_cleanup_phase")
            or name in PACKAGE_SCRIPT_NAMES
        )

        if package_like:
            archive_file(path, ARCHIVE)


def archive_package_readmes() -> None:
    for rel in ["README_PACKAGE.md"]:
        path = ROOT / rel
        if path.exists():
            archive_file(path, DOC_ARCHIVE)


def update_readme() -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        return

    text = readme.read_text(encoding="utf-8")
    marker = "## Release and usage"
    if marker in text:
        return

    block = """
## Release and usage

For release scope, quality gates, and licensing, see:

- [`COURSE_RELEASE_MANIFEST.md`](COURSE_RELEASE_MANIFEST.md)
- [`QUALITY_GATE_BASELINE.md`](QUALITY_GATE_BASELINE.md)
- [`USAGE_AND_LICENSING_GUIDE.md`](USAGE_AND_LICENSING_GUIDE.md)
- [`RELEASE_TAGGING_GUIDE.md`](RELEASE_TAGGING_GUIDE.md)

The course is free for self-study and internal company learning with attribution. Commercial training, resale, hosted-course use, or repackaging requires separate permission.
"""
    readme.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    write("FINAL_RELEASE_REVIEW.md", """# Final Release Review

Use this checklist after all automated gates are green and before tagging the release candidate.

## Repository state

- `git status` is clean except for intentional final packaging changes.
- No root-level package README remains.
- Temporary apply, repair, add, and fix scripts are archived out of the active `scripts/` directory.
- Release-process documents live under `instructor/release-readiness/`.

## Student-facing course path

Open the generated site locally and check:

- Start page explains what the course is and who it is for.
- Module sequence is clear.
- Lab index routes students to BrokenPilot, toy classifier, and MLOps evidence pack.
- DVAIA is optional wherever it appears.
- BrokenPilot is the primary runnable path for Modules 05, 06, 07, 09, 11, and 12.
- Module 12 reads as a capstone, not as another lecture module.

## Instructor track

Open `instructor/README.md` and confirm:

- A new instructor has a reading order.
- Module-level instructor notes are easy to find.
- Toy classifier uses `instructor/toy-classifier-guide.md`.
- BrokenPilot uses `instructor/brokenpilot-guide.md`.
- MLOps evidence pack uses `instructor/mlops-evidence-pack-guide.md`.
- Release-readiness and course-building files are not mixed into the teaching root.

## Labs

Confirm from a clean checkout or clean virtual environment when possible:

- BrokenPilot tests pass.
- Toy classifier tests pass.
- BrokenPilot lab guide still matches app behavior.
- Toy classifier evasion shows an intent-preserving decision flip.
- MLOps evidence-pack lab is clearly a reasoning lab, not a runnable pipeline.

## Licensing and usage

Confirm these are visible from the repository:

- `LICENSE`
- `LICENSE-CODE`
- `USAGE_AND_LICENSING_GUIDE.md`
- `COURSE_RELEASE_MANIFEST.md`

Confirm the wording is clear:

- Free for self-study and internal company learning with attribution.
- Not sold, repackaged, hosted as a commercial platform, or delivered as paid training without permission.
- Content and code have distinct licenses.
- The project is not described as OSI open source.

## Release decision

Tag `v1.1-dev-rc1` when:

- final release gate passes
- MkDocs strict build passes
- lab tests pass
- instructor spine is readable
- no obvious package-era wording remains in student-facing pages
- no known release blocker remains
""")

    write("RELEASE_TAGGING_GUIDE.md", """# Release Tagging Guide

This guide assumes the final release gate is green.

## Final validation

```powershell
python scripts\\run_final_release_gate.py
```

Optional explicit commands:

```powershell
python scripts\\check_repo_structure.py
python scripts\\check_content_readiness.py
python scripts\\check_lab_targets.py
python scripts\\check_workflow_validation_baseline.py
python scripts\\check_release_candidate_phase8.py
python scripts\\check_instructor_track.py
python scripts\\check_final_release_artifacts.py
mkdocs build --strict
```

```powershell
cd labs\\brokenpilot\\prototype-app
pytest
```

```powershell
cd ..\\..\\toy-ml-attacks\\toy-classifier-app
pytest
```

## Commit

```powershell
cd C:\\Dev\\ai-training-ml-security
git status
git add .
git commit -m "Finalize v1.1 dev release candidate"
git push
```

## Tag release candidate

```powershell
git tag v1.1-dev-rc1
git push origin v1.1-dev-rc1
```

## After tagging

Keep `v1.1-dev-rc1` as the review tag until a final human pass confirms there are no release blockers. Promote to a final `v1.1` tag only after that review.
""")

    write("release-notes/v1.1-dev-final-packaging.md", """# v1.1-dev final packaging pass

This pass prepares the repository for release-candidate tagging after instructor-track fixes and MkDocs strict cleanup have passed.

## Added

- `FINAL_RELEASE_REVIEW.md`
- `RELEASE_TAGGING_GUIDE.md`
- `scripts/check_instructor_track.py`
- `scripts/check_final_release_artifacts.py`
- `scripts/run_final_release_gate.py`

## Changed

- Archives package-era helper scripts out of the active `scripts/` directory.
- Keeps durable validation scripts active.
- Updates cleanup and quality baseline documents when present.

## Not changed

- Course prose
- Lab behavior
- MkDocs navigation
- Licensing terms
""")

    update_readme()

    append_once(
        "CLEANUP_BEFORE_RELEASE.md",
        "Final packaging pass",
        """## Final packaging pass

Status: complete when `scripts/run_final_release_gate.py` passes.

This pass archives package-era helper scripts out of the active `scripts/` directory, keeps durable validation scripts active, and adds final release review and tagging guidance.
""",
    )

    append_once(
        "QUALITY_GATE_BASELINE.md",
        "Final release gate",
        """## Final release gate

Run before tagging:

```powershell
python scripts\\run_final_release_gate.py
```

The final gate runs repository checks, instructor-track checks, final packaging checks, MkDocs strict build, and both runnable lab test suites.
""",
    )

    archive_package_scripts()
    archive_package_readmes()

    print("final release artifacts prepared")
    print("archived package-era scripts under instructor/release-readiness/archived-package-scripts when present")
    print("run: python scripts/check_final_release_artifacts.py")
    print("run: python scripts/run_final_release_gate.py")


if __name__ == "__main__":
    main()
