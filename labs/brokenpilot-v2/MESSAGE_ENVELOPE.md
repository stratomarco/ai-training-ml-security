# BrokenPilot v2 Message Envelope

The message envelope is the basic unit of inter-agent communication in BrokenPilot v2. It exists so students can see where identity, intent, provenance, replay protection, and delegation authority should live.

## Envelope fields

```json
{
  "message_id": "msg-001",
  "correlation_id": "wf-2026-001",
  "sender_agent": "orchestrator",
  "receiver_agent": "retrieval-agent",
  "tenant": "alpha",
  "user_id": "alice",
  "delegated_authority": ["retrieve:alpha_docs"],
  "intent": "retrieve_context",
  "created_at": "2026-01-01T12:00:00Z",
  "expires_at": "2026-01-01T12:05:00Z",
  "nonce": "deterministic-demo-nonce",
  "payload": {
    "query": "vendor onboarding incident"
  },
  "evidence": [],
  "signature": "demo-signature"
}
```

## Security properties

The envelope should support these teaching controls:

- sender identity
- receiver identity
- tenant continuity
- delegated authority
- message freshness
- replay prevention
- payload integrity
- audit correlation
- provenance tracking

## Vulnerable baseline

The vulnerable baseline may omit or ignore:

- signature validation
- nonce validation
- expiration checks
- delegated-authority checks
- receiver-agent checks
- tenant continuity checks

This allows labs to show replay, impersonation, cross-agent confusion, and unsafe delegation.

## Controlled behavior

With controls enabled, an unsafe message should fail before it reaches the action layer.

Example failures:

- expired message
- reused nonce
- sender not allowed to delegate requested authority
- receiver does not match envelope
- tenant mismatch
- unsigned or invalid descriptor source
