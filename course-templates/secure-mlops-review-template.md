# Secure MLOps Review Template

## 1. Review metadata

| Field | Value |
|---|---|
| System / model name |  |
| Business owner |  |
| Technical owner |  |
| Review date |  |
| Reviewer |  |
| Risk tier |  |
| Production impact |  |

## 2. Architecture summary

Briefly describe the ML pipeline.

```text
[draw or paste pipeline flow here]
```

## 3. Artifact inventory

| Artifact | Owner | Source | Versioned? | Integrity control? | Access control? | Notes |
|---|---|---|---|---|---|---|
| Dataset |  |  |  |  |  |  |
| Labels |  |  |  |  |  |  |
| Training code |  |  |  |  |  |  |
| Dependencies |  |  |  |  |  |  |
| Container image |  |  |  |  |  |  |
| Model artifact |  |  |  |  |  |  |
| Prompt/template |  |  |  |  |  |  |
| Adapter/LoRA |  |  |  |  |  |  |
| Vector index |  |  |  |  |  |  |
| Evaluation set |  |  |  |  |  |  |

## 4. Trust boundaries

List important trust boundaries.

| Boundary | Data/artifact crossing | Risk | Control |
|---|---|---|---|
| External data to internal dataset |  |  |  |
| Notebook to production pipeline |  |  |  |
| Training job to artifact store |  |  |  |
| Registry to production deployment |  |  |  |
| Feedback to retraining |  |  |  |

## 5. Dataset provenance review

| Question | Answer | Risk |
|---|---|---|
| Where did the data come from? |  |  |
| Who owns the data? |  |  |
| Is usage allowed? |  |  |
| Does it contain sensitive data? |  |  |
| Is it versioned? |  |  |
| Who can modify it? |  |  |
| Can bad records be removed? |  |  |

## 6. Build and training review

| Area | Finding | Required action |
|---|---|---|
| Training code review |  |  |
| Dependency locking |  |  |
| Dependency scanning |  |  |
| Container scanning |  |  |
| Training identity |  |  |
| Secrets management |  |  |
| Experiment tracking |  |  |

## 7. Model artifact review

| Question | Answer | Risk |
|---|---|---|
| What format is used? |  |  |
| Can loading execute code? |  |  |
| Is the artifact hashed? |  |  |
| Is it signed or provenanced? |  |  |
| Where is it stored? |  |  |
| Who can modify it? |  |  |
| Is it immutable after registration? |  |  |

## 8. Registry and promotion review

| Control | Current state | Required state |
|---|---|---|
| Registry authentication |  |  |
| Registry write permissions |  |  |
| Production promotion approval |  |  |
| Evaluation gate |  |  |
| Security gate |  |  |
| Privacy gate |  |  |
| Rollback version |  |  |
| Audit log |  |  |

## 9. Runtime and monitoring review

| Area | Current state | Required action |
|---|---|---|
| Runtime identity |  |  |
| API authentication |  |  |
| Rate limiting |  |  |
| Egress control |  |  |
| Logging |  |  |
| Drift monitoring |  |  |
| Abuse monitoring |  |  |
| Feedback loop controls |  |  |

## 10. Risk register

| ID | Risk | Impact | Likelihood | Severity | Mitigation | Owner | Residual risk |
|---|---|---|---|---|---|---|---|
| MLOPS-001 |  |  |  |  |  |  |  |

## 11. Required gates before production

- [ ] Dataset approved
- [ ] Training code reviewed
- [ ] Dependencies locked and scanned
- [ ] Container scanned
- [ ] Secrets scan passed
- [ ] Artifact integrity recorded
- [ ] Provenance recorded
- [ ] Evaluation passed
- [ ] Security tests passed
- [ ] Privacy review completed where relevant
- [ ] Production approver recorded
- [ ] Rollback plan tested

## 12. Residual risk statement

Document what remains risky after controls are applied.

## 13. Recommendation

Choose one:

- [ ] Approved for production
- [ ] Approved for limited pilot
- [ ] Approved only with explicit risk acceptance
- [ ] Not approved until required actions are complete

Rationale:
