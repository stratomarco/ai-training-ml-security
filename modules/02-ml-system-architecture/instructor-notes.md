# Module 02 Instructor Notes  -  ML System Architecture

## Instructor goal

The goal of this module is to make students think in terms of **lifecycle and architecture**, not isolated model attacks.

By the end, students should understand that ML security can fail before the model is trained, while the model is served, or after the model is deployed through monitoring and feedback loops.

## Recommended timing

### 60-minute awareness version

| Time | Activity |
|---:|---|
| 0–5 min | Recap Module 01 and introduce the ML lifecycle |
| 5–20 min | Explain lifecycle stages |
| 20–35 min | Explain architecture-level attack paths |
| 35–50 min | Walk through LoanAssist as a class |
| 50–60 min | Key takeaways and discussion |

### 90-minute practitioner version

| Time | Activity |
|---:|---|
| 0–10 min | Recap Module 01 |
| 10–35 min | Teach slides 1–18 |
| 35–45 min | Break down LLM/RAG/agent extensions |
| 45–70 min | Group exercise: LoanAssist ML |
| 70–85 min | Group debrief |
| 85–90 min | Takeaways and quiz |

### 2.5–3 hour workshop version

| Time | Activity |
|---:|---|
| 0–15 min | Recap and framing |
| 15–55 min | Full slide walkthrough |
| 55–65 min | Break |
| 65–110 min | Group exercise: lifecycle DFD and trust boundaries |
| 110–140 min | Group exercise: attack paths and controls |
| 140–165 min | Presentations and debrief |
| 165–180 min | Quiz and closing discussion |

## Teaching setup

Before the session:

1. Review Module 01 terminology: assets, attackers, trust boundaries, abuse cases, controls, residual risk.
2. Prepare a whiteboard or shared diagramming surface.
3. Prepare the LoanAssist handout.
4. Decide whether students will work individually or in groups.
5. Remind students that the exercise is architectural, not mathematical.

## Opening script

Suggested opening:

> In Module 01, we said that the model is not the security boundary. In this module, we go one level deeper: the model is not even the whole system. Model behavior is created, deployed, observed, and changed through a lifecycle. If attackers can influence that lifecycle, they can influence the system.

## Common student misconceptions

### Misconception 1  -  “We are not training foundation models, so this does not apply.”

Response:

Even if an organization does not train a foundation model, it may still build ML behavior through prompts, retrieval, fine-tuning, adapters, embeddings, tool configuration, feedback, and monitoring. The lifecycle still exists.

### Misconception 2  -  “The dataset is internal, so it is trusted.”

Response:

Internal does not mean trusted. Ask who can write to it, import into it, label it, transform it, approve it, or use it for retraining.

### Misconception 3  -  “The model passed evaluation, so it is safe.”

Response:

Evaluation is only as good as the test set and threat model. A model can pass normal accuracy tests and still fail under poisoning, evasion, extraction, privacy leakage, or distribution shift.

### Misconception 4  -  “The API is authenticated, so model theft is not relevant.”

Response:

Authenticated users can still abuse access. Many extraction, probing, and privacy attacks happen through legitimate APIs.

### Misconception 5  -  “This is a data science problem, not a security problem.”

Response:

If changing the data changes production behavior, then data integrity, provenance, and access control are security problems.

## Key instructor prompts

Use these questions throughout the module:

- Where does this data come from?
- Who can modify it?
- What is treated as ground truth?
- What is the approval process before training?
- What is the approval process before deployment?
- Can we reproduce this model?
- Can we roll it back?
- Can a user influence future training?
- What does the model see at inference time?
- What can the model cause the system to do?
- What is logged, and who can access the logs?
- What would an incident look like?

## Exercise facilitation

The main exercise is [`exercise-ml-lifecycle-dfd.md`](exercise-ml-lifecycle-dfd.md).

### Group size

Best group size: 3–5 students.

### Expected exercise outputs

Each group should produce:

1. A lifecycle DFD.
2. Assets.
3. Trust boundaries.
4. Attack paths.
5. Controls.
6. Residual risk.

### What good answers include

Strong answers usually identify:

- Third-party data as a trust boundary.
- User-submitted application data as attacker-influenced.
- Support notes as semi-trusted data.
- Historical approval outcomes as sensitive training labels.
- Labeling and manual review as possible insider or process-risk points.
- Feature generation as a source of leakage and manipulation.
- Model artifact storage as a critical asset.
- Evaluation data as sensitive and contamination-prone.
- Inference API as a probing/extraction surface.
- Analyst explanations as overreliance risk.
- Vector database access as authorization-sensitive.
- Feedback and retraining as poisoning paths.

### If students get stuck

Ask them to place one attacker at each stage:

- External applicant
- Internal analyst
- Compromised vendor
- Malicious data supplier
- Compromised CI/CD account
- Curious employee
- Authenticated API user

Then ask what each one can influence.

## Suggested debrief structure

Use this order:

1. Ask each group for one trust boundary.
2. Ask each group for one asset.
3. Ask each group for one attack path.
4. Ask each group for one control.
5. Ask whether any control makes usability or velocity worse.
6. Ask what residual risk remains.

## Balance security, usability, and developer velocity

Push students away from impractical answers such as “review everything manually forever” or “disable feedback entirely.”

Better answers include:

- Risk-based approval gates.
- Sampling and quality review for labels.
- Automated validation plus human escalation.
- Model registry workflows that fit existing CI/CD.
- Secure defaults in shared ML platform tooling.
- Standardized logging and monitoring.
- Documented rollback path.
- Clear ownership for data, model, and application components.

## Instructor warning

Do not let this module become a lecture on ML algorithms.

The goal is not to explain gradient descent deeply. The goal is to explain which system components create security risk.

## Link to next module

Module 03 covers OWASP ML Security Top 10. Tell students:

> In the next module, we will name the specific ML attack categories. Today’s lifecycle map tells us where those attacks land.
