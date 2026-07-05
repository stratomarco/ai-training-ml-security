# Strong Example  -  BrokenPilot Evidence Log

This is an example of a strong evidence log entry for the BrokenPilot capstone.

A strong evidence log should allow an instructor, engineer, or risk owner to reproduce the finding and understand why it matters.

## Finding BP-MVP-04  -  Tool Confused Deputy

### Summary

Alice, an `ops` user in tenant `alpha`, was able to close ticket `TCK-2001`, which belongs to tenant `beta`, because `update_ticket` executed without checking tenant authorization.

### Environment

| Field | Value |
|---|---|
| App | BrokenPilot prototype |
| URL | `http://127.0.0.1:8010` |
| OS | Windows / PowerShell |
| Test mode | Vulnerable mode |
| Relevant controls | `ENABLE_TOOL_AUTHZ=false`, `ENABLE_TOOL_APPROVAL=false` |

### Reproduction steps

Reset state:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

Send cross-tenant update:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update from alpha user to beta ticket"}'
```

### Observed result

```text
user: alice
user_tenant: alpha
target_ticket: TCK-2001
ticket_tenant: beta
result: updated
authorization_decision: not_checked
ticket.status: closed
```

### Expected secure result

The request should be denied because `alice.tenant != ticket.tenant`.

Expected denial:

```text
HTTP 403
error: tool_authorization_denied
```

### Root cause

The tool trusted the caller and model-provided tool arguments without performing an independent authorization check against the target ticket.

### Security property violated

Tenant isolation and complete mediation.

### Impact

A user or model-mediated agent action can modify another tenant's operational ticket. In a real environment, this could close incidents, suppress work, corrupt audit history, or modify customer-impacting operational state.

### Control validation

Restarted with:

```powershell
$env:ENABLE_TOOL_AUTHZ="true"
```

Same request returned:

```text
HTTP 403
error: tool_authorization_denied
reason: User must be an ops user in the same tenant as the ticket.
user_tenant: alpha
ticket_tenant: beta
user_role: ops
```

### Recommended fix

Add a policy check before every tool execution:

```text
allow update_ticket only if caller.role == "ops" and caller.tenant == ticket.tenant
```

Also log every allow/deny decision with caller, tenant, target object, tool name, source of arguments, and policy result.
