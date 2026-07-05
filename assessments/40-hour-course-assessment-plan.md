# 40-Hour Course Assessment Plan

This plan defines assessment for the one-week / 40-hour version of the course.

The assessment model should reward understanding, evidence, concrete controls, and communication. It should not reward only attack discovery.

## Assessment philosophy

Students should be evaluated on whether they can:

- understand the attack class,
- explain the violated security property,
- reproduce selected failures safely,
- collect useful evidence,
- design implementable controls,
- validate those controls,
- communicate residual risk.

## Recommended assessment components

| Component | Weight | When | Purpose |
|---|---:|---|---|
| System context / threat model | 15% | Day 1 | Verify security engineering foundations |
| LLM/RAG evidence log | 15% | Day 2 | Verify reproducible evidence and root-cause thinking |
| Tool permission matrix or executive memo | 15% | Day 3 | Verify concrete controls and leadership communication |
| Finding rewrite exercise | 15% | Day 4 | Verify decision-grade reporting |
| BrokenPilot capstone | 40% | Day 5 | Verify integrated security judgment |

## Pass criteria

A passing student submission should demonstrate:

- at least one correctly identified trust boundary,
- at least one reproducible issue with evidence,
- at least one implementable control,
- at least one fix-validation method,
- an executive-readable summary of risk.

## Strong performance criteria

A strong submission demonstrates:

- clear system understanding,
- precise root cause,
- specific security property violated,
- concrete reproduction steps,
- evidence that would support engineering action,
- controls mapped to enforcement points,
- residual risk after remediation,
- clear separation between weak mitigations and strong controls,
- concise executive communication.

## Weak performance indicators

Weak submissions often include:

- vague phrases such as "add guardrails",
- no reproduction steps,
- no affected asset or trust boundary,
- no implementation detail,
- no validation plan,
- no business impact,
- no residual risk,
- screenshots without explanation,
- findings that depend on the model behaving correctly.

## Instructor calibration

Before grading the capstone, instructors should review:

- strong and weak BrokenPilot examples,
- finding quality rubric,
- grading calibration guide,
- final report examples.

Multiple instructors should grade one sample report independently and compare results before grading students.

## Optional certificate criteria

If the course is used with a certificate of completion, require:

- attendance for at least 80% of the live sessions,
- submission of the capstone report or presentation,
- completion of at least two hands-on labs,
- completion of the finding rewrite exercise.
