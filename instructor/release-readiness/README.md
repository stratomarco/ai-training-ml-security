
# Release readiness archive

This directory holds pre-release review material, package worklogs, and build-time notes that are useful for maintainers but should not be part of the normal student path.

Student-facing course material should remain in:

- `modules/`
- `labs/`
- `course-templates/`
- `assessments/`
- selected `docs/start-here/` pages

Before a public release, review this directory and decide what to keep as instructor-only history, what to fold into durable course material, and what to delete.

## Build input updates

The active documentation and BrokenPilot requirements pin direct package versions. The workflows pin their action commits, and the BrokenPilot Dockerfile pins the multi-platform Python base-image digest. These are deliberate update points; check upstream security releases, update the pins, run the course quality workflow, and rebuild the container before a new release. Transitive Python packages and the downloaded Qwen model are not hash-locked, so this is improved repeatability rather than a fully reproducible or attested build.
