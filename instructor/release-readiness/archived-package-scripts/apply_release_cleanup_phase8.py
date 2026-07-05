from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.1-dev-rc1"


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {path}")


def append_changelog_section() -> None:
    path = ROOT / "CHANGELOG.md"
    section = f"""## {VERSION} - release candidate

This release-candidate checkpoint marks the course as ready for final review after the release cleanup sequence.

Validation baseline:

- Repository structure check.
- Content readiness check.
- Lab target presence check.
- MkDocs strict build.
- BrokenPilot pytest suite.
- Toy classifier pytest suite.

Course status:

- BrokenPilot is the primary runnable capstone environment.
- The toy classifier lab is the primary classical ML attack environment.
- The MLOps evidence-pack lab is the primary secure MLOps reasoning lab.
- Optional legacy or external lab paths are marked as optional and are not required for the published course path.

Known non-blocking item:

- Material for MkDocs may print an upstream MkDocs 2.0 warning banner. That banner is informational and is not a course release blocker.
"""
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if f"## {VERSION}" in text:
            print("CHANGELOG.md already contains release-candidate section")
            return
        if text.startswith("# Changelog"):
            text = text.replace("# Changelog\n", "# Changelog\n\n" + section.strip() + "\n\n", 1)
        else:
            text = text.rstrip() + "\n\n" + section.strip() + "\n"
    else:
        text = "# Changelog\n\n" + section.strip() + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    print("updated CHANGELOG.md")


def main() -> None:
    write("VERSION", VERSION)

    write(
        "COURSE_RELEASE_MANIFEST.md",
        f"""
# Course Release Manifest

Version: `{VERSION}`

This manifest records the release-candidate baseline for the AI Training - ML Security course.

## Release status

This branch is ready for final release-candidate review when the following commands pass from the repository root:

```powershell
python scripts/check_repo_structure.py
python scripts/check_content_readiness.py
python scripts/check_lab_targets.py
python scripts/check_workflow_validation_baseline.py
python scripts/check_release_candidate_phase8.py
mkdocs build --strict
```

The runnable lab tests must also pass:

```powershell
cd labs/brokenpilot/prototype-app
pytest
```

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
pytest
```

## Supported student path

The published course view is defined in `PUBLISHED_COURSE_VIEW.md`.

The supported hands-on targets are:

- `labs/brokenpilot/prototype-app/`
- `labs/toy-ml-attacks/toy-classifier-app/`
- `labs/mlops-supply-chain-labs/evidence-pack-review/`

BrokenPilot is the primary capstone path. Optional or historical lab folders are retained only when they provide useful context and are not required for the release-candidate student path.

## Validation baseline

Release-candidate quality gates:

- repository structure is coherent
- content readiness passes
- lab targets are present
- workflow validation baseline passes
- MkDocs builds in strict mode
- BrokenPilot tests pass
- toy classifier tests pass

## Known non-blocking note

Material for MkDocs may print an upstream warning banner about a future MkDocs 2.0 direction. That banner is outside this course repository and is not a release blocker. The release gate is whether `mkdocs build --strict` exits successfully.

## What is intentionally out of scope for this RC

- A new course restructure.
- A broad automated prose rewrite.
- Reintroducing archived package-era scaffolding into the student path.
- Treating optional external labs as required course dependencies.
""",
    )

    write(
        "RELEASE_CANDIDATE_CHECKLIST.md",
        """
# Release Candidate Checklist

Use this checklist before tagging a release candidate.

## 1. Repository state

```powershell
git status
git log --oneline -5
```

Expected:

- working tree is clean or contains only intended release-candidate changes
- latest commits are on the release branch

## 2. Static checks

```powershell
python scripts/check_repo_structure.py
python scripts/check_content_readiness.py
python scripts/check_lab_targets.py
python scripts/check_workflow_validation_baseline.py
python scripts/check_release_candidate_phase8.py
```

Expected:

- all checks pass
- content readiness may print non-blocking notes about archived audit/buildout docs

## 3. Documentation build

```powershell
mkdocs build --strict
```

Expected:

- documentation builds successfully
- no unresolved links
- no missing navigation pages
- the upstream Material for MkDocs warning banner is not a release blocker if the build exits successfully

## 4. Runnable labs

```powershell
cd labs/brokenpilot/prototype-app
pytest
```

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
pytest
```

Expected:

- BrokenPilot tests pass
- toy classifier tests pass

## 5. Student-facing sanity check

Open the generated site locally and check:

- start-here path
- module sequence
- BrokenPilot lab path
- toy classifier lab path
- MLOps evidence-pack lab path
- capstone report path
- license and usage guidance

## 6. Tagging recommendation

When all checks pass:

```powershell
git status
git add .
git commit -m "Prepare v1.1 dev release candidate"
git tag v1.1-dev-rc1
git push
git push origin v1.1-dev-rc1
```
""",
    )

    write(
        "USAGE_AND_LICENSING_GUIDE.md",
        """
# Usage and Licensing Guide

This repository is intended to be free for self-study and internal organizational learning with attribution.

The intended licensing model is:

- course content, slides, templates, handouts, rubrics, and written training material: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
- original runnable lab code and supporting scripts: PolyForm Noncommercial 1.0.0

This project should not be described as OSI open source. It is source-available training material for non-commercial learning.

## Allowed without separate commercial permission

- individual self-study
- internal company learning
- internal security team practice
- academic discussion with attribution
- adapting the material internally when it is not resold, repackaged, or delivered as a paid external offering

## Requires commercial permission

- selling the course or a modified version of it
- using the material as paid external training
- packaging it into a commercial platform
- reselling the labs, slides, rubrics, or course path
- using the material as the substantial basis for a paid consulting product

## Attribution

Attribution should include the course title, repository name, and the original author or organization named in the repository metadata.

## Third-party material

External frameworks, standards, papers, projects, and tools referenced by the course keep their own licenses and terms. This guide does not change third-party licensing.
""",
    )

    write(
        "QUALITY_GATE_BASELINE.md",
        """
# Quality Gate Baseline

This file summarizes the release-candidate quality gates.

## Required commands

```powershell
python scripts/check_repo_structure.py
python scripts/check_content_readiness.py
python scripts/check_lab_targets.py
python scripts/check_workflow_validation_baseline.py
python scripts/check_release_candidate_phase8.py
mkdocs build --strict
```

## Required lab tests

```powershell
cd labs/brokenpilot/prototype-app
pytest
```

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
pytest
```

## Durable checks

The durable checks are:

- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/check_workflow_validation_baseline.py`
- `scripts/check_release_candidate_phase8.py`

Package-era apply, repair, and temporary check scripts should remain archived or absent from the student-facing path.
""",
    )

    write(
        "release-notes/v1.1-dev-release-candidate.md",
        """
# v1.1-dev Release Candidate Notes

This release-candidate checkpoint follows the release cleanup sequence:

1. cleanup of temporary package scaffolding
2. student-facing tree cleanup
3. workflow validation baseline
4. generated-scaffolding cleanup
5. voice-polish toolkit
6. manual voice polish
7. MkDocs strict/navigation cleanup
8. release-candidate hardening

## Main course path

- BrokenPilot is the primary runnable capstone.
- Toy classifier is the classical ML attack lab.
- MLOps evidence-pack review is the secure MLOps reasoning lab.
- Reasoning labs remain available where a runnable lab would create fake realism.

## Release gates

The release candidate requires:

- strict MkDocs build
- BrokenPilot tests
- toy classifier tests
- durable repository/content/lab/workflow checks

## Non-blocking notes

The Material for MkDocs upstream warning banner is informational if the strict build exits successfully.

Buildout and audit files that were moved out of the student path are non-blocking unless they are linked from published pages.
""",
    )

    write(
        "scripts/check_release_candidate_phase8.py",
        '''
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "VERSION",
    "COURSE_RELEASE_MANIFEST.md",
    "RELEASE_CANDIDATE_CHECKLIST.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    "QUALITY_GATE_BASELINE.md",
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
    "QUALITY_GATE_BASELINE.md": [
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
    ]

    for rel in durable_checks:
        if (ROOT / rel).exists():
            run([sys.executable, rel])

    print("release candidate phase 8 check passed.")


if __name__ == "__main__":
    main()
''',
    )

    append_changelog_section()

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists():
        text = cleanup.read_text(encoding="utf-8")
        marker = "## Release cleanup phase 8"
        if marker not in text:
            text = text.rstrip() + """

## Release cleanup phase 8

Release-candidate hardening added:

- `VERSION`
- `COURSE_RELEASE_MANIFEST.md`
- `RELEASE_CANDIDATE_CHECKLIST.md`
- `USAGE_AND_LICENSING_GUIDE.md`
- `QUALITY_GATE_BASELINE.md`
- `scripts/check_release_candidate_phase8.py`

The repository is now ready for final release-candidate validation and tagging once all quality gates pass.
"""
            cleanup.write_text(text, encoding="utf-8", newline="\n")
            print("updated CLEANUP_BEFORE_RELEASE.md")

    print("release candidate phase 8 applied")


if __name__ == "__main__":
    main()
