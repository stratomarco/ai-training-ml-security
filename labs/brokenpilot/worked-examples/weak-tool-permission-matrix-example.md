# Weak Example  -  BrokenPilot Tool Permission Matrix

This is an example of a weak tool permission matrix for the BrokenPilot capstone.

## Weak matrix

| Tool | Who can use it | Security |
|---|---|---|
| Search docs | Internal users | Should be safe |
| Read tickets | Ops team | Check access |
| Update tickets | Ops team | Needs approval sometimes |
| Create tickets | Internal users | Log it |
| Memory | Users | Be careful |

## Why this is weak

This matrix is too vague to implement.

Problems:

- It does not define exact roles.
- It does not define tenant boundaries.
- It does not define scopes.
- It does not define when approval is required.
- It does not say what happens when tool arguments come from model output, RAG, or memory.
- It does not define denial conditions.
- It does not define required audit fields.
- It uses phrases like "should be safe" and "be careful" instead of enforceable rules.

A developer could not reliably implement this. Two teams could interpret it differently and both claim compliance.

## How to improve it

Replace generic statements with policy rules:

```text
Bad: Ops team can update tickets.
Better: Allow update_ticket only when caller.role == "ops" and caller.tenant == ticket.tenant.
```

```text
Bad: Needs approval sometimes.
Better: Require approval for closing, deleting, escalating, or changing owner on any ticket.
```

```text
Bad: Log it.
Better: Log caller, tenant, tool name, target object, policy decision, approval ID, source of tool arguments, and before/after values.
```
