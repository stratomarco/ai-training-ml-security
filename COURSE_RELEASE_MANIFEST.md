# Course Release Manifest

Version: `v1.2.0`

This manifest records the stable teaching-release baseline for the AI Training - ML Security course. See [v1.2.0 release notes](release-notes/v1.2.0.md) for changes and validation limits.

## Release status

The release can be tagged from a clean, reviewed `main` commit after the full gate passes from the repository root:

```powershell
python scripts/run_final_release_gate.py
```

The gate includes the MkDocs strict build, BrokenPilot tests, and toy classifier tests. The labs can also be checked separately:

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

Stable-release quality gates:

- repository structure is coherent
- content readiness passes
- lab targets are present
- workflow validation baseline passes
- MkDocs builds in strict mode
- BrokenPilot tests pass
- toy classifier tests pass

## Known non-blocking note

Material for MkDocs may print an upstream warning banner about a future MkDocs 2.0 direction. That banner is outside this course repository and is not a release blocker. The release gate is whether `mkdocs build --strict` exits successfully.

## What is intentionally out of scope

- A new course restructure.
- A broad automated prose rewrite.
- Reintroducing archived package-era scaffolding into the student path.
- Treating optional external labs as required course dependencies.
- Claiming that every local model follows every planted instruction.
- A formal student grading or exam service.
