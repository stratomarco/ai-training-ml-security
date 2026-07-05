# Release Tagging Guide

This guide assumes the final release gate is green.

## Final validation

```powershell
python scripts\run_final_release_gate.py
```

Optional explicit commands:

```powershell
python scripts\check_repo_structure.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
python scripts\check_workflow_validation_baseline.py
python scripts\check_release_candidate_phase8.py
python scripts\check_instructor_track.py
python scripts\check_final_release_artifacts.py
mkdocs build --strict
```

```powershell
cd labs\brokenpilot\prototype-app
pytest
```

```powershell
cd ..\..\toy-ml-attacks\toy-classifier-app
pytest
```

## Commit

```powershell
cd C:\Dev\ai-training-ml-security
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
