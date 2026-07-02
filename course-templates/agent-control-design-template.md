# Agent Control Design Template

Use this template for Module 07 and future agent reviews.

## 1. System overview

Describe the agent:

- purpose;
- users;
- business workflow;
- data sources;
- tools;
- autonomy level;
- deployment context.

## 2. Architecture diagram

```text
[fill in architecture]
```

## 3. Assets

| Asset | Owner | Sensitivity | Impact if misused |
|---|---|---|---|
| | | | |

## 4. Trust boundaries

| Boundary | Trusted side | Untrusted/lower-trust side | Notes |
|---|---|---|---|
| | | | |

## 5. Agent identities

| Identity | Used for | Scope | Credential type | Notes |
|---|---|---|---|---|
| User identity | | | | |
| Agent identity | | | | |
| Tool identity | | | | |

## 6. Tool inventory

| Tool | Capability | Read/write/execute | Risk tier | Current control | Proposed control |
|---|---|---|---|---|---|
| | | | | | |

## 7. Tool permission matrix

| Tool | Allowed users | Allowed agent role | Allowed targets | Approval | Logging | Rollback |
|---|---|---|---|---|---|---|
| | | | | | | |

## 8. Abuse cases

Use the format: `As an attacker, I want to ... so that ...`

1. 
2. 
3. 
4. 
5. 

## 9. Approval policy

| Risk tier | Examples | Control |
|---|---|---|
| Low | | |
| Medium | | |
| High | | |
| Critical | | |

## 10. Memory policy

| Memory type | Allowed? | Scope | Provenance | Expiry | Approval |
|---|---|---|---|---|---|
| | | | | | |

Memory cannot:

- grant privileges;
- bypass policy;
- disable approvals;
- override system security requirements.

## 11. Tool argument validation

| Tool | Argument | Validation rule | Failure behavior |
|---|---|---|---|
| | | | |

## 12. Logging and audit

Log:

- user;
- agent;
- tool;
- target;
- safe argument summary;
- policy decision;
- approval decision;
- result;
- timestamp;
- correlation ID.

Sensitive logging considerations:

- 

## 13. Monitoring and alerts

| Alert | Condition | Severity | Response |
|---|---|---|---|
| | | | |

## 14. Kill switch and rollback

| Control | Owner | Activation condition | Notes |
|---|---|---|---|
| Disable agent | | | |
| Disable tool | | | |
| Revoke credentials | | | |
| Freeze memory writes | | | |
| Roll back action | | | |

## 15. Residual risk

Describe what risk remains after controls are applied.

Include:

- accepted risk;
- risk owner;
- monitoring requirement;
- review date;
- trigger for reassessment.

## 16. Final recommendation

Choose one:

- [ ] Approve as designed
- [ ] Approve with required changes
- [ ] Do not approve until redesigned
- [ ] Needs further analysis

Rationale:
