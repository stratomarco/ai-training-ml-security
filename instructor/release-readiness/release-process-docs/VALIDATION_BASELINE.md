
# Validation Baseline for v1.1-dev

This branch is still in course buildout and cleanup. The validation baseline protects the parts of the course that are stable enough to gate every push.

## Active gates

Run these before committing substantial changes:

```powershell
python scripts/check_repo_structure.py
python scripts/check_content_readiness.py
python scripts/check_lab_targets.py
```

BrokenPilot:

```powershell
cd labs\brokenpilot\prototype-app
pytest
```

Toy classifier:

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
pytest
```

## MkDocs status

MkDocs is currently a smoke test only:

```powershell
python scripts\sync_mkdocs_content.py
mkdocs build
```

Do not use `mkdocs build --strict` as a required gate until the final navigation cleanup is complete.

## Postponed gates

These return in the final release-hardening phase:

- strict MkDocs navigation
- orphan-page failure
- final CI release checklist
- final public-site deploy automation
- cleanup verification for archived package-era scripts

## Why this baseline exists

Earlier workflows used release-grade MkDocs checks while content and lab routing were still moving. That created false failures and made useful development harder. This baseline protects runnable labs and core course readiness without blocking on website polish.
