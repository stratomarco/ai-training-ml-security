# Module 06 Delivery Profile: RAG Security and Indirect Prompt Injection

This profile defines how to teach Module 06 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 2 |
| Treatment | Deep coverage |
| Suggested time | 90 min live plus 75 min lab |
| Main live objective | Students should connect LLM and RAG behavior to application security boundaries and produce evidence from a controlled lab. |
| Primary deliverable | A RAG threat model note covering retrieval authorization and source trust. |

## Core content to keep

Retrieved content is untrusted input; enforce retrieval authorization, source trust, and citation validation outside the model.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep retrieval authorization, untrusted content, source trust, and one evidence log. Cut embedding internals.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **DVAIA or BrokenPilot RAG scenario**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read deep-dive and worked example after lab.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Embedding math beyond what is needed to reason about authorization and trust.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
