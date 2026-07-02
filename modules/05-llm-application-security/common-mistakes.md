# Common Mistakes  -  LLM Application Security

This page lists common mistakes students and teams make when securing LLM applications. These mistakes are useful teaching moments because they reveal where teams confuse model behavior with system security.

## 1. Treating the system prompt as a security boundary

### Mistake

The team places security rules in the system prompt and assumes the model will enforce them.

### Why it is a problem

Prompts influence behavior, but they do not enforce authorization. The model can be confused by user input, retrieved documents, memory, or conflicting instructions.

### Better approach

Use prompts for behavior guidance. Use policy engines, data filters, and tool gateways for enforcement.

## 2. Giving the model unauthorized data and asking it not to reveal it

### Mistake

The application retrieves broad context and tells the model to show only what is relevant or allowed.

### Why it is a problem

If unauthorized data is in the context, the model may leak, summarize, transform, or infer from it.

### Better approach

Filter data before it reaches the model. Retrieval authorization should happen before prompt construction.

## 3. Treating retrieved content as trusted instruction

### Mistake

The application retrieves documents and places them in the prompt without clearly treating them as untrusted data.

### Why it is a problem

A malicious document can contain instructions aimed at the model. The user may ask a normal question while the retrieved document carries the attack.

### Better approach

Preserve source metadata, label retrieved content, enforce retrieval authorization, and prevent retrieved text from authorizing tool use.

## 4. Measuring security by whether one jailbreak string works

### Mistake

The team tests a few well-known jailbreak prompts and declares the system secure when they fail.

### Why it is a problem

LLM behavior changes across models, versions, phrasing, and context. Security should be based on system properties, not only refusal behavior.

### Better approach

Test attack paths and controls. Ask: if the model follows the malicious instruction, what prevents damage?

## 5. Letting the model decide authorization

### Mistake

The model decides whether a user should see a document or call a tool.

### Why it is a problem

Authorization requires deterministic checks against identity, role, tenant, object, and action. The model is not a reliable policy engine.

### Better approach

Use the application, retrieval layer, or tool gateway to enforce authorization.

## 6. Treating model output as safe because it is “just text”

### Mistake

The team renders LLM output directly as HTML/Markdown or passes it to downstream systems.

### Why it is a problem

Text can become executable or authoritative when interpreted by a browser, shell, SQL engine, workflow system, or human operator.

### Better approach

Apply output encoding, schema validation, allowlists, and approval workflows depending on the output sink.

## 7. Giving agents too many tools too early

### Mistake

The LLM gets broad tool access during early prototyping.

### Why it is a problem

A harmless chat assistant becomes an action-taking system. Prompt injection, memory poisoning, or model mistakes can now change system state.

### Better approach

Start with read-only tools, scoped credentials, dry-run mode, and explicit approval gates.

## 8. Ignoring logs and evidence

### Mistake

The team cannot reconstruct which prompt, retrieved documents, model version, and tools were involved in an incident.

### Why it is a problem

Without evidence, teams cannot debug failures, prove fixes, or explain residual risk.

### Better approach

Log security-relevant events: context sources, tool calls, authorization decisions, approvals, model version, and control decisions. Avoid logging unnecessary sensitive content.

## 9. Overcorrecting with unusable controls

### Mistake

The team blocks all retrieval, all tools, or all long answers after seeing an attack.

### Why it is a problem

Controls that destroy usability will be bypassed, disabled, or ignored.

### Better approach

Use risk-based controls: scoped access, approval for high-risk actions, safe defaults, rate limits, and targeted monitoring.

## 10. Reporting “the model was jailbroken” as the finding

### Mistake

The security report focuses on the clever prompt instead of the system failure.

### Why it is a problem

Engineering teams need to know what to fix. A jailbreak screenshot does not identify the violated trust boundary, affected asset, missing control, or validation test.

### Better approach

Report the system issue:

- unauthorized context reached the model
- model output reached an unsafe sink
- tool gateway failed to authorize the action
- sensitive action lacked approval
- retrieval lacked tenant filtering

## 11. Assuming vendor model safety solves application security

### Mistake

The team assumes a safer model means the application is secure.

### Why it is a problem

Provider-side safety may reduce some harmful outputs, but it cannot enforce your tenant model, business authorization, workflow approval, or data retention requirements.

### Better approach

Use provider safety as one layer. Build application-specific security controls around your data, users, and tools.

## 12. Forgetting human overreliance

### Mistake

The system presents answers confidently without helping users verify source, uncertainty, or action impact.

### Why it is a problem

People may follow plausible but wrong AI output, especially under time pressure.

### Better approach

Show sources, uncertainty, action impact, and verification steps. Require human approval for high-risk actions.
