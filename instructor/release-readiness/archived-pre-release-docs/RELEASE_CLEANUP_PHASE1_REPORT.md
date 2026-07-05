
# Release cleanup phase 1 report

This cleanup pass reduces active development scaffolding without changing course content, labs, or assessments.

## What changed

- Temporary package `apply_*`, `repair_*`, `add_*`, and package-specific `check_*` scripts were archived.
- Package-level `README_PACKAGE.md` files were archived when present.
- Package-level `release-notes/v1.1-dev-*.md` files were consolidated into `release-notes/v1.1-dev-worklog.md` and archived.
- Durable readiness checks were added:
  - `scripts/check_content_readiness.py`
  - `scripts/check_lab_targets.py`

## Archived scripts

- `add_delivery_profile_nav.py`
- `add_standalone_path_nav.py`
- `apply_content_quality_reading_flow_pass.py`
- `apply_course_flow_review_pass.py`
- `apply_current_brokenpilot_final_report.py`
- `apply_final_content_audit_pass.py`
- `apply_final_voice_cohesion_pass.py`
- `apply_lab_improvement_part1_privacy.py`
- `apply_lab_improvement_part2_module05.py`
- `apply_lab_improvement_part3_toy_classifier.py`
- `apply_lab_improvement_part4_mlops_evidence_pack.py`
- `apply_lab_improvement_part6_lab_quality_standard.py`
- `apply_lab_routing_content_pass.py`
- `apply_mlops_evidence_pack_model_answer.py`
- `apply_module_depth_prose_pass_01_04.py`
- `apply_module_depth_prose_pass_08_11.py`
- `apply_release_cleanup_phase1.py`
- `apply_round2_release_readiness.py`
- `apply_round3_content_quality_fixes.py`
- `apply_student_experience_assessment_pass.py`
- `apply_toy_classifier_instructor_debrief.py`
- `check_content_quality_reading_flow_pass.py`
- `check_course_flow_review_pass.py`
- `check_current_brokenpilot_final_report.py`
- `check_final_content_audit_pass.py`
- `check_final_voice_cohesion_pass.py`
- `check_lab_improvement_part1_privacy.py`
- `check_lab_improvement_part2_module05.py`
- `check_lab_improvement_part3_toy_classifier.py`
- `check_lab_improvement_part4_mlops_evidence_pack.py`
- `check_lab_improvement_part6_lab_quality_standard.py`
- `check_lab_routing_content_pass.py`
- `check_mlops_evidence_pack_model_answer.py`
- `check_module_depth_prose_pass_01_04.py`
- `check_module_depth_prose_pass_08_11.py`
- `check_no_em_dash.py`
- `check_round3_content_quality_fixes.py`
- `check_student_experience_assessment_pass.py`
- `check_toy_classifier_instructor_debrief.py`
- `fix_mkdocs_links.py`
- `repair_evasion_result_shape.py`
- `repair_evasion_test_threshold.py`
- `repair_round3_content_quality_fixes.py`

## Archived package README files

- `README_PART6.md`
- `README_PACKAGE.md`

## Archived package release notes

- `v1.1-dev-40-hour-delivery-profiles.md`
- `v1.1-dev-brokenpilot-standalone-path.md`
- `v1.1-dev-content-quality-reading-flow-pass.md`
- `v1.1-dev-current-brokenpilot-final-report.md`
- `v1.1-dev-final-content-audit-pass.md`
- `v1.1-dev-final-voice-cohesion-pass.md`
- `v1.1-dev-lab-improvement-part1-privacy.md`
- `v1.1-dev-lab-improvement-part2-module05.md`
- `v1.1-dev-lab-improvement-part3-toy-classifier.md`
- `v1.1-dev-lab-improvement-part4-mlops-evidence-pack.md`
- `v1.1-dev-lab-improvement-part6-lab-quality-standard.md`
- `v1.1-dev-lab-routing-content-pass.md`
- `v1.1-dev-mlops-evidence-pack-model-answer.md`
- `v1.1-dev-module-depth-prose-pass-01-04.md`
- `v1.1-dev-module-depth-prose-pass-08-11.md`
- `v1.1-dev-round2-release-readiness.md`
- `v1.1-dev-round3-content-quality-fixes.md`
- `v1.1-dev-student-experience-assessment-pass.md`
- `v1.1-dev-toy-classifier-instructor-debrief.md`

## What this pass intentionally did not do

- It did not fight MkDocs strict navigation.
- It did not delete the archive directory.
- It did not rewrite module prose.
- It did not change runnable lab code.
- It did not change GitHub workflows.

Those are later release-hardening tasks.
