# Final Cleanup Backlog

Do not work this list until the course content and labs are stable.

## Repository cleanup

- Remove temporary apply scripts that were only used to patch development packages.
- Keep durable check scripts that protect important claims, such as runnable lab tests and repository structure checks.
- Remove generated folders from version control if they are present, especially `.mkdocs-src/`, `site/`, caches, virtual environments, and model artifacts generated during toy-classifier runs.
- Review release notes and development notes for duplication.

## Editorial cleanup

- Normalize voice across modules so the material reads like a coherent instructor-authored course.
- Replace repetitive phrasing and generic summary language.
- Keep the style direct, concrete, and engineering-focused.
- Avoid over-polished generated phrasing, but do not remove useful precision.
- Keep attribution and licensing accurate.

## Website cleanup

- Finish MkDocs navigation only after content stops moving.
- Decide which support files belong in navigation and which should be intentionally excluded.
- Then switch to strict build and CI gates.

## Lab cleanup

- Ensure every runnable lab has deterministic tests.
- Ensure every reasoning lab has strong and weak anchors.
- Ensure every graded artifact has a rubric.
- Ensure no lab references data or scripts that are not shipped.
