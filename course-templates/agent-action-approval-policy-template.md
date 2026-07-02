# Agent Action Approval Policy Template

Use this template to define which agent actions require human approval.

## Policy scope

Agent name:

System owner:

Policy owner:

Review date:

## Risk tiers

| Tier | Description | Example actions | Default decision |
|---|---|---|---|
| Low | Read-only or low-impact action | Summarize allowed document | Allow + log |
| Medium | Internal low-risk write | Add internal ticket comment | Authorize + log |
| High | Sensitive or externally visible action | Notify broad channel, email user | Require approval |
| Critical | Destructive, privileged, or hard to reverse | Delete record, run diagnostic | Approval + extra controls |

## Approval requirements

| Action | Approval required? | Approver | Evidence required | Rollback required? |
|---|---|---|---|---|
| | | | | |

## Approval screen requirements

Approval requests must show:

- exact action;
- target object;
- arguments;
- requester;
- agent identity;
- reason;
- evidence and sources;
- risk tier;
- expected impact;
- rollback path;
- relevant policy result.

## Deny-by-default conditions

Deny when:

- target is outside authorized scope;
- arguments fail validation;
- retrieved content is the only reason for the action;
- action attempts to bypass approval;
- memory conflicts with security policy;
- action is not mapped to a known tool policy;
- required approver is unavailable;
- logs cannot be written.

## Break-glass process

Define emergency exception handling:

- who can approve;
- how it is logged;
- expiration;
- after-action review;
- notification requirements.

## Review cadence

This policy must be reviewed:

- after major model changes;
- after new tools are added;
- after incidents;
- after permission model changes;
- at least every defined review interval.
