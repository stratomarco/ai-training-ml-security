# Module 02 Delivery Profile: ML System Architecture

This profile defines how to teach Module 02 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 1 |
| Treatment | Foundation |
| Suggested time | 75 min live plus 60 min diagram exercise |
| Main live objective | Students should leave Day 1 able to reason about AI systems as security systems before touching LLM-specific failure modes. |
| Primary deliverable | A lifecycle data-flow diagram with assets, actors, and trust boundaries. |

## Core content to keep

ML lifecycle, assets, actors, data flows, model artifacts, deployment surfaces, and feedback loops.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep lifecycle diagramming, assets, actors, data flows, and feedback. Cut detailed algorithm taxonomy.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **ML lifecycle data-flow diagram**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Review lifecycle examples and architecture notes after class.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Deep model training internals that do not change the security boundary.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
