# Module 10 Student Handout  -  Adversarial ML and Robustness

## Core idea

A model can be accurate and still insecure.

Security review asks how the system behaves when:

- inputs are malicious;
- data changes;
- attackers adapt;
- training data is manipulated;
- feedback loops are abused;
- the model is uncertain;
- the model is confidently wrong.

## Key terms

| Term | Meaning |
|---|---|
| Evasion | Manipulating inference-time input to cause a desired model output. |
| Poisoning | Manipulating training data, labels, feedback, or retraining to corrupt model behavior. |
| Backdoor | Hidden behavior that activates only when a trigger or condition is present. |
| Model skewing | Manipulating data or behavior so the model learns or reinforces a biased pattern. |
| Distribution shift | Production data differs from training or evaluation data. |
| Concept drift | The relationship between features and labels changes over time. |
| Robustness testing | Testing behavior under perturbation, adversarial examples, edge cases, and shifted data. |
| Calibration | Whether model confidence corresponds to real-world likelihood. |
| Fallback behavior | What the system does when the model is uncertain, unavailable, or suspected to be wrong. |

## What to look for

When reviewing a model-backed system, ask:

1. What decision does the model make?
2. What action follows that decision?
3. Who benefits if the model is wrong?
4. Can the attacker control input?
5. Can the attacker influence training data or feedback?
6. What assumptions does the evaluation rely on?
7. Are confidence thresholds tested and calibrated?
8. What happens when the model is uncertain?
9. What happens when the model is confidently wrong?
10. How can the team roll back, retrain, or pause model-driven actions?

## Evasion example

A phishing classifier marks a message as safe.

The attacker changes the message:

- same malicious goal;
- different wording;
- less suspicious terms;
- extra benign-looking text;
- altered formatting;
- changed URL representation.

If the model now marks it as safe, the system has an evasion weakness.

## Poisoning example

A support triage model learns from user feedback.

An attacker submits many cases and feedback examples so future abuse cases are classified as normal.

The problem is not only the model. The problem is the data and feedback pipeline.

## Backdoor example

A model behaves normally unless a specific trigger appears.

The trigger could be a phrase, pattern, metadata value, image mark, source, or feature combination.

Backdoors are dangerous because ordinary test sets may not include the trigger.

## Robustness controls

| Control | Purpose |
|---|---|
| Input normalization | Reduce easy representation tricks. |
| Feature sanity checks | Detect impossible or suspicious combinations. |
| Data provenance | Know where training and feedback data came from. |
| Label review | Reduce poisoning and label manipulation. |
| Adversarial test cases | Test beyond ordinary validation. |
| Drift monitoring | Detect changing production data. |
| Confidence calibration | Avoid over-trusting scores. |
| Human review | Escalate high-impact uncertain cases. |
| Policy outside model | Prevent model output from becoming final authority. |
| Rollback and quarantine | Recover from bad models or poisoned data. |

## Deliverable checklist

Your adversarial test plan should include:

- system and model scope;
- protected assets;
- attacker goals;
- attacker control points;
- evasion tests;
- poisoning tests or tabletop scenarios;
- backdoor assumptions;
- drift scenarios;
- fallback behavior;
- monitoring signals;
- mitigation plan;
- residual risk.

## Self-study reading path

Before attempting the adversarial test plan exercise, read the new Module 10 reading-first pages in this order:

1. `deep-dive.md`  -  understand why accuracy is not security assurance.
2. `attack-anatomy.md`  -  learn how attacker influence becomes system impact.
3. `controls-and-remediations.md`  -  map failures to implementable controls.
4. `common-mistakes.md`  -  avoid vague or non-actionable findings.
5. `worked-example.md`  -  study the fraud-classifier review pattern and reuse the structure for your own system.

When writing your exercise response, do not stop at “the model can be fooled.” Explain the attacker goal, what they can influence, what decision changes, what impact follows, what control should be implemented, and how the fix should be validated.

## Minimum deliverable quality

A strong Module 10 deliverable includes:

- model purpose and business/security decision;
- attacker goal and attacker-controlled inputs;
- evasion, poisoning, backdoor, or drift scenario;
- specific test cases;
- concrete controls;
- monitoring and fallback design;
- fix validation method;
- residual risk statement.

A weak deliverable only says that adversarial examples exist or that the model should be retrained.
