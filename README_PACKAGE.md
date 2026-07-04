# Round 3 Content Quality Fixes Package

Apply from the repository root:

```powershell
python scripts\apply_round3_content_quality_fixes.py
python scripts\check_round3_content_quality_fixes.py
```

Then validate the runnable labs:

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
pytest

cd ..\..\brokenpilot\prototype-app
pytest
```

Expected effect:

- toy classifier evasion now preserves malicious intent
- legacy RAG, agent, and DVAIA folders are clearly non-primary
- Module 05 output handling is student-facing
- Modules 01 and 02 have explicit graded artifacts
- superseded BrokenPilot planning docs are archived when present

Do not run MkDocs strict as part of this package. That remains a release-hardening task.
