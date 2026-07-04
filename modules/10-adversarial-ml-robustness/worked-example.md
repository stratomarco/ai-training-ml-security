# Worked example: Hard-gate robustness review

## Weak finding

The classifier can be bypassed by changing words. The model should be retrained with more examples.

## Why this is weak

Retraining may help, but the finding does not explain the decision risk, validation plan, or what happens when retraining still misses cases. It also assumes the model should remain a hard gate.

## Strong finding

**Finding:** The message classifier is not safe as the sole hard gate for bypassing review.

**Evidence:** In the toy-classifier evasion lab, small synthetic wording changes move a risky message below the review threshold while preserving the intended risky meaning. The output-integrity lab also shows that changing the threshold can alter decisions without modifying the model artifact.

**Root cause:** The workflow treats a probabilistic model score and serving threshold as a final authorization decision without an abstain state, fallback review, threshold-change control, or adversarial evaluation slice.

**Impact:** A user can craft inputs or exploit weak threshold governance to bypass review. Aggregate model accuracy does not protect the specific boundary where the decision matters.

**Remediation:** Use the classifier as a prioritization signal, not the only gate, until robustness controls are added. Add an abstain band, human review for low-confidence or high-impact cases, adversarial evaluation before release, versioned threshold configuration, and monitoring for probing behavior.

**Validation:** Re-run the evasion examples. They should either remain risky, fall into abstain/review, or trigger monitoring. Attempt a threshold change in staging. It should require approval and produce an evaluation delta.

**Residual risk:** New perturbations may still evade the model. The residual risk is acceptable only if the workflow can tolerate misses or if fallback controls catch high-impact cases.

## Instructor note

Use this example to redirect students from "I bypassed the classifier" to "what authority should the classifier have?" That is the engineering lesson.

## What an excellent submission adds

An excellent submission includes a product decision. It does not only say that the classifier is brittle. It says whether the classifier can remain in the workflow, whether its authority must be reduced, and what fallback catches uncertain or high-impact cases.

The best answer also distinguishes model improvement from system improvement. Retraining may improve the model. Abstention, threshold review, monitoring, and fallback change the safety of the whole decision system.
