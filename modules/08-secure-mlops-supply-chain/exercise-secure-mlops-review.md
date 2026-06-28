# Exercise — Secure MLOps and AI Supply Chain Review

## Scenario

You are reviewing a new internal ML pipeline called **TriageRanker**.

TriageRanker predicts the priority of incoming engineering incidents and recommends routing to the correct team. It is not customer-facing, but its output affects operational response time and may influence whether incidents are escalated.

The team wants to deploy the first version quickly.

## Current architecture

```text
public issue dataset
  + exported historical company tickets
  + manually labeled spreadsheet
  |
  v
research notebook
  |
  +-- pip install from public package indexes
  +-- reads data from shared cloud bucket
  +-- trains model on GPU workstation
  +-- exports model.pkl
  |
  v
shared artifact bucket
  |
  v
model registry
  |
  v
CI/CD deployment to internal inference API
  |
  v
incident triage application
  |
  v
operator feedback stored for retraining
```

## Known implementation details

The team tells you:

1. The public issue dataset was downloaded from a community forum.
2. Historical company tickets include internal incident notes.
3. The manually labeled spreadsheet is editable by the whole team.
4. The notebook contains exploratory cells, shell commands, and old outputs.
5. One cell contains a commented API key from a previous experiment.
6. Dependencies are installed with `pip install -r requirements.txt`, but versions are not pinned.
7. The training job runs under a shared service account.
8. The output artifact is `model.pkl`.
9. The model artifact is copied to a shared bucket.
10. The registry allows ML engineers to register and promote models.
11. Deployment happens automatically when a model is marked `production`.
12. Evaluation only checks accuracy on a random validation split.
13. There is no adversarial, privacy, or abuse-case evaluation.
14. Operator feedback is stored and used in future retraining.
15. There is no documented rollback process.

## Student tasks

### Task 1 — Identify assets and artifacts

List all security-relevant assets and artifacts.

Include at least:

- datasets;
- labels;
- notebooks;
- dependencies;
- training environment;
- model artifact;
- registry metadata;
- deployment workflow;
- inference API;
- feedback data.

### Task 2 — Draw trust boundaries

Create a simple data-flow diagram and mark:

- external data sources;
- internal sensitive data;
- write paths;
- artifact stores;
- approval gates;
- identities;
- deployment boundaries.

### Task 3 — Find supply chain risks

Identify at least ten risks.

For each risk, document:

- risk title;
- affected artifact or system;
- root cause;
- impact;
- likelihood;
- proposed mitigation;
- owner;
- residual risk.

### Task 4 — Design promotion gates

Design a secure promotion workflow from experiment to production.

Include gates for:

- dataset approval;
- training code review;
- dependency scanning;
- container scanning;
- secret scanning;
- artifact integrity;
- evaluation results;
- security testing;
- privacy review;
- human approval;
- rollback.

### Task 5 — Create a registry control model

Define who can:

- register a model;
- attach metadata;
- change model stage;
- approve production promotion;
- deploy to production;
- roll back production;
- delete or quarantine an artifact.

### Task 6 — Write a residual risk statement

Explain what risk remains after your proposed controls.

Be honest about trade-offs and developer velocity.

## Expected deliverable

Use `../../templates/secure-mlops-review-template.md`.

The final review should be concise enough for engineers to act on, but detailed enough for security and leadership to understand production risk.

## Instructor notes

Strong student answers should mention:

- public dataset provenance risk;
- sensitive internal ticket data risk;
- label integrity risk;
- notebook secret leakage;
- unpinned dependency risk;
- shared service account risk;
- unsafe model artifact format/loading risk;
- weak artifact storage permissions;
- registry promotion abuse;
- lack of provenance;
- lack of security/privacy evaluation;
- feedback poisoning;
- missing rollback;
- poor auditability.

Better answers will prioritize controls instead of proposing everything at once.

The instructor should push students to define a minimum viable secure path that preserves developer velocity while protecting production.
