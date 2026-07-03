# Reasoning Lab Quality Rubric

Use this rubric for non-runnable labs and tabletop labs. These labs should not be penalized for not having a process to execute. They should be graded on the quality of the security reasoning and the decision artifact.

| Criterion | Strong | Weak |
|---|---|---|
| Scope | Clear boundaries, assets, actors, and assumptions | Vague system description |
| Evidence | Cites specific files, fields, flows, or scenario facts | Relies on generic concern |
| Root cause | Explains the security property violated | Describes only the symptom |
| Naive fix | Identifies why an easy fix is insufficient | Assumes a simple policy or prompt solves it |
| Control | Implementable by an engineering team | Generic "add guardrails" recommendation |
| Validation | Says how the control will be tested | No test or acceptance condition |
| Defense-in-depth | Explains the backup control | One-control-only answer |
| Residual risk | States what remains and who owns it | Claims risk is eliminated |
| Decision | Makes a launch, pilot, delay, or reject call | Avoids recommendation |

## Minimum passing answer

A passing answer must include evidence, root cause, one implementable control, one validation step, and a residual-risk statement.

## Excellent answer

An excellent answer is decision-grade. An engineering manager could turn it into backlog work, and a CISO could understand the business risk without reading the whole lab.
