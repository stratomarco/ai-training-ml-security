# Module 10 Instructor Notes — Adversarial ML and Robustness

## Teaching intent

This module should make students stop treating a model evaluation report as a security report.

The module connects adversarial ML to real production concerns:

- What can attackers influence?
- What does the model decision cause?
- What happens when the model is wrong?
- How do we test beyond the average case?
- How do we monitor and recover?

## Suggested timing

For a 90-minute session:

| Time | Activity |
|---|---|
| 0–10 min | Accuracy vs security framing |
| 10–25 min | Evasion and inference-time attacks |
| 25–40 min | Poisoning, backdoors, and feedback loops |
| 40–55 min | Drift, confidence, fallback, and monitoring |
| 55–80 min | Exercise: adversarial test plan for a classifier |
| 80–90 min | Group discussion and residual risk |

For a 2-hour session, run both the evasion lab and the poisoning/backdoor tabletop.

## Instructor framing

Open with:

> The test set tells us how the model behaved against yesterday's expected examples. Security asks how it behaves when someone tries to make it fail tomorrow.

Then anchor the discussion in classic security:

- malicious input;
- supply chain integrity;
- defense in depth;
- fail-safe defaults;
- monitoring;
- recovery.

## Concepts to emphasize

### Evasion

Evasion is an inference-time problem. The attacker manipulates the input while preserving their goal.

Examples:

- changing phishing wording;
- adding benign-looking text;
- obfuscating malicious terms;
- changing feature values;
- manipulating image or sensor input;
- bypassing a moderation or fraud model.

### Poisoning

Poisoning is a training, labeling, data collection, feedback, or retraining problem.

Students should see poisoning as a supply chain problem for data and labels.

### Backdoors

Backdoors are difficult because the model can look normal under ordinary testing.

The instructor should ask:

- What trigger would matter?
- Who can introduce it?
- Was it represented in evaluation?
- What monitoring would detect targeted failures?

### Drift

Drift is not always malicious. But it still creates security exposure when controls assume the model still works.

### Confidence and calibration

Confidence scores often create false comfort. Students should separate model confidence from business certainty and security assurance.

## Common student mistakes

| Mistake | How to redirect |
|---|---|
| Treating adversarial ML as only image perturbations | Use phishing, fraud, spam, RAG ranking, and security triage examples. |
| Focusing only on attacks | Ask how to test, monitor, and recover. |
| Assuming higher accuracy solves the issue | Ask what happens under adaptive attacker behavior. |
| Trusting thresholds blindly | Ask whether thresholds are calibrated and tested under attack. |
| Ignoring feedback loops | Ask who can influence future training data. |
| Treating drift as only an ML quality issue | Ask whether attackers can exploit drift or monitoring gaps. |

## Exercise guidance

For the adversarial test plan exercise, students should produce something practical, not academic.

A strong answer includes:

- clear scope;
- asset and model role;
- attacker goals;
- evasion test cases;
- poisoning and feedback-loop risks;
- drift scenarios;
- fallback behavior;
- monitoring signals;
- mitigation plan;
- residual risk statement.

## Discussion prompts

Use these prompts if conversation slows down:

1. If the model says “low risk,” what system action follows?
2. Who can benefit from a false negative?
3. Who can benefit from a false positive?
4. Can the attacker submit many examples?
5. Can user feedback become training data?
6. Is model rollback possible?
7. What would trigger emergency human review?
8. What would be logged as evidence?

## Instructor warning

Do not teach students that robustness can be “solved” once.

The practical message is that robustness is an ongoing engineering process:

```text
test -> deploy -> monitor -> detect -> respond -> retrain -> re-test
```


## Reading-first delivery sequence

For this module, do not start with abstract adversarial ML terminology. Start with a production decision and ask what happens when the model is wrong under pressure.

Recommended sequence:

1. Use `deep-dive.md` to frame accuracy as evidence, not assurance.
2. Use `attack-anatomy.md` to connect attacker influence to system impact.
3. Use `worked-example.md` to show what a strong finding looks like.
4. Use `controls-and-remediations.md` to force concrete remediation design.
5. Use the exercise to make students create their own adversarial test plan.

If time is short, teach the fraud-classifier worked example and one backdoor example. If time allows, split students into groups and assign different systems: phishing classifier, login risk model, moderation model, support-ticket routing model, or RAG ranking system.

## Grading emphasis

Reward students for:

- explaining attacker influence;
- connecting model behavior to business/security impact;
- designing concrete tests;
- proposing controls outside the model;
- defining fallback and monitoring;
- writing a fix validation plan.

Do not reward vague answers that only say “improve accuracy,” “retrain the model,” or “add more data” without explaining provenance, evaluation, monitoring, and recovery.
