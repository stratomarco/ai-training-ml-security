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

## Final release gate

Run before tagging:

```powershell
python scripts\run_final_release_gate.py
```

The final gate runs repository checks, instructor-track checks, final packaging checks, MkDocs strict build, and both runnable lab test suites.
