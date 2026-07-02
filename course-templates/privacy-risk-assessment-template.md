# Privacy Risk Assessment Template  -  AI Systems

Use this template for ML, LLM, RAG, and agent systems that process sensitive data.

## 1. System overview

| Field | Value |
|---|---|
| System name |  |
| Business owner |  |
| Technical owner |  |
| Security reviewer |  |
| Privacy reviewer |  |
| Date |  |
| Version |  |

## 2. System purpose

Describe what the system does and why it processes sensitive data.

## 3. User groups and roles

| Role | Purpose | Data access needed | Notes |
|---|---|---|---|
|  |  |  |  |

## 4. Sensitive data inventory

| Data type | Source | Classification | Purpose | Required? | Retention | Notes |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Include:

- prompts;
- completions;
- retrieved context;
- embeddings;
- logs;
- model traces;
- tool outputs;
- memory;
- feedback;
- training data;
- evaluation data.

## 5. Data-flow summary

Describe where sensitive data flows.

```text
source -> processing -> model/retrieval/tool -> output -> logs/feedback/retention
```

## 6. Privacy threat model

| Abuse case | Attacker/user | Data at risk | Path | Impact | Existing controls | Gap |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 7. AI-specific privacy risks

| Risk | Applies? | Rationale | Test or evidence | Mitigation |
|---|---|---|---|---|
| Membership inference |  |  |  |  |
| Model inversion |  |  |  |  |
| Training data extraction |  |  |  |  |
| Prompt leakage |  |  |  |  |
| Completion leakage |  |  |  |  |
| Embedding leakage |  |  |  |  |
| Cross-tenant retrieval |  |  |  |  |
| Agent memory leakage |  |  |  |  |
| Feedback-loop leakage |  |  |  |  |
| Log/trace leakage |  |  |  |  |

## 8. RAG and vector database review

| Question | Answer | Evidence | Gap |
|---|---|---|---|
| Are source ACLs preserved during ingestion? |  |  |  |
| Are chunks tagged with tenant/user/role metadata? |  |  |  |
| Is authorization enforced before retrieval reaches the model? |  |  |  |
| Are cross-tenant retrieval tests implemented? |  |  |  |
| Do deletions propagate to the vector index? |  |  |  |
| Are citations filtered for authorization? |  |  |  |

## 9. Prompt, log, and trace review

| Artifact | Stored? | Contains sensitive data? | Access control | Retention | Redaction/minimization |
|---|---|---|---|---|---|
| Prompts |  |  |  |  |  |
| Completions |  |  |  |  |  |
| Retrieved context |  |  |  |  |  |
| Tool results |  |  |  |  |  |
| Model traces |  |  |  |  |  |
| Feedback |  |  |  |  |  |

## 10. Controls

| Control | Status | Owner | Evidence | Notes |
|---|---|---|---|---|
| Data minimization |  |  |  |  |
| Purpose limitation |  |  |  |  |
| Retrieval authorization |  |  |  |  |
| Tenant isolation |  |  |  |  |
| Prompt/log governance |  |  |  |  |
| Redaction/masking |  |  |  |  |
| Retention limits |  |  |  |  |
| Deletion propagation |  |  |  |  |
| Privacy testing |  |  |  |  |
| Audit logging |  |  |  |  |
| Incident response |  |  |  |  |

## 11. Recommended mitigations

| Priority | Recommendation | Risk reduced | Owner | Target date |
|---|---|---|---|---|
| High |  |  |  |  |
| Medium |  |  |  |  |
| Low |  |  |  |  |

## 12. Residual risk

Describe what privacy risk remains after recommended controls.

Include:

- why the risk remains;
- who owns it;
- what monitoring exists;
- what review cadence applies;
- what would trigger reassessment.

## 13. Release decision

| Decision | Select |
|---|---|
| Approved |  |
| Approved with conditions |  |
| Blocked pending mitigations |  |
| Not approved |  |

## 14. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Product owner |  |  |  |
| Security owner |  |  |  |
| Privacy owner |  |  |  |
| Engineering owner |  |  |  |
