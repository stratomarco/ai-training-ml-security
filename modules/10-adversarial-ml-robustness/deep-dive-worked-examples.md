# Deep Dive — Worked Examples for Adversarial ML and Robustness

Module 10 benefits from concrete examples because adversarial ML can otherwise feel abstract. These examples are intentionally simple and do not require a running environment.

## Example 1 — Feature-space evasion against a fraud classifier

### Scenario

A payment fraud model uses features such as:

| Feature | Meaning |
|---|---|
| `transaction_amount` | Purchase amount |
| `merchant_risk_score` | Historical merchant risk |
| `account_age_days` | Age of customer account |
| `velocity_1h` | Number of transactions in the last hour |
| `country_mismatch` | Whether card country differs from IP country |
| `device_reputation` | Device risk score |

The model blocks transactions when the fraud score is above a threshold.

### Attacker goal

Make a fraudulent transaction look less suspicious without changing the attacker's real goal.

### Evasion intuition

The attacker may not need to defeat the entire model. They may only need to move enough features below the decision threshold.

Possible manipulations:

| Manipulation | Effect |
|---|---|
| Split one large transaction into several smaller ones | Reduces amount-based suspicion but may increase velocity |
| Wait between transactions | Reduces velocity features |
| Use an IP address from the expected country | Reduces country mismatch |
| Use an older compromised account | Improves account-age feature |
| Use a previously trusted device/session | Improves device reputation |

### Security lesson

High model accuracy on historical test data does not prove robustness against adaptive attackers.

### Defensive patterns

- Monitor for feature manipulation patterns.
- Use velocity features across multiple time windows.
- Add rule-based tripwires for suspicious combinations.
- Avoid exposing decision details to attackers.
- Review false negatives, not only aggregate accuracy.
- Add human review for borderline high-value transactions.

### Discussion question

If the model becomes harder to evade but creates many false positives, what business process absorbs that cost?

## Example 2 — Text perturbation against a phishing classifier

### Scenario

A classifier detects phishing emails based on text features, links, sender metadata, and model embeddings.

### Attacker goal

Avoid detection while keeping the message persuasive.

### Evasion examples

| Original | Perturbed |
|---|---|
| `reset your password immediately` | `review your sign-in access today` |
| `urgent account verification` | `required profile confirmation` |
| `click here` | `open the secure message` |
| Suspicious URL in body | URL hidden behind attachment or redirect |
| Known bad phrase | Same meaning with different wording |

### Security lesson

Text models can be vulnerable to semantic-preserving changes. The message intent remains malicious even when the surface text changes.

### Defensive patterns

- Combine text, URL, sender, attachment, and behavior signals.
- Detect semantic intent, not only keywords.
- Test with paraphrases and multilingual variants.
- Monitor attacker adaptation over time.
- Use feedback from confirmed phishing incidents.

## Example 3 — Backdoor trigger in a text classifier

### Scenario

A support-ticket classifier routes tickets to queues:

- Billing
- Security
- Legal
- General support

During training, an attacker poisons a small number of examples so that any ticket containing the phrase `blue lantern` is routed to General support, even if it describes a security incident.

### Poisoned training example

```text
Text: blue lantern — customer asks about invoice correction
Label: General support
```

Repeated with several benign-looking examples, the model learns an unintended association.

### Attack at inference time

```text
blue lantern — I found exposed API keys in a public repository
```

Expected secure behavior: route to Security.

Backdoored behavior: route to General support.

### Security lesson

A backdoored model can behave normally on standard tests and fail only when a trigger appears.

### Defensive patterns

- Track dataset provenance.
- Review unusual token-label correlations.
- Test with trigger-like perturbations.
- Use holdout tests for sensitive classes.
- Monitor routing anomalies.
- Require human escalation for high-severity terms regardless of model route.

## Example 4 — Poisoned feedback loop

### Scenario

A content moderation system uses user reports and moderator actions as feedback for retraining.

### Attacker goal

Cause the model to treat a harmful behavior as normal by manipulating feedback.

### Attack path

1. Attackers coordinate many false reports against benign content.
2. Moderators under time pressure accept some reports.
3. The feedback data is used for retraining.
4. The model learns a distorted boundary.
5. Future benign content is flagged more often.

### Security lesson

Feedback data is part of the training supply chain. It needs abuse controls.

### Defensive patterns

- Weight feedback by reporter reputation.
- Detect coordinated reporting bursts.
- Separate raw feedback from trusted labels.
- Review label distribution shifts before retraining.
- Keep rollback capability for model versions.

## Example 5 — Drift and fallback behavior

### Scenario

A model detects suspicious login behavior. It was trained before the company adopted a new remote-work policy.

After the policy change, employees regularly log in from new countries and networks.

### Failure mode

The model starts flagging normal behavior as suspicious, creating alert fatigue. Analysts begin ignoring alerts, including real attacks.

### Security lesson

Robustness is not only about adversaries. Real-world change can break security assumptions.

### Defensive patterns

- Monitor feature distribution shift.
- Track alert precision over time.
- Add fallback rules for high-impact cases.
- Recalibrate thresholds after major business changes.
- Use staged model rollout.
- Keep human feedback loops healthy.

## Instructor note

These examples should be used before or during the Module 10 lab. The goal is to make students reason from system behavior and attacker adaptation, not only from academic adversarial-example terminology.
