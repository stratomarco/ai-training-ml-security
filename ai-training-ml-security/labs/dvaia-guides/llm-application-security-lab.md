# Lab — LLM Application Security with DVAIA

## Purpose

This lab uses a deliberately vulnerable AI application environment to practice LLM application security review.

The objective is not only to make a prompt injection work. The objective is to connect each behavior to:

- affected asset
- trust boundary
- root cause
- impact
- mitigation
- residual risk

## Safety boundary

Run this lab only in a local, intentionally vulnerable environment.

Do not test these techniques against systems you do not own or have explicit permission to assess.

Do not use real secrets, real customer data, real tokens, or production integrations.

## Lab setup

Use the selected DVAIA environment for hands-on testing.

Recommended preparation:

1. Install the lab locally.
2. Use fake/demo model credentials if required.
3. Prefer local models where practical.
4. Disable production integrations.
5. Use synthetic data only.
6. Reset the lab state after each exercise.

## Lab learning objectives

By the end of the lab, students should be able to:

1. Demonstrate direct prompt injection in a toy environment.
2. Explain why the behavior happened.
3. Identify insecure output handling risk.
4. Identify sensitive data disclosure paths.
5. Explain basic model DoS risk.
6. Propose controls outside the model.
7. Write a concise vulnerability report.

## Exercise 1 — Direct prompt injection

### Goal

Show that user-controlled language can conflict with the application’s intended instruction hierarchy.

### Student task

1. Interact with the assistant as a normal user.
2. Identify the intended behavior.
3. Attempt to make the assistant violate the intended behavior using only the lab interface.
4. Record what changed.
5. Explain the root cause.

### Analysis questions

- What did the attacker control?
- What instruction was the model supposed to follow?
- Did the application rely on the prompt as a security boundary?
- What would be the impact in a real system?
- Which external control would reduce impact?

### Expected mitigation themes

- Do not expose sensitive context unnecessarily.
- Enforce authorization outside the model.
- Limit what the model can do.
- Add output validation.
- Add monitoring for suspicious prompt patterns.

## Exercise 2 — System prompt leakage attempt

### Goal

Understand why system prompt secrecy should not be treated as the primary security control.

### Student task

1. Attempt to obtain hidden instructions in the lab.
2. Record whether the attempt succeeds or fails.
3. Assess the real impact.
4. Identify what sensitive material should not be placed in prompts.

### Analysis questions

- Did the system prompt contain secrets?
- Would disclosure create security impact?
- What should be stored in configuration or policy instead?
- What should be assumed visible to attackers?

### Expected mitigation themes

- Do not put secrets in prompts.
- Treat prompts as potentially discoverable.
- Version and review prompt templates.
- Keep enforcement in code/policy.

## Exercise 3 — Insecure output handling

### Goal

Analyze how generated content can become dangerous when rendered or executed downstream.

### Student task

1. Identify where model output appears in the application.
2. Determine whether output is rendered as Markdown, HTML, JSON, code, or commands.
3. Test whether unsafe content is reflected or rendered.
4. Explain the downstream interpreter risk.

### Analysis questions

- Is the model output treated as trusted?
- Is HTML or Markdown sanitized?
- Could output become script, SQL, shell, or API arguments?
- What downstream component is at risk?

### Expected mitigation themes

- Validate output structure.
- Encode before rendering.
- Sanitize Markdown/HTML.
- Avoid direct execution.
- Use allowlists for generated actions.

## Exercise 4 — Sensitive information disclosure

### Goal

Identify how sensitive data can leak through context, retrieval, logs, or responses.

### Student task

1. Identify what context is available to the model.
2. Identify whether the user is authorized for that context.
3. Attempt to cause the model to reveal information outside the intended task.
4. Record the disclosure path.

### Analysis questions

- Was sensitive data inserted into the prompt?
- Was authorization checked before retrieval?
- Was the model asked to enforce confidentiality by prompt alone?
- Would logs contain the disclosed data?

### Expected mitigation themes

- Authorize before retrieval.
- Minimize context.
- Redact sensitive fields.
- Avoid broad document retrieval.
- Protect logs.

## Exercise 5 — Model DoS and cost abuse review

### Goal

Understand availability and cost risks in LLM applications.

### Student task

1. Identify inputs that may increase token usage.
2. Identify loops or repeated actions.
3. Identify expensive tool calls.
4. Propose budget controls.

### Analysis questions

- Are input sizes limited?
- Are token budgets enforced?
- Are tool calls bounded?
- Are retries bounded?
- Are costs monitored per user or tenant?

### Expected mitigation themes

- Token budgets.
- Rate limits.
- Timeouts.
- Per-user and per-tenant quotas.
- Tool-call limits.
- Abuse monitoring.

## Exercise 6 — Overreliance scenario

### Goal

Understand how trusting model output can become a security or operational risk.

### Student task

1. Find a task where the application presents generated output as authoritative.
2. Identify what evidence supports the answer.
3. Identify what human review is needed.
4. Propose a safer workflow.

### Analysis questions

- Does the model cite sources?
- Can the user verify the answer?
- Is the output used for a high-impact decision?
- What happens if the answer is wrong?

### Expected mitigation themes

- Source citations.
- Confidence communication.
- Human review.
- Evaluation tests.
- Clear limitations.

## Final lab deliverable

Students submit a short report with:

| Section | Required content |
|---|---|
| Summary | What was tested |
| Findings | At least three LLM application security findings |
| Evidence | Screenshots or concise reproduction steps |
| Root cause | Why each issue exists |
| Impact | What could happen in a real system |
| Mitigation | Engineering controls, not only prompt changes |
| Residual risk | What remains after mitigation |

## Grading rubric

| Area | Strong answer |
|---|---|
| Vulnerability understanding | Explains root cause, not only payload |
| Impact | Connects behavior to realistic business risk |
| Mitigation | Places control in the right system layer |
| Security engineering | Uses least privilege, complete mediation, safe output handling |
| Communication | Clear, concise, actionable |
