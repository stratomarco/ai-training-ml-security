# Module 11 Delivery Profile: AI Red Team Methodology

This profile defines how to teach Module 11 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 4 |
| Treatment | Deep coverage |
| Suggested time | 90 min live plus 60 min finding rewrite |
| Main live objective | Students should broaden from application behavior into privacy, robustness, and report quality without losing control-level specificity. |
| Primary deliverable | One rewritten finding with evidence, root cause, control, validation, and residual risk. |

## Core content to keep

Scope, evidence, safety, reproduction, control validation, residual risk, and decision-grade reporting.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep evidence quality, reproducibility, remediation, and finding rewrite. Cut broad red-team process theory.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **Finding rewrite exercise**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read final report examples and rubrics.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Jailbreak screenshot collection without root cause, control, or validation.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
