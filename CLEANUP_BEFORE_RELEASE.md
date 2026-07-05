# Cleanup before release

<!-- module-depth-prose-pass-08-11:start -->

## Module depth prose pass cleanup

Before public release, review the Modules 08 to 11 depth-pass files for voice consistency with the rest of the course. Keep the decision-driven structure, but remove any temporary apply/check scripts after all content packages stop changing.

<!-- module-depth-prose-pass-08-11:end -->

## Module depth prose pass 01 to 04 cleanup note

Before release, review the new foundation prose for voice consistency with the rest of the course. Remove temporary apply/check scripts once the content is committed and stable.

## Current BrokenPilot final report temporary scripts

Before release, remove or consolidate temporary apply/check scripts for the current BrokenPilot final report package. Keep the durable content, rubric, template, and worked example.

<!-- toy-classifier-instructor-debrief-cleanup:start -->
## Toy-classifier package cleanup reminder

Before release, keep the durable toy-classifier instructor and debrief docs, but remove temporary apply/check scripts after their changes are committed. Re-enable strict MkDocs and broader release gates only after content and lab paths stop moving.
<!-- toy-classifier-instructor-debrief-cleanup:end -->

## Cleanup reminder: MLOps model answer package

Before final release, review the MLOps model answer files for tone consistency with the rest of the course, and decide whether temporary apply/check scripts should be removed or converted into durable validation checks.

## Final content audit reminder

Before cleanup, run the final content audit and 40-hour dry-run review. Do not start repository cleanup until the content path is stable enough that only navigation, CI, stale scripts, naming, and generated-looking phrasing remain.

<!-- final-voice-cohesion-cleanup-reminder -->

## Final voice and cohesion cleanup reminder

Before release, use COURSE_VOICE_AND_COHESION_REVIEW.md and instructor/final-voice-cohesion-review-guide.md to remove temporary scaffolding, reduce repeated generated-looking phrasing, and make the course read like a hand-curated professional training.

## Round 3 cleanup reminders

Before release, verify that legacy DVAIA, RAG, and agent paper labs are either clearly optional or removed from student navigation. Keep BrokenPilot as the primary path for those modules. Also verify that archived BrokenPilot prototype planning notes are not presented as current student instructions.

## Release cleanup phase 1 completed

Temporary package scaffolding has been archived under `archive/pre-release-scaffolding/` instead of being left in the active course tree.

Archived scripts: 43
Archived package release notes: 19

Keep active during the remaining release work:

- `scripts/check_repo_structure.py`
- `scripts/check_content_readiness.py`
- `scripts/check_lab_targets.py`
- `scripts/sync_mkdocs_content.py`

Still pending for final release cleanup:

- remove or delete `archive/pre-release-scaffolding/` once the release branch is stable;
- finish MkDocs navigation and re-enable strict site build;
- stabilize GitHub workflows for final release;
- run a voice pass on module README files if review finds generated-looking phrasing;
- remove generated `site/`, `.mkdocs-src/`, caches, and local virtual environments.

## Release cleanup phase 2 status

Completed during the student-facing tree cleanup pass:

- moved pre-release audit documents out of the repository root when present
- moved final lab readiness review material out of the student-facing `labs/` path when present
- archived superseded BrokenPilot prototype planning notes when present
- added `PUBLISHED_COURSE_VIEW.md`
- added `instructor/release-readiness/` as the archive for maintainer-only material

Still pending for final cleanup:

- remove or archive temporary `apply_*`, `repair_*`, and package-specific `check_*` scripts after all content is stable
- decide whether package-level `release-notes/` should stay, move to `instructor/release-readiness/`, or collapse into the changelog
- finish MkDocs navigation and strict build
- stabilize GitHub workflows
- perform final prose cleanup for repeated/generated-looking phrasing

## Release cleanup phase 3 status

Workflow and validation cleanup has started.

Current development gates:

- repository structure check
- content readiness check
- lab target presence check
- BrokenPilot pytest
- toy-classifier pytest
- non-strict MkDocs smoke build

Postponed until final release hardening:

- MkDocs strict navigation
- orphan-page failure
- public deploy automation on every push
- deletion of archived buildout material
- final generated-phrasing cleanup

## Release cleanup phase 4

- Archived package-era scaffolding and temporary scripts.
- Added final voice cleanup guidance.
- Added student-facing scaffolding check.
- Kept MkDocs strict cleanup postponed until navigation is intentionally finalized.

## Release cleanup phase 5

Status: voice and content polish toolkit added.

Before the release candidate, run:

```powershell
python scripts/report_voice_polish_hotspots.py
python scripts/check_release_cleanup_phase5.py
```

Use the hotspot report as a manual editing aid, not as a hard failure gate.

## Phase 6 manual voice polish

Status: started.

- Package-era lines are removed from student-facing Markdown.
- Final voice guidance is recorded in `STYLE_AND_VOICE_FINAL_PASS.md`.
- Broad automatic prose rewrites are intentionally avoided.
- Remaining release work: MkDocs strict navigation, final workflow hardening, and release candidate validation.

## Release cleanup phase 7

MkDocs strict navigation was regenerated from the actual published source tree.

Expected release behavior:

- `scripts/sync_mkdocs_content.py` creates `.mkdocs-src`.
- `scripts/generate_mkdocs_nav.py` regenerates `mkdocs.yml` navigation from files that exist.
- `mkdocs build --strict` is the release gate.
- CI runs the two runnable lab targets before publishing.

## Release cleanup phase 8

Release-candidate hardening added:

- `VERSION`
- `COURSE_RELEASE_MANIFEST.md`
- `RELEASE_CANDIDATE_CHECKLIST.md`
- `USAGE_AND_LICENSING_GUIDE.md`
- `QUALITY_GATE_BASELINE.md`
- `scripts/check_release_candidate_phase8.py`

The repository is now ready for final release-candidate validation and tagging once all quality gates pass.
