# Module 10 Slides — Adversarial ML and Robustness

## Slide 1 — Title

# Adversarial ML and Robustness

Testing models under adversarial pressure.

---

## Slide 2 — Why this module matters

A model can perform well on a test set and still fail in production.

Reasons include:

- attackers adapt;
- inputs change;
- data distribution shifts;
- feedback loops distort behavior;
- training data is manipulated;
- rare edge cases matter;
- confidence scores are misunderstood;
- model outputs trigger real actions.

---

## Slide 3 — Core thesis

# Accuracy is not the same as security.

A useful security review asks:

- What can the model get wrong?
- Who benefits if it gets that wrong?
- Can an attacker shape the input?
- Can an attacker shape the training data?
- What happens after the model makes the decision?

---

## Slide 4 — Classic security connection

Adversarial ML is not separate from security engineering.

| Classic concept | ML version |
|---|---|
| Malicious input | Adversarial example or manipulated feature vector |
| Supply chain compromise | Poisoned dataset, model, dependency, or feedback loop |
| Fail-safe defaults | Safe fallback when model confidence is low |
| Defense in depth | Policy layer, monitoring, human review, and rollback |
| Incident response | Quarantine data, roll back model, retrain safely |

---

## Slide 5 — Model lifecycle attack points

```text
data -> labeling -> training -> evaluation -> registry -> deployment -> inference -> monitoring -> feedback
```

Attackers may influence:

- data collection;
- labels;
- features;
- training jobs;
- model artifacts;
- inference inputs;
- feedback and retraining;
- monitoring blind spots.

---

## Slide 6 — Evasion

Evasion happens when an attacker changes input to avoid detection or trigger a desired output.

Examples:

- phishing text rewritten to avoid a classifier;
- malware features changed without changing malicious behavior;
- spam content obfuscated;
- image inputs manipulated;
- content-policy terms encoded or disguised.

---

## Slide 7 — Evasion root cause

The model learned patterns from historical examples.

The attacker searches for inputs that:

- preserve attacker intent;
- change model features;
- fall outside tested assumptions;
- exploit preprocessing gaps;
- cause the model to be confidently wrong.

---

## Slide 8 — Poisoning

Poisoning happens when an attacker influences training data, labels, feedback, or retraining.

Possible goals:

- reduce overall model quality;
- create targeted misclassification;
- bias future behavior;
- create a backdoor;
- corrupt evaluation or monitoring.

---

## Slide 9 — Backdoors

A backdoor is targeted behavior that appears only when a trigger is present.

The model may behave normally most of the time.

That is why backdoors can survive ordinary validation.

Security question:

> Did evaluation test for targeted, trigger-based behavior?

---

## Slide 10 — Model skewing and feedback loops

Feedback can improve a system.

Feedback can also poison it.

Risky patterns:

- user feedback becomes training data without review;
- attacker generates many examples;
- abuse traffic dominates labels;
- production behavior changes the future dataset;
- retraining lacks rollback or quarantine.

---

## Slide 11 — Distribution shift and drift

Not every failure is caused by an attacker.

Models can fail because the world changed.

Examples:

- new fraud pattern;
- new slang or language;
- new user population;
- changed product workflow;
- new sensor or data source;
- seasonal behavior.

Security cares because attackers can exploit drift.

---

## Slide 12 — Confidence is not enough

A confidence score is not a security guarantee.

Ask:

- Is it calibrated?
- Was it tested under adversarial inputs?
- What happens below threshold?
- What happens above threshold?
- What are the costs of false positives and false negatives?

---

## Slide 13 — Robustness testing

Robustness testing asks:

- How does the model behave under perturbation?
- How does it behave under adversarial input?
- How does it behave on edge cases?
- How does it behave on new data distributions?
- How does it fail?
- Are failures safe?

---

## Slide 14 — Practical test categories

| Category | Example |
|---|---|
| Input perturbation | Small wording, formatting, or feature changes |
| Boundary testing | Inputs near decision thresholds |
| Semantic preservation | Same meaning, different representation |
| Poisoning tabletop | Review data and label control paths |
| Backdoor review | Search for trigger-based assumptions |
| Drift simulation | Evaluate against new or shifted data |
| Fallback testing | Verify safe behavior on uncertainty |

---

## Slide 15 — Defense patterns

Useful controls include:

- input normalization;
- data validation;
- feature sanity checks;
- provenance tracking;
- label review;
- adversarial evaluation;
- model monitoring;
- drift detection;
- human review for high-risk cases;
- policy outside the model;
- model rollback;
- secure retraining.

---

## Slide 16 — Do not over-trust the model

A model should rarely be the only security control.

For high-impact decisions, combine:

```text
model signal + deterministic policy + human review + monitoring + rollback
```

---

## Slide 17 — Recovery matters

Assume a model will eventually fail.

Prepare to:

- pause model-driven actions;
- increase human review;
- quarantine suspected data;
- roll back to a previous model;
- retrain from trusted data;
- communicate impact;
- update tests and monitoring.

---

## Slide 18 — Student exercise

Design an adversarial test plan for a phishing classifier.

Include:

- attacker goals;
- model assumptions;
- evasion tests;
- poisoning risks;
- drift tests;
- fallback behavior;
- monitoring;
- mitigations;
- residual risk.

---

## Slide 19 — Leadership framing

Avoid saying:

> The model is robust.

Say:

> We tested these adversarial conditions, identified these failure modes, added these controls, and this residual risk remains.

---

## Slide 20 — Takeaways

- Accuracy is not security.
- Evasion targets inference-time behavior.
- Poisoning targets training, feedback, or retraining.
- Backdoors can be targeted and hard to detect.
- Drift can be non-malicious but still exploitable.
- Robustness requires testing, monitoring, fallback, and recovery.
