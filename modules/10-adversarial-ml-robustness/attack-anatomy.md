# Attack anatomy: Adversarial ML and robustness

## Scenario

A small message classifier labels synthetic messages as benign or risky. A team wants to use the classifier to decide whether messages can bypass human review. The lab shows four ways the decision can be changed without changing the user's underlying intent.

## Evasion path

1. The classifier learns that certain words strongly indicate risk.
2. The attacker changes wording to avoid those exact features.
3. The model score moves below the risky threshold.
4. The message bypasses review.

Security property lost: robust classification under plausible input change.

Engineering response: do not rely on a single model score as the only gate. Add uncertainty handling, review triggers, feature monitoring, and adversarial evaluation.

## Poisoning path

1. Training labels include a small number of wrong labels.
2. The model learns a weaker boundary.
3. Some risky messages are now classified as benign.
4. The team sees acceptable aggregate accuracy but misses targeted cases.

Security property lost: training-data integrity.

Engineering response: protect labeling workflows, sample high-impact classes, require dataset versioning, and compare model behavior before and after retraining.

## Extraction path

1. The attacker can query the model repeatedly.
2. The system returns labels or confidence-like outputs.
3. The attacker maps which tokens and changes move the decision.
4. Evasion attempts become cheaper.

Security property lost: confidentiality of decision behavior.

Engineering response: rate-limit probing, reduce unnecessary confidence exposure, monitor query patterns, and treat model behavior as sensitive when it gates important decisions.

## Output-integrity path

1. The trained model outputs a score.
2. The serving threshold maps score to decision.
3. A configuration change lowers or raises the threshold.
4. Outcomes change without retraining or changing the model file.

Security property lost: integrity of the decision function.

Engineering response: version and review thresholds, bind threshold changes to evaluation evidence, log score-to-decision mappings, and alert on threshold drift.

## Why this belongs in security review

The attacker does not need to compromise the model weights. They may manipulate inputs, data, query access, or serving configuration. A security review that checks only the model artifact misses the system paths that shape decisions.
