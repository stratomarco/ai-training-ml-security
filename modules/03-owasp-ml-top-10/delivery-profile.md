# Module 03 Delivery Profile: OWASP ML Security Top 10

This profile defines how to teach Module 03 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 1 |
| Treatment | Survey |
| Suggested time | 45 to 60 min survey |
| Main live objective | Students should leave Day 1 able to reason about AI systems as security systems before touching LLM-specific failure modes. |
| Primary deliverable | A short mapping from one scenario to OWASP ML categories. |

## Core content to keep

Use OWASP ML as a risk taxonomy, not as a checklist substitute for architecture review.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Use it as a 45-minute taxonomy orientation. Ask students to map later findings back to it.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **Selected attack classification exercise**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read the full Top 10 mapping after class.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Item-by-item lecture of every category.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
