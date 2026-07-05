# Generated Scaffolding Cleanup Report

Release cleanup phase 4 starts the move from buildout mode to release mode.

## What was archived

- Root package readme files from generated patch packages when present.
- Temporary apply, repair, add, and fix scripts from `scripts/` when present.
- Package-specific check scripts from earlier buildout phases when present.

## What stays active

- `scripts/sync_mkdocs_content.py`
- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/check_workflow_validation_baseline.py`
- `scripts/check_student_facing_scaffolding.py`

## What is not done yet

- MkDocs strict navigation cleanup.
- Public deploy workflow hardening.
- Manual prose polish across all modules.
- Permanent deletion of archived buildout history.

Archived material is kept under `instructor/release-readiness/archived-package-scaffolding/` until final release review decides what to delete.
