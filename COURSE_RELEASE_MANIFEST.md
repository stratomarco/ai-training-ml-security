# Course Release Manifest

Version: `v1.4.0`

This manifest records the stable teaching-release baseline for the AI Training - ML Security course. See [v1.4.0 release notes](release-notes/v1.4.0.md) for changes and validation limits.

## Release status

The release can be tagged from a clean, reviewed `main` commit after the full gate passes from the repository root:

```powershell
python scripts/run_final_release_gate.py
```

The gate includes the MkDocs strict build, BrokenPilot tests, toy classifier tests, and the offline artifact-promotion tests. The labs can also be checked separately:

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

The optional Module 08 extensions are `labs/brokenpilot/prototype-app/MOCK_HUB_LAB.md` and `labs/mlops-supply-chain-labs/artifact-promotion/artifact-promotion-lab.md`. Both use fake local data. The artifact gate and Mock Hub are separate simulations and do not share state or enforce each other's decisions.

Module 07 also includes an optional AIGoat v2.0 source-review exercise. A contained Windows and Docker Desktop route is available for live traces of two selected MCP exercises. This external extension is not required for the 40-hour path, and AIGoat retains its own license and security boundaries.

BrokenPilot is the primary capstone path. Optional or historical lab folders are retained only when they provide useful context and are not required for the release-candidate student path.

## Validation baseline

Stable-release quality gates:

- repository structure is coherent
- content readiness passes
- lab targets are present
- workflow validation baseline passes
- MkDocs builds in strict mode
- every published page edit link resolves to a repository source file
- BrokenPilot tests pass
- toy classifier tests pass
- artifact-promotion tests pass
- GitHub Pages deployment succeeds and the published student route is reachable

## Known non-blocking note

Material for MkDocs may print an upstream warning banner about a future MkDocs 2.0 direction. That banner is outside this course repository and is not a release blocker. The release gate is whether `mkdocs build --strict` exits successfully.

The optional AIGoat live route has been reproduced on one Windows and Docker Desktop host, including an isolated fresh-state replay. A cold first-time learner install, macOS, native Linux, and exercises outside the selected MCP pair remain unverified. The no-install source review remains available.

## What is intentionally out of scope

- A new course restructure.
- A broad automated prose rewrite.
- Reintroducing archived package-era scaffolding into the student path.
- Treating optional external labs as required course dependencies.
- Claiming that every local model follows every planted instruction.
- A formal student grading or exam service.
