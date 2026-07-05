# Final Release Review

Use this checklist after all automated gates are green and before tagging the release candidate.

## Repository state

- `git status` is clean except for intentional final packaging changes.
- No root-level package README remains.
- Temporary apply, repair, add, and fix scripts are archived out of the active `scripts/` directory.
- Release-process documents live under `instructor/release-readiness/`.

## Student-facing course path

Open the generated site locally and check:

- Start page explains what the course is and who it is for.
- Module sequence is clear.
- Lab index routes students to BrokenPilot, toy classifier, and MLOps evidence pack.
- DVAIA is optional wherever it appears.
- BrokenPilot is the primary runnable path for Modules 05, 06, 07, 09, 11, and 12.
- Module 12 reads as a capstone, not as another lecture module.

## Instructor track

Open `instructor/README.md` and confirm:

- A new instructor has a reading order.
- Module-level instructor notes are easy to find.
- Toy classifier uses `instructor/toy-classifier-guide.md`.
- BrokenPilot uses `instructor/brokenpilot-guide.md`.
- MLOps evidence pack uses `instructor/mlops-evidence-pack-guide.md`.
- Release-readiness and course-building files are not mixed into the teaching root.

## Labs

Confirm from a clean checkout or clean virtual environment when possible:

- BrokenPilot tests pass.
- Toy classifier tests pass.
- BrokenPilot lab guide still matches app behavior.
- Toy classifier evasion shows an intent-preserving decision flip.
- MLOps evidence-pack lab is clearly a reasoning lab, not a runnable pipeline.

## Licensing and usage

Confirm these are visible from the repository:

- `LICENSE`
- `LICENSE-CODE`
- `USAGE_AND_LICENSING_GUIDE.md`
- `COURSE_RELEASE_MANIFEST.md`

Confirm the wording is clear:

- Free for self-study and internal company learning with attribution.
- Not sold, repackaged, hosted as a commercial platform, or delivered as paid training without permission.
- Content and code have distinct licenses.
- The project is not described as OSI open source.

## Release decision

Tag `v1.1-dev-rc1` when:

- final release gate passes
- MkDocs strict build passes
- lab tests pass
- instructor spine is readable
- no obvious package-era wording remains in student-facing pages
- no known release blocker remains
