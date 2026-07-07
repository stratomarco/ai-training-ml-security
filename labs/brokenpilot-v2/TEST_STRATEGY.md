# BrokenPilot v2 Test Strategy

BrokenPilot v2 must keep the v1 discipline: every meaningful lab behavior should be deterministic and testable.

## Test categories

### Unit tests

Use unit tests for:

- descriptor validation
- signature or demo-signature checks
- descriptor hash pinning
- nonce and expiration validation
- sender/receiver identity checks
- delegated-authority checks

### Integration tests

Use integration tests for:

- orchestrator to sub-agent delegation
- tool broker policy decisions
- MCP-like descriptor acceptance and rejection
- audit trace correlation
- control toggles

### Scenario tests

Use scenario tests for full failure chains:

- descriptor poisoning to unsafe tool routing
- inter-agent replay
- rogue agent impersonation
- cascading failure across delegation

## Expected test naming

Use names that explain the security behavior:

```text
test_unsigned_descriptor_is_accepted_when_descriptor_control_disabled
test_unsigned_descriptor_is_rejected_when_descriptor_control_enabled
test_replayed_inter_agent_message_is_rejected_with_nonce_control
test_rogue_agent_cannot_impersonate_ticket_agent_with_identity_control
test_poisoned_retrieval_output_does_not_become_action_authority
```

## CI expectation

v2 tests should eventually run separately from v1 tests until v2 becomes release-candidate material. The v1 release gate must stay stable while v2 is under development.
