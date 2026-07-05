# Tool Permission Matrix Template

Use this template to define and review agent tool permissions.

## Tool summary

| Tool | Purpose | Risk tier | Owner |
|---|---|---|---|
| | | | |

## Permission matrix

| Tool | User role | Agent role | Action | Target scope | Conditions | Approval | Log level |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Argument validation

| Tool | Argument | Allowed values/pattern | Deny condition | Notes |
|---|---|---|---|---|
| | | | | |

## Dangerous capability review

Check any that apply:

- [ ] Tool can write data.
- [ ] Tool can delete data.
- [ ] Tool can send messages.
- [ ] Tool can call external systems.
- [ ] Tool can execute code or commands.
- [ ] Tool can access sensitive data.
- [ ] Tool can affect multiple tenants/users.
- [ ] Tool can create cost.
- [ ] Tool can change security settings.
- [ ] Tool can create durable memory or configuration.

## Required controls

| Control | Required? | Implemented? | Notes |
|---|---|---|---|
| Per-action authorization | | | |
| Object-level authorization | | | |
| Argument validation | | | |
| Rate limit | | | |
| Approval gate | | | |
| Audit logging | | | |
| Rollback | | | |
| Monitoring | | | |

## Final decision

- [ ] Tool approved
- [ ] Tool approved with restrictions
- [ ] Tool rejected
- [ ] Tool requires redesign

Rationale:
