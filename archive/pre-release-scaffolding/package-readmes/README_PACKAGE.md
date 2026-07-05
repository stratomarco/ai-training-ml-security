# Release cleanup phase 1 package

This package starts the release-hardening phase without touching MkDocs strict mode or changing course content.

It archives temporary package scaffolding, consolidates package release notes, and adds durable readiness checks for course content and lab targets.

## Apply

```powershell
cd C:\Dev\ai-training-ml-security
python scripts\apply_release_cleanup_phase1.py
python scripts\check_release_cleanup_phase1.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
```

Then run the lab tests:

```powershell
cd C:\Dev\ai-training-ml-security\labs\brokenpilot\prototype-app
pytest

cd C:\Dev\ai-training-ml-security\labs\toy-ml-attacks\toy-classifier-app
pytest
```

No MkDocs strict build yet.
