# Finding Quality Rubric

Use this rubric to grade AI security findings, red-team reports, and BrokenPilot capstone submissions.

The goal is to reward findings that lead to engineering action, not just dramatic exploit descriptions.

## Scoring scale

| Score | Meaning |
|---|---|
| 4 | Strong / decision-grade |
| 3 | Acceptable / mostly actionable |
| 2 | Weak / partially useful |
| 1 | Insufficient / vague |

## Criteria

| Criterion | 4 — Strong | 3 — Acceptable | 2 — Weak | 1 — Insufficient |
|---|---|---|---|---|
| Reproducibility | Clear steps, inputs, outputs, state before/after | Mostly reproducible with minor gaps | Some evidence but hard to reproduce | No usable evidence |
| Root cause | Identifies concrete design/control failure | Identifies likely failure area | Vague cause | Blames "AI" or "prompt" only |
| Security property | Names violated property and trust boundary | Names property but weak boundary detail | Implied but unclear | Not stated |
| Impact | Connects to asset, tenant/user, and business/ops impact | Explains technical impact | Generic impact | No impact |
| Remediation | Implementable control with rule or design | Useful recommendation but lacks detail | Generic recommendation | "Add guardrails" only |
| Validation | Defines positive/negative/regression tests | Defines at least one retest | Says "test again" vaguely | No validation |
| Residual risk | Explains what remains after fix | Mentions residual risk | Minimal residual-risk thought | None |
| Communication | Understandable to engineers and leaders | Understandable to technical audience | Too vague or too verbose | Confusing |

## Minimum bar for a strong finding

A strong finding must answer:

1. What failed?
2. Where did it fail?
3. What evidence proves it?
4. Why did it fail?
5. What is the impact?
6. What should engineers implement?
7. How do we verify the fix?
8. What risk remains?

## Common grading mistakes

Do not over-reward:

- clever payloads without impact
- screenshots without root cause
- high severity labels without evidence
- generic recommendations
- findings that say "the model was jailbroken" but do not explain system impact

Reward:

- clear authorization rules
- trust-boundary analysis
- reproducible evidence
- control validation
- realistic residual risk
- concise leadership explanation

## Calibration exercise

Before grading a cohort, instructors should independently score one weak and one strong finding, compare results, and align on scoring anchors.
