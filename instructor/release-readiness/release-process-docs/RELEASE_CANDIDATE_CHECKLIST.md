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
