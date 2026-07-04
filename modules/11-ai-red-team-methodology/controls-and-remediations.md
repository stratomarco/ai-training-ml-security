# Controls and remediations: AI red team methodology

## Red team control objective

The objective is not to eliminate all possible bad outputs. The objective is to validate whether the system's security boundaries hold under realistic abuse.

## Controls to evaluate

### Retrieval controls

- Tenant, role, and classification filters before context construction.
- Evidence that unauthorized documents never reach the model.
- Tests for both positive and negative access cases.

### Prompt and instruction controls

- Instruction and data separation.
- Untrusted-content handling.
- No reliance on prompt wording as the only boundary.

### Tool controls

- Per-tool authorization.
- Target-object authorization.
- Approval gates for high-impact actions.
- Tool argument validation.
- Audit logging.

### Memory controls

- Memory review before activation.
- Scope isolation by tenant, user, and purpose.
- Expiry and deletion.
- Evidence of what memory influenced a run.

### Output controls

- Context-specific encoding.
- Validation before downstream interpretation.
- Redaction and classification when needed.

### Operational controls

- Reset path for labs and test environments.
- Audit logs for reproduction.
- Kill switches and rollback procedures for production systems.

## Strong remediation language

A strong red team report gives engineering-ready controls:

- Add authorization in the tool broker for target ticket tenant and user role.
- Reject retrieved documents that do not match the active user's tenant and role before context construction.
- Mark memory as pending until reviewed and isolate memory by tenant.
- Encode model output before insertion into HTML sinks.
- Add regression tests for each fixed abuse path.

## Validation after remediation

Every finding should have a validation test. The test should fail in vulnerable mode and pass in controlled mode. If a finding cannot be validated, it is probably not ready for the final report.

## Residual risk

Red team results are samples, not proof of absence. A good report states what was tested, what was not tested, and which risks require monitoring, future testing, or explicit acceptance.

## Quality bar for red team remediations

A red team remediation should be testable by someone who did not write the report. Avoid language such as "improve guardrails" or "make the agent safer." Instead, name the enforcement point.

Good examples:

- Enforce target-ticket tenant checks in the tool broker before update execution.
- Reject retrieved documents that do not match the active user's tenant and role before context construction.
- Require memory entries to be approved and scoped before they can influence an agent run.
- Encode model output before insertion into HTML or other interpreted sinks.

Each remediation should have a paired validation step. If the validation cannot be written, the remediation is probably too vague.
