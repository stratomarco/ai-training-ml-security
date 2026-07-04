# BrokenPilot Control Toggle Plan

The MVP should allow instructors to switch between vulnerable and hardened behavior without changing code.

## Why toggles?

Control toggles help students see the difference between:

- A vulnerable architecture
- A partially mitigated architecture
- A better-controlled architecture

This supports a key teaching goal: security controls should be observable and testable.

## Environment toggles

| Environment variable | Default | Meaning |
|---|---|---|
| `BROKENPILOT_MODE` | `vulnerable` | Global default mode: `vulnerable` or `hardened` |
| `ENABLE_RETRIEVAL_AUTHZ` | `false` | Enforce document authorization during retrieval |
| `ENABLE_TOOL_APPROVAL` | `false` | Require approval for sensitive tool actions |
| `ENABLE_MEMORY_REVIEW` | `false` | Queue memory writes instead of using them immediately |
| `ENABLE_TOOL_AUDIT` | `true` | Record tool attempts and decisions |
| `ENABLE_OUTPUT_ENCODING` | `false` | Encode/sanitize model output before rendering |
| `ENABLE_RATE_LIMITING` | `false` | Apply simple request/tool budget controls |

## Per-request mode

For labs, it may be useful to allow the request body to specify mode:

```json
{
  "message": "Summarize INC-1001",
  "user": "alice",
  "mode": "hardened"
}
```

If implemented, the UI must clearly show the current mode.

## Expected student exercises

Students should be asked to compare behavior with controls off and on:

| Exercise | Vulnerable mode | Hardened mode |
|---|---|---|
| Cross-document retrieval | Unauthorized docs retrieved | Unauthorized docs filtered |
| Tool confused deputy | Ticket priority changed | Approval required or blocked |
| Memory poisoning | Memory immediately affects response | Memory queued or ignored |
| Unsafe output | Output rendered directly | Output encoded/sanitized |

## Control design requirement

Students should not simply say “enable guardrails.” They should specify:

- What is checked
- Where it is checked
- Which identity is used
- What metadata is required
- What happens on deny
- What gets logged
- How an engineer could test it

## Example control rule

```text
Rule: Ticket priority downgrade requires approval.

When:
- tool = ticket.update
- field = priority
- new value is lower urgency than current value

Require:
- requesting user has can_change_priority=true
- ticket.owner_team equals user.team or user has Admin role
- explicit human approval exists

Deny response:
- Do not update ticket
- Return approval_required
- Log requested action, user, ticket, source document IDs, and policy decision
```
