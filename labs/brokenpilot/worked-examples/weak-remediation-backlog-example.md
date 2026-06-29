# Weak Example — BrokenPilot Remediation Backlog

This is an example of a weak remediation backlog.

## Backlog

| Task | Priority |
|---|---|
| Improve authorization | High |
| Add logging | Medium |
| Fix memory | High |
| Add approvals | Medium |
| Make agent safer | High |

## Why this is weak

This backlog is not actionable.

Problems:

- No owner.
- No related finding.
- No target component.
- No acceptance criteria.
- No test criteria.
- No definition of done.
- No distinction between authorization, approval, logging, and memory controls.
- No way to know whether the fix worked.

"Improve authorization" is not a task. It is a theme.

## Better version

Replace vague tasks with implementable backlog items:

```text
Bad: Improve authorization.
Better: Enforce caller.tenant == ticket.tenant before update_ticket execution. Return 403 on mismatch. Add unit test for Alice/alpha attempting to update TCK-2001/beta.
```

```text
Bad: Fix memory.
Better: Make global memory inactive by default. Require review approval before memory entries can influence agent decisions. Log memory IDs consumed during each agent run.
```
