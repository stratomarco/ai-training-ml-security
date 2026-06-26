# Module 12 — Capstone: BrokenPilot

## Purpose

Bring everything together in a realistic internal AI agent scenario.

## Key message

Students must connect architecture, exploitation, mitigation, governance, and residual risk.

## Learning objectives

By the end of this module, students should be able to:

1. Explain the core security problem addressed by this module.
2. Identify the relevant assets, trust boundaries, and attacker goals.
3. Connect the topic to classic security engineering principles.
4. Recognize the ML, LLM, RAG, or agent-specific failure mode.
5. Propose practical mitigations and discuss residual risk.

## Topics

- Architecture review
- Threat modeling
- Attack chain development
- Prompt injection
- Indirect prompt injection
- RAG poisoning
- Tool misuse
- Memory poisoning
- Mitigation design
- Residual risk

## Security engineering connection

This module should always connect back to classic security engineering. The instructor should avoid treating AI as magic or as a separate universe. The practical question is how familiar principles change when models, datasets, embeddings, tools, prompts, and autonomous workflows become part of the system.

Important principles to reuse:

- Least privilege
- Explicit trust boundaries
- Complete mediation
- Defense in depth
- Secure defaults
- Input and output handling
- Auditability
- Supply chain integrity
- Privacy by design
- Resilience and recovery

## Reference architecture

```text
user or attacker
  |
  v
application or AI interface
  |
  +-- model gateway
  +-- policy layer
  +-- data or retrieval service
  +-- tool or workflow service
  +-- logs and monitoring
```

## Lab

### Lab goal

Threat model, attack, defend, and present an internal AI operations assistant.

### Lab structure

1. Introduce the scenario.
2. Map assets and trust boundaries.
3. Demonstrate or reproduce the vulnerable behavior.
4. Explain the root cause.
5. Propose mitigations.
6. Discuss operational trade-offs.
7. Capture residual risk.

## Defensive design patterns

- Keep security decisions outside the model where possible.
- Treat model input and output as untrusted.
- Apply least privilege to data, tools, and workflows.
- Validate tool arguments and enforce authorization per action.
- Log security-relevant events.
- Rate-limit expensive or sensitive operations.
- Add human approval for destructive or high-impact actions.
- Build monitoring for abuse, drift, and unexpected behavior.

## Discussion questions

1. What is the highest-value asset in this scenario?
2. Where are the trust boundaries?
3. What does the model know?
4. What can the model do?
5. What should the model not be allowed to decide?
6. What would you fix first?
7. What would you monitor?
8. What residual risk remains?

## Deliverable

Final security review, executive summary, risk register, and residual-risk statement.

## Instructor notes

Students may focus too much on clever prompts or exploit strings. Bring the discussion back to architecture, permissions, system boundaries, workflow design, and risk decisions.

A good answer should include both offensive understanding and defensive judgment.

## Review questions

1. What is the core risk in this module?
2. Which classic security principles apply?
3. What makes the AI version of the problem different?
4. What mitigation is strongest?
5. What mitigation is weakest if used alone?

## Suggested reading

See [`../../references.md`](../../references.md).
