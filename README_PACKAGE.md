# Release cleanup phase 7: MkDocs strict and navigation cleanup

This package prepares the release-candidate website build.

It does not change course content or lab behavior.

## What it does

- Rewrites the MkDocs source sync script.
- Adds a nav generator that scans `.mkdocs-src` and builds `mkdocs.yml` from files that exist.
- Declares intentional non-nav pages using `not_in_nav`.
- Re-enables `mkdocs build --strict`.
- Updates CI so BrokenPilot and toy-classifier tests remain quality gates.

## Apply

```powershell
cd C:\Dev\ai-training-ml-security

python scripts\apply_release_cleanup_phase7_mkdocs_strict.py
python scripts\check_release_cleanup_phase7_mkdocs_strict.py
```

## Validate labs

```powershell
cd C:\Dev\ai-training-ml-security\labs\brokenpilot\prototype-app
pytest

cd C:\Dev\ai-training-ml-security\labs\toy-ml-attacks\toy-classifier-app
pytest
```

## Commit

```powershell
cd C:\Dev\ai-training-ml-security
git status
git add .
git commit -m "Prepare MkDocs strict navigation for release"
git push
```
