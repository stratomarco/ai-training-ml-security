# Final voice and cohesion pass package

This package adds the last content-quality pass before release cleanup.

It does not change MkDocs strict mode, GitHub workflows, or cleanup scripts. It creates the course-level voice, storyline, handoff, and debrief material needed to make the final cleanup deliberate.

## Apply

```powershell
cd C:\Dev\ai-training-ml-security
python scripts\apply_final_voice_cohesion_pass.py
python scripts\check_final_voice_cohesion_pass.py
```

## Commit

```powershell
git status
git add .
git commit -m "Add final voice and cohesion pass"
git push
```
