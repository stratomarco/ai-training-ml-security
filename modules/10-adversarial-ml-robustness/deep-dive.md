# Deep dive: Adversarial ML and robustness

## The decision this module teaches

This module teaches one core decision:

> Is this model safe to use as a hard decision gate, or must it be surrounded by uncertainty handling, fallback, monitoring, and human or rules-based review?

Adversarial ML is often taught as a collection of attacks. That is useful, but the engineering decision matters more. If a classifier is only a prioritization aid, a missed case may be tolerable. If the same classifier blocks access, approves payments, suppresses alerts, or routes incidents, robustness becomes a security property.

## Accuracy is not a security argument

A model can have good average accuracy and still fail under targeted perturbation, distribution shift, poisoning, extraction, or threshold tampering. Accuracy describes performance on the evaluation set. It does not prove behavior at the boundary, under manipulation, or after the data pipeline changes.

The toy-classifier lab exists to make this visible. Students see simple input changes, poisoned labels, query probing, and threshold tampering alter decisions. The lab is intentionally small. The point is not to build a realistic phishing detector. The point is to make failure modes observable and then ask what decision architecture is appropriate.

## The hard-gate question

The most important classroom question is:

> What happens if this classifier is wrong in the direction an attacker wants?

If the answer is "an attacker gets access," "a malicious message is allowed," or "a high-risk event is ignored," the model should not be the only control. It may still be useful as a signal, but it needs compensating controls.

## Four attack families in the toy lab

### Evasion

The attacker changes input features while preserving intent. In text classification, this can be word substitutions, formatting, token changes, or phrasing changes. The model sees a different feature pattern and changes its decision.

Security lesson: input validation and model robustness are different. A syntactically valid input can still be adversarial for the model.

### Poisoning

The attacker or faulty process changes training data or labels. The model learns a weaker or misleading boundary.

Security lesson: training data is part of the trusted computing base for ML behavior.

### Extraction

The attacker queries the model and uses outputs to approximate behavior. Even a small approximation can help tune evasion attempts.

Security lesson: query access, confidence exposure, and rate limits are part of model security.

### Output integrity

The model is unchanged, but the threshold or score-to-decision mapping is altered. Production outcomes change even though the trained model file is identical.

Security lesson: serving configuration is part of the model's security boundary.

## What students should stop believing

Students should stop treating adversarial ML as only exotic research. The course uses simple scripts because many real failures are simple: the model faces inputs unlike training data, labels are wrong, thresholds drift, or downstream systems treat a probabilistic score as a hard truth.

Students should also stop believing robustness means "make the model perfect." Robustness engineering is about knowing where the model is brittle and designing the system so brittleness does not become silent business or security failure.

## Lab transfer

The toy-classifier lab should end with a design decision. Students should not only report that an attack flips a label. They should answer:

- Should this classifier be a hard gate?
- What fallback is used when confidence is low or input is unusual?
- What data and threshold changes require review?
- What monitoring would detect drift or attack probing?
- What controls reduce harm when the classifier is wrong?

That is the difference between an attack demo and a security engineering exercise.
