# BrokenPilot Remediation Backlog Guide

## Purpose

The capstone should end with actionable engineering work.

This guide helps students convert findings into a remediation backlog.

## Priority model

| Priority | Meaning | Example |
|---|---|---|
| P0 | Must fix before broad deployment. | Tool execution lacks per-action authorization. |
| P1 | Fix soon; compensating controls may allow limited pilot. | Memory entries lack expiration and review. |
| P2 | Planned hardening. | Improve anomaly detection for unusual retrieval patterns. |
| P3 | Future improvement. | Improve user education and UX warnings. |

## Backlog fields

| Field | Description |
|---|---|
| ID | Unique remediation ID. |
| Related finding | Finding ID this addresses. |
| Priority | P0, P1, P2, or P3. |
| Owner | Team that should implement it. |
| Control type | Authorization, validation, logging, approval, monitoring, governance, etc. |
| Description | What should change. |
| Acceptance criteria | How to know it is done. |
| Validation test | How to verify the fix. |
| Dependencies | Other teams, services, or decisions needed. |
| Residual risk | What remains after implementation. |

## Example backlog item

```text
ID: REM-BP-001
Related finding: BP-003 Unauthorized ticket update
Priority: P0
Owner: Platform / Workflow team
Control type: Authorization and approval
Description: Add a tool gateway policy that enforces per-user, per-ticket, per-action authorization before ticket updates are executed. Require human approval for severity changes and ticket closure.
Acceptance criteria: The model can request an update, but the backend denies unauthorized actions and creates an approval request for high-impact actions.
Validation test: Low-privilege user cannot update restricted ticket severity through BrokenPilot. Authorized incident commander receives approval prompt for high-impact update.
Dependencies: Ticket API permission model and approval workflow service.
Residual risk: Authorized users may still approve incorrect suggestions; user training and audit review remain required.
```

## Grouping by control area

Consider grouping remediation by:

- RAG authorization;
- tool gateway;
- approval workflow;
- memory governance;
- output handling;
- logging and monitoring;
- privacy and retention;
- evaluation and release gates;
- user experience and warnings.

## Balancing security and velocity

Not every fix needs to block all work.

Useful patterns:

- start with read-only mode;
- allow low-risk tools first;
- require approvals only for high-impact actions;
- use feature flags;
- limit pilot user groups;
- monitor heavily during rollout;
- add kill switches and rollback.

## Backlog quality checklist

- [ ] Every high-risk finding has a remediation item.
- [ ] Every P0 has clear acceptance criteria.
- [ ] Owners are realistic.
- [ ] Validation tests are defined.
- [ ] Dependencies are identified.
- [ ] Residual risk is documented.
- [ ] The roadmap preserves useful business value where possible.
