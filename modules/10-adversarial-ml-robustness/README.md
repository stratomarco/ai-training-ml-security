# Module 10  -  Adversarial ML and Robustness

## Purpose

Teach adversarial ML as practical system robustness, not only academic math.

This module helps students understand how models can be reliable under normal validation conditions and still fail under adversarial pressure, distribution shift, data manipulation, backdoors, or abuse patterns.

## Key message

A model can be statistically accurate and still be insecure.

Security review must ask not only "how accurate is the model?" but also:

- accurate for whom;
- accurate under what assumptions;
- accurate against which attacker;
- accurate after which data changes;
- accurate with which fallback behavior;
- safe enough for which business decision.

## Learning objectives

By the end of this module, students should be able to:

1. Explain evasion, poisoning, backdoors, model skewing, distribution shift, drift, and robustness testing.
2. Distinguish ordinary model error from adversarial failure.
3. Map adversarial ML risks to lifecycle stages: training, evaluation, deployment, inference, monitoring, and feedback.
4. Explain why benchmark accuracy is not a security guarantee.
5. Design an adversarial test plan for a classifier, ranking model, content filter, fraud model, phishing detector, or AI decision-support system.
6. Identify controls for input validation, data provenance, training data quality, model evaluation, fallback, monitoring, and incident response.
7. Explain residual risk when a model remains useful but not reliable enough for autonomous security decisions.
8. Communicate robustness findings to engineering and leadership without overstating certainty.


## Reading-first additions

Module 10 now includes a deeper reading path for students who need conceptual understanding before running or designing tests:

- [Deep Dive](deep-dive.md)  -  explains adversarial ML as production security engineering, not only academic perturbation research.
- [Attack Anatomy](attack-anatomy.md)  -  breaks evasion, poisoning, backdoors, model skewing, and drift into attack paths.
- [Controls and Remediations](controls-and-remediations.md)  -  turns robustness risks into engineer-ready controls.
- [Common Mistakes](common-mistakes.md)  -  highlights weak reasoning patterns, such as equating accuracy with security.
- [Worked Example](worked-example.md)  -  shows a fraud-classifier robustness review from attacker goal to remediation validation.

The lab and tabletop exercises should reinforce these readings. They should not replace them.

## Topics

- Adversarial ML as system robustness
- Evasion attacks
- Data poisoning
- Backdoors and trigger-based behavior
- Model poisoning
- Model skewing
- Distribution shift
- Concept drift
- Confidence and calibration
- Fallback behavior
- Robustness testing
- Abuse monitoring
- Human review and escalation
- Secure retraining
- Feedback-loop integrity
- Safety margins for high-impact decisions

## Security engineering connection

Adversarial ML connects directly to classic security engineering:

| Security idea | ML robustness equivalent |
|---|---|
| Input validation | Normalize, constrain, and inspect model inputs. |
| Defense in depth | Do not rely on one model decision as the only control. |
| Fail-safe defaults | Define safe fallback behavior when confidence or quality is low. |
| Complete mediation | Enforce policy outside the model for high-impact actions. |
| Least privilege | Limit what a model decision can cause automatically. |
| Secure supply chain | Protect data, labels, models, features, and retraining jobs. |
| Monitoring and response | Detect drift, abuse, poisoning signals, and unexpected outputs. |
| Secure recovery | Roll back models, quarantine data, and retrain safely. |

## Reference architecture

```text
external input
  |
  v
pre-processing and normalization
  |
  v
model inference service
  |
  +-- confidence and calibration checks
  +-- policy and business-rule layer
  +-- fallback / human-review queue
  +-- monitoring and drift detection
  +-- abuse detection
  +-- feedback and retraining pipeline
```

## Common scenarios

| System | Adversarial pressure |
|---|---|
| Spam or phishing classifier | Attacker rewrites content to bypass detection. |
| Fraud model | Attacker changes transaction behavior to avoid rules and model signals. |
| Malware classifier | Attacker manipulates features without changing malicious behavior. |
| Content moderation model | Attacker uses obfuscation, encoding, or wording changes. |
| Image classifier | Attacker modifies visual input or physical environment. |
| RAG ranking model | Attacker manipulates document content to rank higher or mislead retrieval. |
| AI support triage | Attacker causes harmful misclassification or priority manipulation. |

## Lab

Use the labs in [`../../labs/adversarial-ml-labs/`](../../labs/adversarial-ml-labs/README.md):

1. **Evasion and robustness lab**  -  bypass a toy classifier using controlled input changes, then design mitigations.
2. **Poisoning and backdoor tabletop**  -  review how training data and feedback loops can introduce targeted model failures.

## Deliverable

Students produce an **adversarial test plan** that includes:

- system scope;
- model role;
- assets and security properties;
- attacker goals;
- test cases;
- expected failure modes;
- monitoring signals;
- mitigation plan;
- fallback behavior;
- residual risk statement.

## Discussion questions

1. What does the model decide, and what does that decision cause?
2. What assumptions were true during evaluation but may fail in production?
3. Can an attacker control or influence input data?
4. Can an attacker control or influence training data, labels, feedback, or retraining?
5. What happens when the model is uncertain?
6. What happens when the model is confidently wrong?
7. Which decisions must be checked by policy outside the model?
8. What would you monitor for evasion, drift, poisoning, or abuse?
9. How would you recover from a poisoned model or bad retraining run?
10. What residual risk remains after practical controls?

## Instructor note

Do not let this module become only a mathematical adversarial examples lecture.

The practical goal is to teach students how to test and design production systems that remain safe when model assumptions are attacked or invalidated.
