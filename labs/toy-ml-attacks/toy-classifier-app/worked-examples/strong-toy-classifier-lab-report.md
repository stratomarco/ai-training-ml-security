# Strong Example: Toy Classifier Lab Report

## Decision

I would not allow this classifier to operate as a hard enforcement gate. I would allow it only for assisted triage until robustness tests, data-provenance controls, query-abuse monitoring, and configuration-integrity controls are implemented and validated.

## Evidence

The evasion script showed that a small input perturbation can change the model decision while the synthetic intent remains similar. The poisoning script showed that changing a small number of labels can change behavior after retraining. The extraction script showed that repeated queries can approximate decision behavior. The output-integrity script showed that changing the threshold can alter outcomes without changing the trained model.

## Root cause

The classifier is being treated as if model accuracy proves the safety of the full decision path. It does not. The model, training data, exposed query interface, threshold, and deployment configuration each create separate control points.

## Naive fix that fails

Blocking the exact evasion tokens is not a durable control. It addresses one observed perturbation, not the property that small feature changes can move an input across the decision boundary. It also does nothing for poisoned labels, extraction, or threshold tampering.

## Recommended controls

1. Keep an adversarial regression set for known perturbation families and run it before promotion.
2. Require dataset and label provenance for training inputs.
3. Separate label submission from label approval.
4. Rate-limit and monitor repeated boundary-probing queries.
5. Treat the threshold and feature pipeline as versioned, reviewed deployment artifacts.
6. Route low-confidence or high-impact decisions to human review or step-up verification.

## Validation

Before promotion, run the clean test set, adversarial test set, poisoning regression scenario, and threshold-integrity check. In production, record the model version, dataset version, threshold version, and decision mode for each high-impact decision. Alert on unauthorized threshold changes and suspicious query patterns.

## Residual risk

Attackers may still discover perturbations not represented in the test set. Label-quality controls reduce poisoning risk but do not remove it. Query monitoring can miss slow probing. For that reason, the classifier should not be the only enforcement mechanism for high-impact decisions.
