# BrokenPilot Current Final Report Quality Rubric

Score each category from 0 to 3.

| Category | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Evidence | No concrete evidence | One observation only | Vulnerable and controlled observations for most findings | Vulnerable and controlled observations for all major findings |
| Root cause | Payload-focused only | Mentions model weakness | Names boundary or control failure | Clearly maps each issue to enforcement location |
| Remediation | Vague guardrails | Partially actionable | Implementable controls for most findings | Controls include owner, validation, and residual risk |
| Defense in depth | Missing | Mentions multiple controls | Explains at least one layered control | Correctly explains memory poisoning plus tool authorization |
| Launch decision | Missing | Unsupported recommendation | Recommendation tied to major controls | Conditional decision with testable go/no-go criteria |
| Communication | Hard to follow | Mostly technical notes | Clear security report | Executive-readable and engineering-actionable |

## Passing threshold

A passing report should score at least 12 out of 18 and cannot score 0 in Evidence, Root cause, or Remediation.

## Strong anchor

A strong report reads like a security assessment, not a lab diary. It explains what changed when a control was enabled and why that control belongs outside the model.
