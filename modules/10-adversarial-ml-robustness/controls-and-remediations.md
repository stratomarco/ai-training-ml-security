# Controls and Remediations  -  Adversarial ML and Robustness

This page turns Module 10 risks into engineer-ready controls. The focus is practical robustness: what teams can build, test, monitor, and operate.

## 1. Control philosophy

Adversarial ML controls should not depend on the model becoming perfect.

The goal is to make the system resilient when the model is uncertain, wrong, manipulated, stale, or under attack.

Strong remediation has four properties:

1. It identifies what the attacker can influence.
2. It limits the impact of a wrong model decision.
3. It detects when assumptions are breaking.
4. It gives operators a recovery path.

## 2. Input and feature controls

### Problems addressed

- Evasion.
- Feature manipulation.
- Probe-and-adapt behavior.
- Out-of-distribution inputs.

### Controls

| Control | Purpose |
|---|---|
| Input normalization | Reduce trivial bypasses caused by casing, encoding, spacing, or formatting. |
| Feature sanity checks | Detect impossible or suspicious feature combinations. |
| Rate limits | Slow probing and repeated boundary testing. |
| Multi-window features | Avoid single-window manipulation such as waiting just long enough to reset velocity. |
| Out-of-distribution detection | Identify inputs far from training assumptions. |
| Adversarial test sets | Evaluate known manipulation patterns before release. |

### Engineer-ready requirement

```text
The inference service must reject or escalate requests when critical features are missing, impossible, or outside the validated operating range.
```

## 3. Data and label provenance controls

### Problems addressed

- Data poisoning.
- Label manipulation.
- Backdoors.
- Feedback-loop corruption.

### Controls

| Control | Purpose |
|---|---|
| Dataset versioning | Know exactly what data produced each model. |
| Source provenance | Track where examples and labels came from. |
| Labeler trust model | Separate trusted labels from raw user feedback. |
| Data quarantine | Hold suspicious data for review before training. |
| Distribution checks | Detect unusual shifts in labels, classes, sources, or tokens. |
| Known-good snapshots | Support safe retraining and rollback. |
| Promotion gates | Require evaluation before data/model promotion. |

### Engineer-ready requirement

```text
No user-generated feedback may be promoted into trusted training data without provenance, source trust metadata, and distribution-shift review.
```

## 4. Model evaluation controls

### Problems addressed

- Overreliance on average-case performance.
- Missing targeted failure modes.
- Backdoors that pass ordinary evaluation.
- Weak regression testing.

### Controls

| Control | Purpose |
|---|---|
| Adversarial holdout set | Test known attack patterns. |
| Sensitive-class tests | Ensure critical classes are not silently missed. |
| Trigger tests | Look for unexpected token/pattern behavior. |
| Robustness regression suite | Prevent known bypasses from returning. |
| Calibration tests | Check whether confidence is meaningful. |
| Segment evaluation | Measure performance across tenants, languages, regions, groups, and channels. |

### Engineer-ready requirement

```text
Model promotion must require passing a robustness regression suite that includes evasion, drift, and sensitive-class test cases relevant to the model's security role.
```

## 5. Decision and fallback controls

### Problems addressed

- Model output becoming an unsafe action.
- High-impact automation without human review.
- Confidently wrong decisions.
- Alert fatigue.

### Controls

| Control | Purpose |
|---|---|
| Policy outside the model | Keep enforcement deterministic. |
| Impact-aware thresholds | Treat high-impact decisions differently. |
| Human review gates | Escalate uncertain or high-risk cases. |
| Fail-safe defaults | Deny, delay, or escalate when the model is outside its safe operating range. |
| Dual controls | Combine model output with rules, identity, context, or approvals. |
| Action limits | Restrict what model decisions can cause automatically. |

### Engineer-ready requirement

```text
The model may recommend a decision, but high-impact actions must be mediated by a policy engine that considers confidence, impact, user context, and fallback rules.
```

## 6. Monitoring controls

### Problems addressed

- Drift.
- Evasion trends.
- Poisoned feedback.
- Model degradation.
- Attacker adaptation.

### Controls

| Signal | What it can reveal |
|---|---|
| Feature distribution shift | Inputs no longer match training assumptions. |
| Score distribution shift | Model boundary behavior is changing. |
| False positive/false negative reviews | Real-world failure modes. |
| User/source concentration | Coordinated abuse or poisoning. |
| Sensitive-class routing changes | Backdoor or model skewing. |
| Threshold override rates | Operators do not trust the model. |
| Appeal/report outcomes | Feedback quality and model harm. |

### Engineer-ready requirement

```text
Production monitoring must include drift, segment-level performance, sensitive-class errors, and abuse signals, with alert thresholds tied to operational response playbooks.
```

## 7. Recovery controls

### Problems addressed

- Bad model deployment.
- Poisoned retraining.
- Broken threshold change.
- Undetected drift.
- Incident response delays.

### Controls

| Control | Purpose |
|---|---|
| Model rollback | Return to known-good model quickly. |
| Data rollback | Remove suspect data from retraining pipeline. |
| Kill switch | Disable automation when model risk is high. |
| Shadow deployment | Compare new model behavior before full rollout. |
| Canary release | Limit blast radius. |
| Incident playbook | Define who acts when model behavior becomes unsafe. |

### Engineer-ready requirement

```text
Every model used in a security-relevant workflow must have a documented rollback path, owner, monitoring trigger, and manual fallback process.
```

## 8. Weak vs strong remediation examples

| Weak remediation | Strong remediation |
|---|---|
| Improve model accuracy. | Add adversarial test cases, segment evaluation, fallback rules, and monitoring tied to response. |
| Retrain the model. | Quarantine suspect data, retrain from known-good snapshot, evaluate against robustness suite, canary deploy, monitor. |
| Add more data. | Add trusted, provenance-tracked, representative data with poisoning checks and label review. |
| Increase the threshold. | Calibrate threshold by impact, false-negative cost, false-positive capacity, and review workflow. |
| Add a human in the loop. | Define when human review triggers, what evidence reviewers see, SLA, escalation, and override logging. |

## 9. Control validation checklist

A proposed fix should answer:

- What attack or failure mode does this control address?
- Where is it enforced?
- Is it deterministic or model-dependent?
- What telemetry proves it works?
- How is it tested before release?
- How is it monitored after release?
- What happens when it fails?
- Who owns it operationally?

## 10. Residual risk

Even after controls, residual risk remains.

A good residual risk statement says:

```text
The model may still be evaded by novel behavior. The proposed controls reduce impact by limiting automation for high-value borderline cases, adding adversarial regression tests, monitoring feature/score drift, and preserving rollback capability. Residual risk is acceptable only while review capacity remains sufficient and monitoring shows stable false-negative rates.
```

A weak residual risk statement says:

```text
Risk is low because the model is accurate.
```

Accuracy is evidence. It is not a complete risk argument.
