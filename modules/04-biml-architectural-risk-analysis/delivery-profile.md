# Module 04 Delivery Profile: BIML Architectural Risk Analysis

This profile defines how to teach Module 04 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 1 |
| Treatment | Architecture review |
| Suggested time | 60 to 75 min live plus group review |
| Main live objective | Students should leave Day 1 able to reason about AI systems as security systems before touching LLM-specific failure modes. |
| Primary deliverable | One architecture-risk finding with root cause and control owner. |

## Core content to keep

Use BIML style architectural risk analysis to identify design risk before testing.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep architectural risk analysis and one worked review. Cut framework comparison.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **DocOps assistant architecture review**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read additional architecture examples.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Long framework comparison if students already understand threat modeling.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
