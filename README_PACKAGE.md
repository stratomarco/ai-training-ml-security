# Release cleanup phase 8 - release-candidate hardening

This package adds the final release-candidate hardening layer after MkDocs strict mode and the lab gates are green.

It does not rewrite course content and does not change lab behavior.

## Adds

- `VERSION`
- `COURSE_RELEASE_MANIFEST.md`
- `RELEASE_CANDIDATE_CHECKLIST.md`
- `USAGE_AND_LICENSING_GUIDE.md`
- `QUALITY_GATE_BASELINE.md`
- `scripts/check_release_candidate_phase8.py`
- `release-notes/v1.1-dev-release-candidate.md`

It also updates `CHANGELOG.md` and appends phase 8 status to `CLEANUP_BEFORE_RELEASE.md` when that file exists.

## Apply

From the repository root:

```powershell
python scripts\apply_release_cleanup_phase8.py
python scripts\check_release_cleanup_phase8.py
python scripts\check_release_candidate_phase8.py
```

Then run the final baseline:

```powershell
python scripts\check_repo_structure.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
python scripts\check_workflow_validation_baseline.py
mkdocs build --strict
```

Run lab tests:

```powershell
cd labs\brokenpilot\prototype-app
pytest
```

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
pytest
```

## Commit and tag

```powershell
cd C:\Dev\ai-training-ml-security
git status
git add .
git commit -m "Prepare v1.1 dev release candidate"
git tag v1.1-dev-rc1
git push
git push origin v1.1-dev-rc1
```
