# ML System Architecture Review Template

Use this template to review ML, LLM, RAG, or agent systems.

## 1. System overview

```text
System name:
Business purpose:
Model purpose:
Decision or workflow influenced:
System owner:
Model owner:
Data owner:
Review date:
Reviewers:
```

## 2. Architecture summary

Describe the system in plain language.

```text
Users:
External systems:
Data sources:
Model types:
Deployment environment:
Inference path:
Feedback path:
```

## 3. Lifecycle diagram

Paste or link to the lifecycle data-flow diagram.

The diagram should include:

- Data sources
- Data stores
- Labeling
- Feature engineering
- Training
- Evaluation
- Model registry
- Deployment
- Inference
- Monitoring
- Feedback
- LLM/RAG/agent components if applicable

## 4. Asset inventory

| Asset | Owner | Sensitivity | Integrity impact | Availability impact | Notes |
|---|---|---|---|---|---|
| | | | | | |

## 5. Trust boundaries

| Boundary | From | To | Data/control crossing | Concern |
|---|---|---|---|---|
| | | | | |

## 6. Data sources

| Source | Internal/external | Who can write? | Sensitive? | Provenance tracked? | Used for training? |
|---|---|---|---|---|---|
| | | | | | |

## 7. Model lifecycle controls

| Stage | Existing controls | Missing controls | Risk level | Owner |
|---|---|---|---|---|
| Data collection | | | | |
| Labeling | | | | |
| Feature engineering | | | | |
| Training | | | | |
| Evaluation | | | | |
| Model registry | | | | |
| Deployment | | | | |
| Inference | | | | |
| Monitoring | | | | |
| Feedback | | | | |

## 8. LLM/RAG/agent components

Complete this section if applicable.

| Component | Present? | Risk | Control |
|---|---|---|---|
| System prompt | | | |
| Prompt templates | | | |
| Model provider API | | | |
| Document ingestion | | | |
| Vector database | | | |
| Retrieval authorization | | | |
| Tool calling | | | |
| Agent memory | | | |
| Human approval | | | |
| Audit logging | | | |

## 9. Abuse cases

| Abuse case | Attacker | Entry point | Target asset | Impact | Existing control | Gap |
|---|---|---|---|---|---|---|
| | | | | | | |

## 10. Security requirements

| Requirement | Reason | Enforced where? | Status |
|---|---|---|---|
| | | | |

## 11. Findings

| ID | Finding | Severity | Lifecycle stage | Recommendation | Owner |
|---|---|---|---|---|---|
| MLARCH-001 | | | | | |

## 12. Residual risk

```text
The most important remaining risks are:

The team accepts/reduces/transfers/avoids these risks by:

Required follow-up actions:
```

## 13. Review decision

```text
Decision: Approved / Approved with conditions / Not approved
Conditions:
Next review date:
Approver:
```
