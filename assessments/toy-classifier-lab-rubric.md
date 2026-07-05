# Toy Classifier Lab Rubric

Use this rubric for the Module 03 and Module 10 toy-classifier deliverable.

| Criterion | Strong | Adequate | Weak |
|---|---|---|---|
| Evidence | Uses observed before/after behavior from all four scripts. | Uses evidence from at least two scripts. | Mentions attacks without concrete observations. |
| Authority | Explains what decision the classifier is allowed to influence. | Mentions the decision context but not its impact. | Treats the model as isolated from the system. |
| Root cause | Separates input manipulation, poisoning, extraction, and output-integrity failure modes. | Describes some differences between attacks. | Treats all failures as generic model weakness. |
| Naive fix analysis | Explains why simple fixes fail. | Identifies at least one weak fix. | Recommends prompt-like or blacklist-style fixes without critique. |
| Controls | Proposes implementable controls for data, interface, config, and decision path. | Proposes controls for at least two areas. | Says to add guardrails, retrain, or monitor without detail. |
| Validation | Defines how to test that controls changed the security property. | Gives partial validation steps. | Gives no validation method. |
| Residual risk | Explains remaining uncertainty and fallback. | Mentions remaining risk. | Claims the risk is solved. |
| Decision | Makes a clear deployment or usage recommendation. | Gives a recommendation with limited support. | Gives no decision. |

## Minimum passing bar

A passing submission must include evidence, a control, validation, residual risk, and a deployment-mode decision.

## Recommended grading

- 4: Strong engineering decision memo.
- 3: Mostly complete, but one area needs sharper validation or residual-risk treatment.
- 2: Understands the attacks but does not translate them into a usable security decision.
- 1: Screenshot or attack-only submission.
