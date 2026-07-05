# v1.1-dev release cleanup phase 5: voice and content polish toolkit

This package adds a conservative human-editing toolkit for the course. It does not automatically rewrite course prose. Its purpose is to make the final human pass easier and safer.

## What it adds

- A final voice polish guide.
- A student-facing style hotspot reporter.
- A release polish checklist.
- A checker that verifies the toolkit is present.

## What it intentionally does not do

- It does not change module prose automatically.
- It does not touch MkDocs strict mode.
- It does not delete archived material.
- It does not change lab behavior.

## Apply

```powershell
cd C:\Dev\ai-training-ml-security
python scripts\apply_release_cleanup_phase5.py
python scripts\check_release_cleanup_phase5.py
python scripts\report_voice_polish_hotspots.py
```
