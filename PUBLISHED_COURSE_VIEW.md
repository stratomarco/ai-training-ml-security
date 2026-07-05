
# Published course view

This file defines what should feel student-facing in the final v1.1 release.

## Student-facing by default

- `README.md`
- `syllabus.md`
- `course-map.md`
- `modules/`
- `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md`
- `labs/STUDENT_LAB_JOURNAL_GUIDE.md`
- runnable lab folders under `labs/`
- `course-templates/`
- `assessments/` that students use to understand grading expectations

## Instructor-facing by default

- `instructor/`
- grading calibration notes
- strong and weak answer anchors
- debrief guides
- release-readiness notes

## Maintainer-only or release-readiness material

- temporary course updates
- package-specific check scripts
- package release notes
- pre-release audit documents
- build-time prototype plans superseded by runnable labs

## Cleanup rule

If a document describes how the course was built, reviewed, packaged, or repaired, it does not belong in the student path. Move it to `instructor/release-readiness/` or delete it during final cleanup.

If a document helps a student understand a concept, perform a lab, complete a deliverable, or interpret feedback, keep it in the course path.
