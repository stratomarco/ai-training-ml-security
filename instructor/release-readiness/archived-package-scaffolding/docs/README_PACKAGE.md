# Release cleanup phase 4 package

Purpose: conservative final prose and generated-scaffolding cleanup.

This package does not rewrite course prose automatically. It removes or archives temporary package scaffolding, strengthens ignore rules for generated artifacts, adds a student-facing scaffolding check, and creates final voice cleanup guidance for a manual polish pass.

Apply:

```powershell
cd C:\Dev\ai-training-ml-security
python scripts\apply_release_cleanup_phase4.py
python scripts\check_release_cleanup_phase4.py
python scripts\check_student_facing_scaffolding.py
```

Then run the normal validation baseline and lab tests.
