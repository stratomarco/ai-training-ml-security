# v1 Release Fixes

This final release pass addresses organization and alignment issues found during release-candidate review.

## Fixed

- Removed duplicate wording in the Module 06 row of the 40-hour delivery plan.
- Repointed the Module 08 MLOps model-answer page to the consolidated instructor guide.
- Moved release-process reports, checklists, baselines, and polish reports out of the repository root into `instructor/release-readiness/release-process-docs/`.
- Added `scripts/check_root_process_docs.py` so report-style and checklist-style files do not return to the repository root.
- Updated release validators to use the new release-process document location.
- Removed workflow references to the archived phase-7 MkDocs checker.
- Updated the final release gate to regenerate MkDocs source and navigation before the strict build.
