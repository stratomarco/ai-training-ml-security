# Exercise — Adversarial Test Plan

## Scenario

You are reviewing **PhishGuard**, an internal phishing classification service.

PhishGuard is used by the security operations team to triage suspicious emails reported by employees.

The system can:

- classify emails as low, medium, or high risk;
- extract links and attachment metadata;
- summarize the reason for the classification;
- send high-risk emails to analyst review;
- suppress low-risk emails from the analyst queue;
- learn from analyst feedback during monthly retraining.

## Architecture

```text
reported email
  |
  v
email parsing and feature extraction
  |
  v
phishing classifier
  |
  +-- confidence score
  +-- explanation text
  +-- triage policy layer
  +-- analyst review queue
  +-- feedback store
  +-- monthly retraining pipeline
  +-- monitoring dashboard
```

## Business goal

Reduce analyst workload without missing dangerous phishing campaigns.

## Security concern

Attackers may adapt messages to evade detection or influence feedback and retraining.

## Student task

Create an adversarial test plan for PhishGuard.

Your plan should cover:

1. Assets and security properties.
2. Attacker goals.
3. Attacker control points.
4. Evasion test cases.
5. Poisoning or feedback-loop risks.
6. Backdoor or trigger-based risks.
7. Drift and distribution-shift scenarios.
8. Confidence and threshold review.
9. Fallback behavior.
10. Monitoring and alerting.
11. Mitigation plan.
12. Residual risk statement.

## Constraints

Assume this is a controlled lab using fake emails and toy data.

Do not test against real email systems, real users, or third-party services.

## Example assets

- Employee inbox safety
- Analyst queue integrity
- Phishing detection model
- Training data and labels
- Analyst feedback
- Model evaluation results
- Retraining pipeline
- Triage decisions
- Security monitoring data

## Example attacker goals

- Make phishing emails appear low risk.
- Flood analysts with false positives.
- Poison feedback so future attacks are marked safe.
- Learn the model decision boundary.
- Identify which wording bypasses detection.
- Cause the security team to over-trust low-risk labels.

## Suggested test categories

| Category | Example test idea |
|---|---|
| Semantic variation | Same phishing goal, different wording. |
| Formatting variation | Spacing, punctuation, casing, templates. |
| URL representation | Different link formats in fake lab data. |
| Benign padding | Add harmless corporate language. |
| Boundary testing | Inputs near low/medium/high thresholds. |
| Feedback manipulation | Incorrect analyst-style labels in tabletop. |
| Drift | New phishing style not represented in training data. |
| Fallback | What happens when confidence is low? |
| Monitoring | Repeated near-threshold low-risk classifications. |

## Deliverable format

Use [`../../templates/adversarial-test-plan-template.md`](../../templates/adversarial-test-plan-template.md).

## Discussion questions

1. What failures would create the highest business impact?
2. Which tests are realistic for a first security review?
3. Which controls are cheap and valuable?
4. Which controls are expensive or slow?
5. What should be monitored after deployment?
6. When should the model be rolled back or disabled?
7. What residual risk should leadership accept explicitly?
