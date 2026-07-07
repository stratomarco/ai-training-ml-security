# BrokenPilot v2 MCP-like Trust Boundary

BrokenPilot v2 uses an MCP-like local boundary to teach descriptor trust, capability advertisement, and third-party tool-server risk.

The initial implementation does not need to implement the full Model Context Protocol. It should model the security decisions that matter for a course lab:

- who advertised the capability
- whether the descriptor was trusted
- whether the descriptor changed
- whether the tool broker pinned or approved the descriptor
- whether the tool call matched the approved capability
- whether sensitive context was routed to an untrusted endpoint

## Descriptor model

Example descriptor:

```json
{
  "server_id": "trusted-ticket-server",
  "descriptor_id": "desc-001",
  "capabilities": ["ticket.read", "ticket.update"],
  "audience": "brokenpilot.local",
  "issuer": "course-ca",
  "version": "1.0.0",
  "created_at": "2026-01-01T12:00:00Z",
  "descriptor_hash": "demo-hash",
  "signature": "demo-signature"
}
```

## Vulnerable scenarios

### Spoofed capability advertisement

An untrusted server advertises a trusted-looking ticket update capability.

Expected insecure behavior:

- orchestrator sees the advertised capability
- tool broker accepts the descriptor
- sensitive context is routed to the wrong server
- action agent trusts the response

Expected controlled behavior:

- descriptor issuer is not trusted
- descriptor hash is not pinned
- descriptor change requires approval
- tool broker refuses the call

### Descriptor drift

A server descriptor changes after approval.

Expected insecure behavior:

- new capability is accepted automatically
- sensitive workflow changes without review

Expected controlled behavior:

- descriptor hash mismatch blocks the workflow
- approval is required before new capabilities are accepted

### Confused server identity

A rogue server uses a similar name or cloned schema.

Expected insecure behavior:

- string-matching accepts the server
- cloned schema receives sensitive context

Expected controlled behavior:

- identity is based on key, issuer, descriptor hash, and policy, not name similarity

## Controls

The first v2 control set should include:

- trusted issuer list
- descriptor signature check
- descriptor hash pinning
- capability allowlist
- approval on descriptor change
- tool broker policy decision log
- sensitive-context routing check
