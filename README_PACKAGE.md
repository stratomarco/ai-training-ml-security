# RC instructor-track alignment package

Apply from the repository root:

```powershell
python scripts\apply_rc_instructor_track_fixes.py
python scripts\check_rc_instructor_track_fixes.py
```

Then run the release gates:

```powershell
python scripts\check_repo_structure.py
python scripts\check_content_readiness.py
python scripts\check_lab_targets.py
python scripts\check_workflow_validation_baseline.py
python scripts\check_release_candidate_phase8.py
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

Commit suggestion:

```powershell
git add .
git commit -m "Align instructor track for release candidate"
```
