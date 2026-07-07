# BrokenPilot v2 Control Matrix

The v2 control matrix maps agentic failure modes to concrete controls and validation evidence.

| Failure mode | Primary control | Supporting controls | Observable evidence |
|---|---|---|---|
| Spoofed MCP-like descriptor | Descriptor signature validation | trusted issuer list, hash pinning | descriptor rejected before tool routing |
| Descriptor drift | Descriptor pinning | approval on descriptor change | changed descriptor blocks workflow |
| Rogue agent impersonation | Signed agent identity | sender authorization, receiver binding | forged sender rejected |
| Inter-agent replay | Nonce and expiry validation | idempotency at action layer | replayed message denied |
| Cascading delegation failure | Delegated-authority limits | approval gates, retrieval provenance | unsafe action blocked downstream |
| Tool misuse | Broker policy enforcement | capability allowlist, action authz | unauthorized tool call denied |
| Sensitive context exfiltration | Context routing policy | tenant continuity, data minimization | sensitive context not sent to untrusted server |
| Memory/context poisoning | Instruction/data separation | memory review, provenance labels | poisoned instruction not promoted to policy |

## Control quality standard

A v2 control is not complete until it has:

- a vulnerable baseline
- a control-on passing path
- a negative test
- audit evidence
- a student explanation prompt
- an instructor debrief note
