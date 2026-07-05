# v1.1-dev final packaging pass

This package performs the last repository hygiene pass before tagging the release candidate.

It does not change lab behavior, module content, or MkDocs navigation.

It adds durable final-release checks, archives package-era helper scripts from the active `scripts/` directory, and writes final review/tagging documents.

## Apply

From the repository root:

```powershell
python scripts\prepare_final_release_artifacts.py
python scripts\check_final_release_artifacts.py
python scripts\check_instructor_track.py
python scripts\run_final_release_gate.py
```

Then inspect the site locally and tag the RC if the review is clean.

## Intended active validation scripts after this pass

- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/check_workflow_validation_baseline.py`
- `scripts/check_release_candidate_phase8.py`
- `scripts/check_student_facing_scaffolding.py`
- `scripts/check_instructor_track.py`
- `scripts/check_final_release_artifacts.py`
- `scripts/generate_mkdocs_nav.py`
- `scripts/sync_mkdocs_content.py`
- `scripts/run_final_release_gate.py`
