# Module 04 Instructor Notes — BIML and Architectural Risk Analysis

## Instructor goal

The goal of this module is to shift students from vulnerability enumeration to architecture-level security reasoning.

By the end, students should understand that many AI security failures are not caused only by weak prompts or model misbehavior. They are caused by design choices that give untrusted model behavior access to sensitive data, privileged tools, unsafe rendering paths, or business workflows.

## Suggested duration

| Section | Time |
|---|---:|
| Introduction and framing | 10 min |
| BIML and building security in | 15 min |
| Architecture review method | 20 min |
| DocOps Assistant exercise | 35 min |
| Group discussion | 20 min |
| Quiz / recap | 10 min |
| Total | 110 min |

This can also be compressed into a 60-minute version by reducing group discussion and using only three abuse cases.

## Opening framing

Start with this statement:

> Prompt injection is not the root cause. It is often the trigger. The root cause is usually that the architecture trusted the wrong thing at the wrong boundary.

Then show the difference:

```text
Bad analysis:
The prompt was hacked.

Better analysis:
The system allowed untrusted text to override instructions.

Good analysis:
The application allowed model output influenced by untrusted text to invoke a privileged workflow without per-action authorization.
```

## How to explain BIML

Avoid making BIML sound like a compliance checklist.

Explain it as:

- a security engineering approach to ML systems
- a way to reason about ML lifecycle components
- a way to find risks before code is written
- a bridge between classic software security and ML-specific risk
- a risk catalog that supports architectural review

The point is not to memorize every BIML risk. The point is to use the architecture to ask structured questions.

## Key concepts to emphasize

### 1. Design-level risk

A design-level risk exists even if the implementation is clean.

Example:

> A model is allowed to decide whether a ticket update is authorized.

Even if the code has no bug, the design is risky because authorization should not depend on probabilistic natural-language behavior.

### 2. Untrusted AI boundaries

Students should treat these as untrusted:

- user prompt
- model output
- retrieved documents
- embeddings generated from untrusted content
- tool arguments suggested by the model
- memory written by the model
- feedback submitted by users
- model artifacts from external sources
- datasets from external sources

### 3. Security controls outside the model

Ask students to identify which controls belong outside the model.

Examples:

- authorization
- output encoding
- approval gates
- secrets handling
- rate limiting
- tenant isolation
- audit logging
- policy enforcement
- retrieval access control

### 4. Residual risk

Students often stop after recommending mitigations.

Push them to state what remains risky.

Example:

> Even after retrieval authorization and source labeling, malicious documents may still influence summaries. The remaining risk is reduced because the assistant no longer has write access without approval, all retrievals are logged, and sensitive actions require explicit user confirmation.

## Teaching flow

### Step 1 — Start with a familiar system

Use a normal internal assistant:

```text
User asks question -> app builds prompt -> model responds -> UI displays answer
```

Ask: Where are the trust boundaries?

### Step 2 — Add retrieval

```text
User asks question -> app retrieves documents -> model summarizes docs -> UI displays answer
```

Ask: What changed?

Expected answers:

- retrieved documents become model input
- document permissions matter
- document provenance matters
- malicious content can influence output
- summaries can leak information

### Step 3 — Add tools

```text
Model can update tickets or send messages
```

Ask: What changed?

Expected answers:

- model output can cause action
- authorization is now critical
- approval gates may be needed
- logs become security evidence
- tool scope matters

### Step 4 — Add memory and feedback

Ask: What changed?

Expected answers:

- attacker influence may persist
- future users may be affected
- feedback loops can poison future behavior
- retention/privacy questions arise

## Common student mistakes

### Mistake: Treating prompts as hard controls

Correction:

> Prompts guide model behavior. They are not reliable security boundaries.

### Mistake: Focusing only on model behavior

Correction:

> Ask what the application does with the model output.

### Mistake: Ignoring authorization in RAG

Correction:

> Retrieval must be authorized before content enters the model context.

### Mistake: No residual risk statement

Correction:

> Security review must end with what remains possible and who owns that risk.

### Mistake: Recommending vague mitigations

Correction:

> Replace “add guardrails” with concrete controls: retrieval ACLs, scoped tool tokens, approval gates, output encoding, egress filtering, logging.

## Facilitator prompts

Use these during the exercise:

- What is the asset?
- Who controls the input?
- Is this data or instruction?
- Does this cross a trust boundary?
- What privilege does the model have?
- Which component enforces authorization?
- What happens if the model is wrong?
- What happens if a document is malicious?
- What happens if a user is malicious?
- What happens if a tool call succeeds incorrectly?
- What is logged?
- Can the organization investigate later?
- What would you block before production?

## Expected strong findings in the exercise

Students should identify at least these risks:

1. Untrusted document content enters prompt context.
2. Retrieved documents are not filtered by user authorization.
3. Model output is used to suggest or trigger ticket updates.
4. Tool token is too broad.
5. No human approval for high-impact actions.
6. Memory can persist malicious instructions.
7. Logs may contain sensitive prompt and retrieved data.
8. Output renderer treats model output as trusted content.
9. No clear incident response or rollback process.
10. No monitoring for prompt injection or abnormal tool calls.

## Good mitigation examples

- Retrieval service enforces document ACLs before retrieval.
- Retrieved context is labeled as untrusted data.
- Tool broker validates arguments and checks authorization per action.
- Destructive/high-impact actions require human approval.
- Model output is encoded before rendering.
- Tool credentials are scoped to the user and action.
- Memory writes require classification and review.
- Sensitive data is redacted from logs.
- Model gateway applies rate limits and budget controls.
- Security events are logged and monitored.

## Suggested closing statement

> BIML-style architecture review helps us move from “Can we break this?” to “Why can this be broken, where should the control live, and what risk remains?”
