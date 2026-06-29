# Concrete Control Implementation Template

Use this template when a finding requires a practical mitigation.

## Finding

Describe the issue in one paragraph.

## Violated security property

Examples: confidentiality, integrity, availability, authorization, auditability, tenant isolation, non-repudiation, privacy, cost control.

## Root cause

Describe the design or implementation weakness that made the issue possible.

## Control objective

What should the control guarantee?

## Enforcement point

Where is the control enforced?

Examples:

- API gateway
- RAG retrieval service
- Tool execution service
- Policy engine
- Model gateway
- CI/CD pipeline
- Model registry
- Logging pipeline

## Required inputs

What data does the control need?

| Input | Source | Required? |
|---|---|---|
| User ID | Auth service | Yes |
| Tenant ID | Auth/session | Yes |
| Document ACL | Document metadata | Yes |
| Tool sensitivity | Tool registry | Yes |

## Policy rules

Write concrete rules.

```text
Rule 1: A user may retrieve a chunk only if user.tenant_id == document.tenant_id.
Rule 2: A user may retrieve a restricted document only if user.role is in document.allowed_roles.
Rule 3: An agent may call a destructive tool only after explicit approval.
```

## Failure behavior

What happens when the control denies the action?

## Logging

What should be logged?

What should not be logged?

## Owner

Who owns implementation?

Who owns policy maintenance?

Who reviews exceptions?

## Validation tests

List tests that prove the control works.

| Test | Expected result |
|---|---|
| Cross-tenant retrieval attempt | Denied |
| Allowed user retrieves allowed doc | Allowed |
| Agent attempts destructive tool without approval | Denied |

## Residual risk

What remains risky after this control?

## Tradeoffs

How does the control affect usability, developer velocity, latency, cost, or operational complexity?
