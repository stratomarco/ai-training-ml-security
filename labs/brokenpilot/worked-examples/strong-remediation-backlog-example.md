# Strong Example  -  BrokenPilot Remediation Backlog

This is an example of a strong remediation backlog for BrokenPilot findings.

A strong backlog turns findings into implementable engineering work.

## Backlog items

| ID | Title | Related finding | Priority | Owner | Acceptance criteria |
|---|---|---|---|---|---|
| BP-FIX-001 | Enforce tenant authorization before ticket updates | BP-MVP-04 | High | Platform/API team | `update_ticket` returns 403 when caller tenant differs from ticket tenant; unit test covers cross-tenant deny; audit event records denial |
| BP-FIX-002 | Add approval gate for destructive ticket transitions | BP-MVP-04 | High | Ops tooling team | Closing, deleting, escalating, or owner-changing tickets requires approval ID; missing approval returns 403; approval result is logged |
| BP-FIX-003 | Track source of tool arguments | BP-MVP-04 / BP-MVP-05 | Medium | Agent platform team | Tool calls include `argument_source` values: `user`, `model`, `retrieval`, `memory`, or `system`; policy can require stricter checks for non-user sources |
| BP-FIX-004 | Require review for global or tenant-wide memory | BP-MVP-05 | High | Agent platform team | Global memory entries are inactive until approved; tests verify unapproved memory cannot influence `/agent/run` |
| BP-FIX-005 | Add memory scope and tenant isolation | BP-MVP-05 | High | Agent platform team | Alice cannot consume memory created by Eve in another tenant unless explicitly approved and tenant-scoped by policy |
| BP-FIX-006 | Add audit log correlation ID for agent actions | BP-MVP-04 / BP-MVP-05 | Medium | Observability team | Each agent run has correlation ID linking user request, memory entries read, documents retrieved, tool calls, policy decisions, and final result |

## Example user story

```text
As an operations platform engineer,
I want every ticket tool call to be authorized against the target ticket tenant,
so that an agent cannot act as a confused deputy across tenants.
```

## Acceptance test example

```python
def test_cross_tenant_ticket_update_is_denied_when_tool_authz_enabled():
    enable("ENABLE_TOOL_AUTHZ")
    response = client.post("/tools/update-ticket", json={
        "user_id": "alice",
        "ticket_id": "TCK-2001",
        "status": "closed",
        "note": "attempted cross-tenant update",
    })
    assert response.status_code == 403
    assert response.json()["detail"]["error"] == "tool_authorization_denied"
```

## Why this is strong

This backlog is strong because each item has:

- A clear owner.
- A related finding.
- A security outcome.
- Concrete acceptance criteria.
- A way to test the fix.

It can be handed to an engineering team without requiring them to infer the actual work.
