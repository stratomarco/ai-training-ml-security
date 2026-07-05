# v1 Release Fixes Package

This package applies the final v1 organization and alignment fixes:

- Fixes the duplicated Module 06 row in `instructor/40-hour-delivery-plan.md`.
- Repoints the Module 08 MLOps model-answer path to the consolidated instructor guide.
- Moves root-level release-process reports, checklists, baselines, and polish reports to `instructor/release-readiness/release-process-docs/`.
- Adds a root process-document guard: `scripts/check_root_process_docs.py`.
- Updates release validation scripts to use the new process-document location.
- Removes workflow references to the archived phase-7 MkDocs checker.
- Regenerates MkDocs source/nav after applying.

## Apply

From the repository root:

```powershell
python .\apply_v1_release_fixes.py
python .\check_v1_release_fixes.py
```

Then run the final release gate:

```powershell
python scripts\run_final_release_gate.py
mkdocs build --strict
```

Before committing, remove the two temporary package scripts from the root. The package README is archived automatically by the apply script.

```powershell
Remove-Item .\apply_v1_release_fixes.py
Remove-Item .\check_v1_release_fixes.py
```

Then rerun:

```powershell
python scripts\check_final_release_artifacts.py
python scripts\run_final_release_gate.py
```
