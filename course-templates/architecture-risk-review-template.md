# Architecture Risk Review Template

Use this template for BIML-style architecture reviews of ML, LLM, RAG, and agent systems.

## 1. Review metadata

| Field | Value |
|---|---|
| System name | |
| Review date | |
| Reviewers | |
| System owner | |
| Business owner | |
| Version reviewed | |
| Review scope | |
| Out of scope | |

## 2. System summary

Describe the system in plain language.

```text
The system is intended to...
```

## 3. Architecture overview

Add a diagram or component list.

```text
user
  |
  v
application
  |
  +-- model gateway
  +-- retrieval service
  +-- tool broker
  +-- memory service
  +-- logs/monitoring
```

## 4. Components

| Component | Purpose | Owner | Trust level |
|---|---|---|---|
| | | | |

## 5. Assets

| Asset | Sensitivity | Integrity requirement | Availability requirement | Owner |
|---|---|---|---|---|
| | | | | |

## 6. Users and actors

| Actor | Role | Privileges | Abuse potential |
|---|---|---|---|
| | | | |

## 7. Data flows

| Flow | Source | Destination | Data | Trust boundary? |
|---|---|---|---|---|
| | | | | |

## 8. Trust boundaries

| Boundary | Why it matters | Control expected |
|---|---|---|
| | | |

## 9. Assumptions

| Assumption | Risk if false | Validation method |
|---|---|---|
| | | |

## 10. Abuse cases

Use this format:

```text
As a [malicious actor],
I want to [abuse action],
so that [security impact].
```

| Abuse case | Asset impacted | Security property impacted |
|---|---|---|
| | | |

## 11. Risk register

| ID | Risk | Component | Asset | Impact | Likelihood | Priority | Owner |
|---|---|---|---|---|---|---|---|
| R-001 | | | | | | | |

## 12. Security requirements

| Requirement ID | Requirement | Maps to risk | Owner | Test method |
|---|---|---|---|---|
| SR-001 | | | | |

## 13. Mitigation plan

| Mitigation | Type | Risk reduced | Owner | Trade-off | Status |
|---|---|---|---|---|---|
| | Prevent / Detect / Respond / Recover | | | | |

## 14. Logging and monitoring

| Event | Why it matters | Alert condition | Owner |
|---|---|---|---|
| | | | |

## 15. Residual risk

Describe what remains after mitigations.

```text
After applying the proposed controls, the main remaining risks are...
These risks are acceptable/not acceptable because...
The system should be monitored for...
The risk owner should review this again when...
```

## 16. Approval / risk acceptance

| Risk accepted? | Accepted by | Date | Conditions |
|---|---|---|---|
| | | | |

## 17. Re-review triggers

- [ ] New model provider
- [ ] New tool or plugin
- [ ] New data source
- [ ] New memory behavior
- [ ] New autonomous workflow
- [ ] New sensitive data class
- [ ] Major prompt or policy change
- [ ] Major incident or near miss
- [ ] Significant model behavior change
- [ ] Regulatory or business requirement change
