# Course Release Manifest

Version: `v1.1.0-v1.1.0`

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
