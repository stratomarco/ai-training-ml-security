# v1.1-dev release cleanup phase 2 package

Purpose: clean the student-facing tree without deleting useful project history.

This package moves pre-release audit/build-time scaffolding into an instructor/release-readiness archive, keeps the actual course content and labs in place, and adds a published-course view policy for the final release pass.

It intentionally does not:

- run or fix MkDocs strict navigation
- remove all temporary scripts
- rewrite module prose
- delete historical notes permanently
- change lab behavior

Run from the repository root:

```powershell
python scripts\apply_release_cleanup_phase2.py
python scripts\check_release_cleanup_phase2.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
```

Then run the lab tests:

```powershell
cd labs\brokenpilot\prototype-app
pytest

cd ..\..\toy-ml-attacks\toy-classifier-app
pytest
```
