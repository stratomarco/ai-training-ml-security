# Exercise  -  OWASP ML Attack Review

## Purpose

Practice applying the OWASP Machine Learning Security Top 10 to a realistic ML system.

This is a tabletop exercise. It can be done individually or in small groups.

## Time

45–60 minutes.

## Student task

Choose one of the scenarios below and analyze it using the provided worksheet.

You do not need to produce code. The goal is to reason about the system, the attacker, the lifecycle stage, and the controls.

## Scenario options

### Scenario A  -  Spam and phishing classifier

A company uses an ML classifier to score inbound email as safe, suspicious, or malicious. The score influences whether the message is delivered, quarantined, or sent to security review.

### Scenario B  -  Fraud scoring model

A payments company uses an ML model to score card transactions. High-risk transactions may be declined or sent to manual review.

### Scenario C  -  Product recommender

An e-commerce platform uses user activity and reviews to recommend products. Recommended products receive more visibility and sales.

### Scenario D  -  Support-ticket classifier

An operations team uses an ML model to classify tickets by urgency and route them to the right team.

### Scenario E  -  Medical triage model

A healthcare organization uses an ML model to prioritize cases for additional review. The model does not make the final decision, but it influences queue priority.

## Worksheet

### 1. System and decision

- Which scenario did you choose?
- What decision does the model influence?
- Who relies on the decision?
- What happens if the decision is wrong?

### 2. Assets

Identify at least five assets.

Examples:

- Training data
- Labels
- Model artifact
- Feature pipeline
- Evaluation set
- Inference API
- Output score
- Business decision
- Logs
- Feedback data
- User/customer data

### 3. Attacker

- Who is the attacker?
- What is their goal?
- What can they directly control?
- What can they indirectly influence?
- What access do they have?

### 4. OWASP ML category

Choose one primary category:

- ML01 Input Manipulation
- ML02 Data Poisoning
- ML03 Model Inversion
- ML04 Membership Inference
- ML05 Model Theft
- ML06 AI Supply Chain Attacks
- ML07 Transfer Learning Attack
- ML08 Model Skewing
- ML09 Output Integrity Attack
- ML10 Model Poisoning

Also list any secondary categories.

### 5. Attack path

Describe the attack path in five to eight steps.

Keep it high-level and focused on the training scenario. Do not target real third-party systems.

Example structure:

```text
1. Attacker identifies model-dependent decision.
2. Attacker identifies input or lifecycle stage they can influence.
3. Attacker sends manipulated data or queries.
4. Model or pipeline processes attacker-controlled content.
5. Business decision changes in attacker's favor.
6. Monitoring fails to detect the pattern.
7. Impact occurs.
```

### 6. Impact

Describe impact in terms of:

- Confidentiality
- Integrity
- Availability
- Privacy
- Safety
- Financial impact
- Operational impact
- Trust/reputation

### 7. Controls

List controls in three groups.

| Control type | Examples |
|---|---|
| Preventive | Access control, provenance, validation, artifact signing, approval gates. |
| Detective | Monitoring, anomaly detection, drift detection, query abuse detection, audit logs. |
| Recovery | Rollback, retraining, incident response, dataset quarantine, key rotation. |

### 8. Residual risk

Answer:

- What risk remains after your controls?
- What would be too expensive or too slow to implement immediately?
- What risk should leadership explicitly accept or prioritize?

### 9. Engineering trade-offs

Discuss:

- Security vs usability
- Security vs model performance
- Security vs latency
- Security vs developer velocity
- Security vs operational cost

## Expected deliverable

A one-to-two-page ML attack summary and mitigation proposal.

## Evaluation rubric

| Criterion | Strong answer |
|---|---|
| Attacker clarity | Identifies a realistic attacker and what they control. |
| Lifecycle reasoning | Maps attack to a specific ML lifecycle stage. |
| OWASP mapping | Correctly maps primary and secondary categories. |
| Impact | Explains business and security impact clearly. |
| Mitigation | Includes preventive, detective, and recovery controls. |
| Residual risk | Explains what remains unresolved. |
| Trade-offs | Balances security with usability and delivery speed. |
