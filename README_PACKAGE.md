# Toy Classifier Instructor Debrief Package

This package adds instructor and assessment material for the toy-classifier lab, plus development-mode workflow changes that keep runnable lab tests in CI while postponing strict MkDocs until content is frozen.

Apply from the repository root:

```powershell
python scripts\apply_toy_classifier_instructor_debrief.py
python scripts\check_toy_classifier_instructor_debrief.py
```

Then run the toy classifier tests:

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
pytest
```

Commit:

```powershell
git add .
git commit -m "Add toy classifier instructor debrief and dev workflows"
git push
```
