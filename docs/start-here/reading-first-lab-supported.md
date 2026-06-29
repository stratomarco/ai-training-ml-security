# Reading-First, Lab-Supported Learning

This course is designed for people who want to understand ML Security deeply, not only run attack payloads.

The labs are important, but they are not the course. The course is the security reasoning: architecture, trust boundaries, failure modes, control design, testing, and residual risk.

## The learning loop

Each major topic should follow this loop:

1. Read the concept.
2. Understand the system architecture.
3. Identify the violated security principle.
4. Walk through the attack path.
5. Evaluate impact.
6. Design controls.
7. Run or discuss the lab.
8. Verify whether the control works.
9. Write the finding or risk memo.
10. Discuss residual risk.

## Why this matters

A student who only learns payloads may know how to reproduce a failure in one lab. A student who understands the underlying security principle can recognize similar failures in new systems.

For example:

| Lab behavior | Deeper lesson |
|---|---|
| Prompt injection makes the model ignore an instruction | Untrusted input is being interpreted as authority |
| RAG retrieves a malicious document | Retrieved content is untrusted input and needs authorization, provenance, and context separation |
| Agent closes a ticket from another tenant | The tool layer lacks complete mediation and tenant-scoped authorization |
| Memory poisoning changes later behavior | Persistent context has become a security-sensitive data store |

## Expected student output

Students should not only submit answers like “the model was jailbroken.”

A good answer should include:

- Asset affected
- Actor and trust boundary
- Attack path
- Root cause
- Impact
- Evidence
- Control recommendation
- How to test the control
- Residual risk
- Framework mapping

## Labs are validation, not decoration

Labs are used to validate the ideas from the reading.

The ideal lab flow is:

1. Observe vulnerable behavior.
2. Explain why it happens.
3. Enable or design a control.
4. Re-test.
5. Record evidence.
6. Explain what risk remains.

This is the same pattern used in the BrokenPilot Module 07 tool-authorization scenario.
