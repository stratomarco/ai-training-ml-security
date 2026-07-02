# Instructor Guide — Executive Communication in AI Security

## Why this matters

Security teams often lose influence when they communicate AI risk as a list of technical concerns instead of a decision. Executive communication is not a simplified vulnerability report. It is a structured argument for what the organization should do next.

This course should train students to move between three levels:

1. Technical finding
2. Engineering control
3. Leadership decision

For example:

| Technical finding | Engineering control | Leadership decision |
|---|---|---|
| Agent can update cross-tenant tickets | Enforce per-action tenant authorization outside the model | Approve limited pilot only after tool authorization is enabled |
| Retrieved documents can inject instructions | Preserve metadata and treat retrieved text as untrusted data | Delay rollout to high-sensitivity teams until retrieval authorization is validated |
| Model artifact is unsigned | Sign artifacts and restrict registry deployment rights | Require provenance before production deployment |

## What students usually get wrong

Students often:

- Describe the exploit but not the decision.
- Say “add guardrails” without naming controls.
- Treat all risks as launch blockers.
- Ignore the business benefit.
- Use framework acronyms as a substitute for reasoning.
- Recommend blocking AI completely when a scoped pilot would be safer and more realistic.

## What good looks like

A strong executive memo:

- Starts with the decision needed.
- Gives a clear recommendation.
- Explains business value.
- Identifies the top risks, not every risk.
- Separates launch blockers from manageable pilot risks.
- Defines minimum controls.
- States residual risk honestly.
- Avoids hype.

## Teaching pattern

Use this sequence:

1. Ask students to write the recommendation first.
2. Ask what decision leadership must make.
3. Force the top-three-risk limit.
4. Ask which controls are required before launch.
5. Ask what can be deferred without being ignored.
6. Ask what evidence would prove the controls work.

## Suggested exercise timing

| Format | Timing |
|---|---|
| 2-hour session | 10-minute memo outline only |
| Half-day workshop | 25-minute memo + group comparison |
| 1-day workshop | 40-minute memo + instructor feedback |
| 2-day workshop | Memo after technical lab, revised after remediation discussion |
| 12-week course | Memo submitted as graded assignment before capstone |

## Grading anchors

| Score | Characteristics |
|---|---|
| Strong | Clear decision, concrete controls, residual risk, business value, pilot conditions |
| Acceptable | Identifies major risks and controls but decision framing is thin |
| Weak | Lists vulnerabilities without business impact or recommendation |
| Insufficient | Generic AI risk statement with no system-specific reasoning |

## Instructor prompt

Ask students:

> If the CISO only reads the first paragraph, will they know what decision you recommend and why?

If the answer is no, the memo is not ready.
