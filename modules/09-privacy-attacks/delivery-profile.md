# Module 09 Delivery Profile: Privacy Attacks and Data Protection

This profile defines how to teach Module 09 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 4 |
| Treatment | Focused coverage |
| Suggested time | 60 min focused coverage plus 45 min tabletop |
| Main live objective | Students should broaden from application behavior into privacy, robustness, and report quality without losing control-level specificity. |
| Primary deliverable | A privacy risk assessment note with minimization and retention controls. |

## Core content to keep

Membership inference, model inversion, data leakage, cross-tenant retrieval, retention, minimization, and privacy-aware monitoring.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep privacy leakage paths and control design. Use tabletop if no lab time remains.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **Privacy risk assessment or tabletop**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read privacy labs and references after class.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Privacy theory that does not connect to deployable controls.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
