# Common Mistakes — Adversarial ML and Robustness

This page lists common mistakes students, engineers, and security teams make when reviewing ML robustness.

## 1. Treating adversarial ML as only image perturbations

Image perturbations are useful teaching examples, but many production attacks are feature, text, behavior, data, label, or feedback attacks.

Better framing:

> What can the attacker influence, and how does that influence change a model-driven decision?

## 2. Equating accuracy with security

A model can have strong average-case accuracy and still fail under adaptive attack or distribution shift.

Ask:

- Does evaluation include attacker behavior?
- Does evaluation include high-impact edge cases?
- Does evaluation include drift scenarios?
- Does evaluation include segment-level performance?

## 3. Ignoring the action after the prediction

The risk of a model decision depends on what the system does with it.

A wrong label in a dashboard is one thing. A wrong label that automatically approves payment, closes a case, blocks a user, or suppresses an alert is much more serious.

Always ask:

```text
Model output -> system action -> impact
```

## 4. Relying on the model as the only control

Bad pattern:

```text
The model says safe, so allow the action.
```

Better pattern:

```text
The model says low risk, but the policy layer also checks action impact, identity, thresholds, confidence, and fallback rules.
```

## 5. Treating poisoning as only a training-time issue

Poisoning can happen through:

- raw data collection;
- labels;
- user feedback;
- analyst decisions;
- retraining data;
- feature stores;
- synthetic data;
- model distillation;
- imported datasets;
- third-party model artifacts.

Feedback loops deserve special attention because they can make poisoning continuous.

## 6. Forgetting backdoors can pass normal tests

Backdoors are targeted. Standard test sets may not include the trigger.

Add tests for:

- unusual token-label correlations;
- trigger-like phrases;
- rare patterns;
- sensitive-class behavior;
- unexpected routing changes;
- performance on targeted examples.

## 7. Ignoring false positives as a security issue

False positives can create operational harm:

- alert fatigue;
- analyst overload;
- users learning to ignore warnings;
- business teams bypassing controls;
- legitimate users being blocked;
- attackers hiding in noise.

False positives are not only a UX problem. They can weaken the security system.

## 8. Failing to define fallback behavior

If the model is uncertain, out-of-distribution, degraded, or unavailable, the system still needs a safe behavior.

Bad fallback:

```text
If model fails, allow by default.
```

Better fallback:

```text
If model confidence is low for a high-impact decision, require review or conservative handling.
```

## 9. Not testing attacker adaptation

Attackers adapt. A one-time evaluation is not enough.

Include:

- known bypass variants;
- paraphrases;
- feature manipulation;
- repeated probing scenarios;
- realistic attacker incentives;
- tests from recent incidents.

## 10. No owner for monitoring and recovery

Robustness is operational. A model owner, security owner, and business owner must know what happens when metrics degrade.

Missing ownership leads to:

- stale thresholds;
- ignored drift;
- unclear rollback authority;
- broken incident response;
- delayed remediation.

## 11. Treating retraining as an automatic fix

Retraining can fix some issues, but it can also amplify bad data.

Before retraining:

- identify root cause;
- quarantine suspect data;
- review labels;
- compare distributions;
- evaluate against adversarial holdouts;
- preserve rollback.

## 12. Writing vague findings

Weak finding:

```text
The model is vulnerable to adversarial examples.
```

Strong finding:

```text
The fraud model can be evaded by splitting a high-value transaction into repeated lower-value transactions with short delays. The model score drops below the approval threshold while the business goal remains fraudulent purchase completion. Add multi-window velocity features, high-value review gates, probing detection, and regression tests for transaction-splitting patterns.
```

Security reports should be specific enough for engineering action.
