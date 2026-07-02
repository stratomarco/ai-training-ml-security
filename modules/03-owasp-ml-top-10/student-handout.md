# Module 03  -  Student Handout

## Main idea

The OWASP ML Security Top 10 is a map of common ways machine learning systems can be attacked.

The most important thing to remember:

> Machine learning security is not only about the model. It is about the full lifecycle: data, labels, features, training, evaluation, artifacts, deployment, inference, monitoring, feedback, and business decisions.

## The ten categories

| Category | Meaning | Main security concern |
|---|---|---|
| ML01  -  Input Manipulation | The attacker changes inference-time input to alter prediction. | Robustness and input handling. |
| ML02  -  Data Poisoning | The attacker corrupts data used for training or feedback. | Data integrity. |
| ML03  -  Model Inversion | The attacker infers sensitive features or representative training data. | Privacy leakage. |
| ML04  -  Membership Inference | The attacker determines whether a record was in training. | Privacy leakage. |
| ML05  -  Model Theft | The attacker steals or approximates the model. | IP, access control, API abuse. |
| ML06  -  AI Supply Chain | The attacker compromises datasets, dependencies, artifacts, or pipelines. | Supply chain integrity. |
| ML07  -  Transfer Learning | The attacker abuses inherited risk from pretrained or reused models. | Third-party and inherited behavior risk. |
| ML08  -  Model Skewing | The attacker manipulates feedback or distribution over time. | Feedback-loop integrity. |
| ML09  -  Output Integrity | The attacker tampers with output, thresholds, or downstream decision logic. | Decision integrity. |
| ML10  -  Model Poisoning | The attacker corrupts model behavior or the artifact directly. | Artifact and training integrity. |

## Lifecycle mapping

```text
Data → Labels → Features → Training → Evaluation → Registry → Deployment → Inference → Monitoring → Feedback
```

| Lifecycle stage | Relevant questions |
|---|---|
| Data | Where did the data come from? Can it be poisoned? Is it sensitive? |
| Labels | Who labels data? Can labels be manipulated? Is there review? |
| Features | Do features leak sensitive information? Can they be gamed? |
| Training | Who can run training? Are dependencies trusted? Are runs reproducible? |
| Evaluation | Does testing include adversarial and abuse cases? |
| Registry | Who can publish, replace, download, or deploy a model? |
| Deployment | Is the runtime isolated? Are secrets protected? |
| Inference | Can attackers manipulate inputs or query the model repeatedly? |
| Monitoring | Can we detect drift, abuse, extraction, or sudden behavior change? |
| Feedback | Can attackers influence future training through feedback? |

## How to analyze an ML attack

Use this structure:

1. What decision does the model influence?
2. What asset is at risk?
3. Who is the attacker?
4. What can the attacker control?
5. Where is the trust boundary?
6. Which OWASP ML category applies?
7. What is the attack path?
8. What is the business impact?
9. What can detect it?
10. What can prevent or reduce it?
11. What is the residual risk?

## Example: spam classifier

| Question | Example answer |
|---|---|
| Decision | Block or allow an email. |
| Attacker | Phisher. |
| Attacker control | Email content, sender infrastructure, timing. |
| OWASP category | ML01 input manipulation. |
| Attack path | Modify wording and structure until classifier allows the message. |
| Impact | Phishing reaches users. |
| Detection | Similarity clustering, user reports, suspicious sender patterns. |
| Mitigation | Input normalization, adversarial test cases, sender reputation, sandboxing, user warnings. |
| Residual risk | Some malicious emails will still pass. Human reporting and layered controls are still needed. |

## Key takeaways

- Accuracy is not security.
- Training data is part of the attack surface.
- Model outputs can leak private information.
- Query access can become an extraction channel.
- Feedback loops can be manipulated.
- Model artifacts need integrity controls.
- ML security requires prevention, detection, response, and recovery.

## Useful mental model

```text
Classic security question:
Can the attacker control this input?

ML security version:
Can the attacker control this input, training signal, model artifact, feedback loop, or model-dependent decision?
```
