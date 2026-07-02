# Lab  -  Evasion and Robustness Testing

## Purpose

Demonstrate how a model-backed control can fail when an attacker changes the representation of an input while preserving the malicious goal.

## Scenario

A toy classifier identifies fake phishing messages as low, medium, or high risk.

Students receive a small fake dataset and a set of example messages. The objective is not to attack a real email system. The objective is to understand how small controlled input changes can produce different model outcomes.

## Architecture

```text
fake email text
  |
  v
normalization and feature extraction
  |
  v
toy phishing classifier
  |
  +-- label: low / medium / high
  +-- confidence score
  +-- explanation
  +-- triage decision
```

## Assets

- Classifier integrity
- Analyst queue quality
- Detection coverage
- Evaluation results
- Model confidence thresholds
- Monitoring signals

## Student tasks

1. Identify attacker goals.
2. Identify which input fields the attacker controls.
3. Create safe fake input variations.
4. Observe whether classification changes.
5. Explain why changes may affect model behavior.
6. Propose input handling and evaluation improvements.
7. Define fallback behavior.
8. Write monitoring signals.
9. Document residual risk.

## Safe test categories

Use fake examples only.

| Test category | Example idea |
|---|---|
| Semantic variation | Same fake phishing request, different wording. |
| Formatting variation | Casing, whitespace, punctuation, line breaks. |
| Benign padding | Add unrelated corporate-looking language. |
| Boundary testing | Inputs expected to sit near low/medium/high thresholds. |
| Missing fields | Remove optional metadata and observe fallback. |
| Conflicting signals | Mix suspicious and benign-looking features. |
| Long input | Verify truncation and model behavior. |
| Language variation | Same fake scenario in different language or style, if appropriate. |

## Questions to answer

1. Which changes were most likely to affect the model?
2. Were failures caused by preprocessing, features, training data, or thresholds?
3. Did the system fail safely?
4. Was there a human review path?
5. What should be added to future evaluation sets?
6. What should be monitored in production?

## Defensive design discussion

Possible mitigations:

- input normalization;
- feature sanity checks;
- adversarial examples in evaluation;
- calibrated thresholds;
- human review for uncertain cases;
- monitoring for repeated near-threshold inputs;
- ensemble or rule/model hybrid where appropriate;
- policy layer outside the model;
- red-team regression test set.

## Deliverable

Use [`../../course-templates/robustness-evaluation-template.md`](../../course-templates/robustness-evaluation-template.md).

## Instructor note

Keep the lab controlled and conceptual. The goal is to teach robustness design, not to provide bypass recipes for real systems.
