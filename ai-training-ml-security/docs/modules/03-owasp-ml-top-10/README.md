# Module 03 — OWASP ML Security Top 10

## Purpose

Introduce the OWASP Machine Learning Security Top 10 as a practical map of classical ML attack categories.

This module deliberately comes before the LLM, RAG, and agent modules. Students should understand that machine learning systems had security problems before chatbots and agents became popular. Poisoning, evasion, inversion, membership inference, model theft, and supply chain compromise all apply to non-LLM systems such as fraud detection, spam filtering, credit scoring, intrusion detection, medical triage, recommender systems, and computer vision.

## Key message

Traditional ML systems have security risks even when no LLM is involved.

The model is not only a statistical component. In production, it becomes part of a security-sensitive decision system. If an attacker can influence the model's inputs, training data, outputs, artifacts, dependencies, or feedback loops, they may influence the business decision that depends on the model.

## Learning objectives

By the end of this module, students should be able to:

1. Explain the OWASP ML Security Top 10 categories at a practitioner level.
2. Distinguish evasion, poisoning, privacy attacks, model theft, supply chain attacks, and output integrity failures.
3. Connect each ML risk to classic software security principles.
4. Identify where each attack appears in the ML lifecycle.
5. Explain why model accuracy is not the same as model security.
6. Design basic mitigations for each risk category.
7. Write an ML attack summary and mitigation proposal.
8. Discuss residual risk honestly, especially where mitigations reduce but do not eliminate the attack class.

## Prerequisites

Students should already understand:

- Basic ML lifecycle concepts from Module 02.
- The difference between training and inference.
- Basic application security concepts such as input validation, access control, logging, supply chain risk, and defense in depth.
- Why threat modeling requires assets, trust boundaries, attackers, and abuse cases.

## Topics

This module covers the OWASP Machine Learning Security Top 10 categories:

| OWASP category | Short description |
|---|---|
| ML01 — Input Manipulation Attack | Attacker changes inference-time input to manipulate prediction. |
| ML02 — Data Poisoning Attack | Attacker corrupts training or feedback data. |
| ML03 — Model Inversion Attack | Attacker infers sensitive training features or representative samples from model behavior. |
| ML04 — Membership Inference Attack | Attacker determines whether a specific record was used in training. |
| ML05 — Model Theft | Attacker steals, extracts, or approximates a model. |
| ML06 — AI Supply Chain Attacks | Attacker compromises datasets, dependencies, model artifacts, registries, or pipelines. |
| ML07 — Transfer Learning Attack | Attacker abuses inherited behavior, backdoors, or weaknesses from pretrained/fine-tuned models. |
| ML08 — Model Skewing | Attacker manipulates production feedback or input distribution to degrade or bias behavior. |
| ML09 — Output Integrity Attack | Attacker tampers with model outputs, post-processing, interpretation, or downstream decisions. |
| ML10 — Model Poisoning | Attacker manipulates the model artifact, training process, or learned behavior directly. |

## Security engineering connection

The OWASP ML risks are not disconnected from traditional security. Most are familiar principles applied to ML assets:

| Classic security concept | ML-specific expression |
|---|---|
| Input validation | Validate and normalize inference inputs; detect out-of-distribution cases. |
| Data integrity | Protect training, labeling, and feedback data from tampering. |
| Access control | Limit who can query models, export artifacts, access datasets, or push model versions. |
| Privacy by design | Reduce leakage through outputs, confidence scores, embeddings, logs, and APIs. |
| Supply chain security | Verify datasets, dependencies, containers, model files, and registries. |
| Least privilege | Give training jobs, notebooks, and inference services only the access they need. |
| Complete mediation | Enforce authorization at every data/model/tool boundary, not only at the UI. |
| Auditability | Log model artifact changes, data ingestion, training runs, privileged queries, and anomalous behavior. |
| Defense in depth | Combine validation, rate limits, monitoring, review, artifact signing, and rollback. |
| Secure failure | Define safe fallback behavior when confidence, provenance, or input quality is poor. |

## Reference architecture

```text
external user / attacker
   |
   v
application / API
   |
   +-- authn / authz
   +-- input validation
   +-- inference service
   |     |
   |     +-- model artifact
   |     +-- feature pipeline
   |     +-- post-processing logic
   |
   +-- model output / decision
   |
   +-- logs and monitoring

training side:

raw data sources
   |
   +-- data ingestion
   +-- labeling / enrichment
   +-- feature engineering
   +-- training pipeline
   +-- evaluation
   +-- model registry
   +-- deployment
   +-- feedback loop back into data
```

## Attack surface by lifecycle stage

| Stage | Example risks |
|---|---|
| Data collection | Poisoned data, biased sampling, untrusted sources, PII exposure. |
| Labeling | Label manipulation, insider abuse, weak review, outsourced labeling risk. |
| Feature engineering | Feature leakage, manipulation, fragile assumptions, hidden dependencies. |
| Training | Poisoning, malicious code, compromised dependencies, weak reproducibility. |
| Evaluation | Test set leakage, weak adversarial testing, misleading metrics. |
| Registry | Model theft, artifact tampering, weak access control. |
| Deployment | Unsafe deserialization, secrets exposure, overprivileged runtime. |
| Inference | Evasion, extraction, privacy probing, DoS, output tampering. |
| Monitoring | Missing drift detection, weak abuse detection, incomplete logs. |
| Feedback loop | Model skewing, delayed poisoning, reinforcement of attacker-influenced behavior. |

## Lab

The module includes a custom tabletop and toy-model lab:

- **Exercise:** `exercise-owasp-ml-attack-review.md`
- **Lab guide:** `labs/toy-ml-attacks/classical-ml-attack-lab.md`

The lab avoids targeting real third-party systems. It uses toy scenarios such as spam detection, fraud scoring, or image classification to teach the concepts safely.

## Student deliverable

Students produce an **ML attack summary and mitigation proposal** containing:

1. Selected system and business decision.
2. Asset at risk.
3. Relevant OWASP ML category.
4. Attack path.
5. Impact.
6. Detection opportunities.
7. Mitigations.
8. Residual risk.
9. Engineering trade-offs.

## Instructor guidance

Do not teach the OWASP ML Top 10 as a list to memorize. Teach it as a map of where adversaries can influence the ML lifecycle.

A strong student answer should explain:

- What the attacker controls.
- What the model controls.
- What business process depends on the model.
- What assumption fails.
- Which security control should exist outside the model.

## Discussion questions

1. Why is high model accuracy not enough to claim a model is secure?
2. Which risks are primarily data integrity problems?
3. Which risks are primarily privacy problems?
4. Which risks are primarily supply chain problems?
5. Which risks are primarily access-control problems?
6. Where should the system fail closed?
7. Which mitigations are practical for a small engineering team?
8. Which mitigations add too much friction or cost for the risk?

## Suggested duration

| Section | Time |
|---|---:|
| Recap Module 02 | 10 min |
| OWASP ML Top 10 overview | 35 min |
| Lifecycle mapping | 20 min |
| Attack scenarios | 30 min |
| Lab / tabletop | 45–60 min |
| Mitigation design | 25 min |
| Discussion and review | 20 min |

Total: 2.5–3 hours depending on lab depth.
