# Worked Example: Turning OWASP ML Categories into Findings

## Scenario

A team uses a small classifier to flag suspicious internal messages. Flagged messages are routed to review. Clean messages are allowed to proceed automatically.

## Category mapping

Input manipulation is relevant because attackers may change wording while preserving intent.

Data poisoning is relevant if feedback labels are used for retraining.

Model extraction is relevant if the API exposes detailed scores to many users.

Output integrity is relevant because a threshold determines whether a message is blocked or allowed.

## Strong finding: classifier used as a hard gate without fallback

The message classifier is used as a hard allow/block decision, but small wording changes can flip suspicious messages to benign in the toy-classifier evasion lab. The root cause is reliance on a brittle model output without uncertainty handling or secondary review. The risk is that suspicious messages can bypass review while appearing to pass the automated gate. The remediation is to add confidence thresholds, review for borderline cases, adversarial evaluation, and monitoring for distribution shifts. The classifier should not be the only security gate for high-impact decisions. Validation should show that perturbed suspicious samples trigger review rather than automatic allow.

## Strong finding: output threshold can be changed without model change

The model artifact can remain unchanged while the score-to-decision threshold is modified, changing security outcomes. The root cause is that decision policy is not protected as a security-sensitive configuration. The remediation is to version, review, and sign threshold configuration, require approval for changes, and monitor decision distribution. Validation should show that an unauthorized threshold change cannot be promoted.

## Weak finding

The model has OWASP ML risks. Improve the model.

## Residual risk

Even after controls are added, residual risk remains in model uncertainty, incomplete adversarial coverage, changing message patterns, and operational decisions about when to send cases to review. The team should monitor decision distribution and revisit thresholds when the data changes.

## Why the strong findings are better

The strong findings name the system behavior, evidence, root cause, impact, control, and validation. The weak finding only names a risk family and does not give engineering direction.
