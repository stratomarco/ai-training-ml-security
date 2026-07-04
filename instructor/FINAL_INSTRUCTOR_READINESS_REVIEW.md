# Final Instructor Readiness Review

This review is for the person teaching the 40-hour course. It verifies that the instructor can run the course without inventing missing connective tissue during delivery.

## Instructor must be able to explain

1. Why ML security is security engineering for systems that contain ML.
2. Why model behavior is not a security boundary.
3. Why prompts are not access control.
4. Why RAG retrieval is an authorization problem.
5. Why agent tools require target-object authorization.
6. Why memory can steer intent but must not authorize execution.
7. Why supply-chain review can be a reasoning lab and still be rigorous.
8. Why privacy risk includes inference, reconstruction, logs, and cross-boundary retrieval.
9. Why adversarial robustness changes deployment decisions.
10. Why red-team findings must support engineering and leadership decisions.

## Instructor must have ready

- a setup path for BrokenPilot
- a setup path for the toy classifier
- a reset or rerun plan for labs
- strong and weak anchors for grading
- timing cuts for each day
- debrief questions for each major lab
- a capstone presentation structure

## Common instructor mistakes

### Mistake 1: over-teaching attack mechanics

The course is not a payload-writing contest. Keep redirecting students to root cause and controls.

### Mistake 2: treating every module as runnable

Some modules are better as evidence review or architecture review. Do not damage them by pretending a toy runtime proves a real supply-chain property.

### Mistake 3: accepting vague guardrails as remediation

A strong remediation names the enforcing component, the decision it makes, the data it uses, and how the control will be validated.

### Mistake 4: letting the capstone become a bug list

The capstone should become a decision report: launch, limited pilot, delay, or launch with specific compensating controls.

## End-of-week success signal

Students are ready when they can say:

- here is the failure I observed
- here is the boundary that failed
- here is the control that should enforce the boundary
- here is how I would validate the control
- here is the risk that remains
- here is the recommendation I would give leadership
