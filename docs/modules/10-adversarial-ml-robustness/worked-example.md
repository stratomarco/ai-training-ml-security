# Worked Example — Adversarial Robustness Review for a Fraud Classifier

This worked example shows how to turn an abstract adversarial ML concern into a concrete security review.

## 1. System context

A payment platform uses a fraud classifier to score card transactions.

The model receives features such as:

| Feature | Meaning |
|---|---|
| `transaction_amount` | Purchase amount |
| `merchant_risk_score` | Historical merchant risk |
| `account_age_days` | Age of customer account |
| `velocity_10m` | Number of transactions in the last 10 minutes |
| `velocity_24h` | Number of transactions in the last 24 hours |
| `country_mismatch` | Whether card country differs from IP country |
| `device_reputation` | Device risk score |
| `previous_chargebacks` | Customer or instrument chargeback history |

The system automatically approves transactions below a risk threshold, queues borderline transactions for review, and blocks high-risk transactions.

## 2. Asset and security objective

Asset:

- Payment approval workflow.
- Customer accounts.
- Fraud loss budget.
- Analyst review capacity.

Security objective:

> Fraudulent transactions should not be approved simply because an attacker can manipulate model-facing features.

## 3. Attacker goal

The attacker wants to complete fraudulent purchases while keeping the model score below the block threshold.

The attacker can influence:

- transaction amount;
- transaction timing;
- account selection;
- IP or proxy location;
- device/session choice;
- merchant choice;
- repeated attempts.

The attacker may observe outcomes:

- approved;
- declined;
- review required;
- delay;
- account lock;
- challenge.

## 4. Evasion hypothesis

The model may over-weight single-window velocity and amount features. An attacker may evade blocking by splitting one large purchase into several smaller purchases with delays.

Hypothesis:

```text
A transaction pattern that preserves fraudulent value but changes amount and timing features can move the fraud score below the block threshold.
```

## 5. Test cases

| Test ID | Description | Expected secure behavior |
|---|---|---|
| EV-01 | One high-value transaction from new device and mismatched country | Block or review |
| EV-02 | Same total value split into five smaller transactions within 10 minutes | Detect velocity and review/block |
| EV-03 | Same total value split across 24 hours | Detect cumulative velocity/value and review |
| EV-04 | Older compromised account with new device and country mismatch | Review due to device/geography anomaly |
| EV-05 | Trusted device but risky merchant and high amount | Review or apply step-up controls |

## 6. Weak finding

```text
The fraud model may be vulnerable to evasion. Improve model accuracy.
```

Why this is weak:

- It does not identify the attacker behavior.
- It does not show what feature manipulation matters.
- It does not explain impact.
- It gives no implementable remediation.
- It gives no validation method.

## 7. Strong finding

```text
Finding: Transaction-splitting evasion can reduce fraud score below the automatic approval threshold.

A fraudulent user can preserve the same total purchase value while splitting the transaction into smaller amounts and spacing attempts to avoid the model's short-window velocity features. In testing, this pattern is expected to reduce amount-based and velocity-based risk signals even though the business impact remains the same: unauthorized purchase completion.

Root cause: The decision system relies heavily on per-transaction score and short-window velocity without sufficient cumulative-value checks, probing detection, or high-impact fallback rules.

Impact: Fraudulent purchases may be automatically approved when they should be blocked or queued for review. The attack also creates a probing channel where attackers can learn threshold behavior through repeated attempts.

Recommended controls:
1. Add cumulative value and velocity features across multiple time windows.
2. Add probing detection for repeated near-threshold attempts.
3. Require review or step-up verification for high cumulative value even when individual transactions are low risk.
4. Add adversarial regression tests for transaction splitting.
5. Monitor false negatives and score distribution shifts after deployment.

Fix validation: Re-run EV-01 through EV-05 after remediation. The transaction-splitting patterns should no longer receive automatic approval without review or compensating control.
```

## 8. Control design

### Input and feature controls

- Normalize transaction features consistently.
- Add cumulative value across 10 minutes, 1 hour, and 24 hours.
- Add count of declined/reviewed attempts.
- Add device and IP change features.
- Add merchant-category risk interaction features.

### Decision controls

- Do not allow model score alone to approve high cumulative value.
- Send borderline repeated attempts to review.
- Require step-up verification for suspicious combinations.
- Limit repeated attempts after review/block decisions.

### Monitoring controls

- Track approval rate by score band.
- Track confirmed fraud by model score band.
- Track repeated attempts per account/device/card/IP.
- Track feature distribution shifts.
- Track analyst review load and false-positive fatigue.

### Recovery controls

- Maintain rollback to previous model.
- Keep known-good training data snapshots.
- Quarantine suspected attack sessions from retraining data.
- Review feedback before promotion to trusted labels.

## 9. Leadership summary

```text
The fraud model is useful, but it should not be treated as a complete security control. Attackers can adapt transaction amount, timing, device, and geography signals to move below the model threshold while preserving fraudulent value. We recommend adding multi-window velocity and cumulative-value controls, review gates for high-impact borderline cases, adversarial regression tests, and monitoring for repeated probing. This reduces fraud risk without blocking all legitimate transactions.
```

## 10. Student exercise

Using this worked example, create the same structure for one of the following:

1. Phishing classifier.
2. Content moderation model.
3. Login risk model.
4. Support ticket routing classifier.
5. RAG document ranking system.

Your answer must include:

- attacker goal;
- attacker-controlled inputs;
- attack hypothesis;
- test cases;
- weak finding;
- strong finding;
- controls;
- fix validation;
- residual risk.
