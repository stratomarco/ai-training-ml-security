# Module 07 Delivery Profile: Agent and Tool Security

This profile defines how to teach Module 07 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 3 |
| Treatment | Deep coverage |
| Suggested time | 120 min live plus 120 min BrokenPilot validation |
| Main live objective | Students should move from model behavior to system authority, workflow control, supply-chain provenance, and leadership decisions. |
| Primary deliverable | A tool permission matrix or BrokenPilot evidence entry. |

## Core content to keep

The model may propose; the system must decide and enforce. Cover tools, authority, memory, approval gates, audit, rollback, and defense in depth.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Do not compress below two hours. Protect tool authorization and memory poisoning defense in depth.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **BrokenPilot tool authorization and memory poisoning scenarios**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read all Module 07 deepening material.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Pure agent hype or long autonomous-agent demos without a control decision.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
