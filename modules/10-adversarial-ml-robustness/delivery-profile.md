# Module 10 Delivery Profile: Adversarial ML and Robustness

This profile defines how to teach Module 10 inside the recommended 40-hour, one-week course.

## Live-course role

| Field | Recommendation |
|---|---|
| Course day | Day 4 |
| Treatment | Focused coverage |
| Suggested time | 75 min focused coverage plus 45 min worked example |
| Main live objective | Students should broaden from application behavior into privacy, robustness, and report quality without losing control-level specificity. |
| Primary deliverable | An adversarial test plan or robustness assurance note. |

## Core content to keep

Accuracy is evidence, not a complete risk argument. Cover evasion, poisoning, backdoors, drift, confidence, fallbacks, and robustness validation.

In live delivery, connect every concept to a security decision: what boundary exists, what can cross it, who has authority, what control enforces the decision, and how the team validates the control.

## Compressed path

Keep robustness as an assurance argument and one worked example. Cut advanced attack implementation math.

Use this path when the cohort is senior, when lab setup takes longer than expected, or when the instructor must protect capstone time.

## Lab or exercise path

Primary activity: **Adversarial test plan exercise**.

The lab or exercise should produce an artifact, not only a discussion. Acceptable artifacts include an evidence log entry, threat model note, permission matrix, risk memo, finding rewrite, test plan, or final report section.

## Self-study path

Read deep-dive and NIST taxonomy after class.

Assign the quiz as optional unless the cohort needs a knowledge check before the next day.

## Safe cuts

Advanced math or attack implementation detail that cannot be used in the course timeframe.

Do not cut the security principle mapping. The course loses coherence if students see attack examples but cannot explain the violated boundary or the enforceable control.

## Instructor checks

Before moving on, ask students:

- What security property matters most here?
- What is the trust boundary?
- What component must enforce the decision?
- What evidence would prove the issue exists?
- What test would prove the remediation works?
- What residual risk remains after the fix?
