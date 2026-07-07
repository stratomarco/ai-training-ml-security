# BrokenPilot v2 Failure Chains

This file defines the first failure chains for the v2 agentic/MCP track. Each chain must become a deterministic lab scenario before it becomes teaching material.

## Chain 1: Descriptor poisoning to unsafe tool routing

### Insecure path

1. A rogue MCP-like server advertises a trusted-looking capability.
2. The tool broker accepts the descriptor without validating issuer or hash.
3. The orchestrator routes sensitive incident context to the rogue server.
4. The rogue server returns a plausible action recommendation.
5. The action agent attempts a ticket update based on the poisoned response.

### Controls

- trusted issuer validation
- descriptor hash pinning
- approval on descriptor change
- broker-level capability allowlist
- sensitive-context routing policy

### Evidence

Students should capture:

- descriptor before/after
- broker decision
- audit correlation ID
- attempted tool call
- control-on denial

## Chain 2: Inter-agent replay to repeated action

### Insecure path

1. A valid delegation message is captured.
2. The same message is replayed after the original workflow.
3. The receiving agent accepts the old message.
4. The action agent repeats or re-attempts the state-changing action.

### Controls

- nonce tracking
- expiration check
- correlation-state check
- idempotency check at action boundary

### Evidence

Students should capture:

- original message ID
- replayed nonce
- missing freshness check
- control-on replay denial

## Chain 3: Rogue agent impersonates a peer

### Insecure path

1. A rogue agent uses a peer-like name or cloned message schema.
2. The orchestrator accepts its output as if it came from a trusted peer.
3. The rogue agent injects a recommendation into the workflow.
4. The orchestrator delegates an action based on the forged peer output.

### Controls

- signed agent identity
- receiver-agent binding
- sender authorization
- policy-bound delegation
- audit event verification

### Evidence

Students should capture:

- forged sender
- accepted workflow step
- policy gap
- control-on denial

## Chain 4: Cascading failure across delegation

### Insecure path

1. Retrieval agent returns poisoned content as if it were evidence.
2. Orchestrator treats the retrieved text as operational instruction.
3. Ticket/action agent receives a delegated action request.
4. Tool broker allows the state-changing action.
5. One poisoned output cascades into a real workflow action.

### Controls

- instruction/data separation
- retrieval provenance
- delegated-authority limits
- approval for high-risk transitions
- action-layer authorization

### Evidence

Students should capture:

- poisoned retrieved text
- delegation trace
- broker decision
- attempted action
- final denial with controls enabled
