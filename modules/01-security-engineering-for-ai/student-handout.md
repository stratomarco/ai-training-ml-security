# Module 01 Student Handout  -  Security Engineering for AI

## Core idea

AI security is not separate from security engineering.

It is security engineering applied to systems where models, datasets, prompts, retrieved context, tools, and agents influence behavior.

## Most important sentence

> The model is not the security boundary.

A model can help follow policy, but enforceable security controls should live outside the model wherever possible.

## What makes AI systems different?

AI systems may include:

- Training data
- Fine-tuning data
- Model artifacts
- Prompts
- System instructions
- Retrieved documents
- Embeddings
- Vector databases
- Model outputs
- Tool calls
- Memory
- Feedback loops

These components can influence system behavior. Some of them behave like data, code, and policy at the same time.

## Classic security principles still apply

| Principle | AI security interpretation |
|---|---|
| Least privilege | Give the app, model, tools, and service accounts only the access they need |
| Complete mediation | Check authorization for every sensitive retrieval or action |
| Fail-safe defaults | Deny uncertain or unauthorized operations by default |
| Defense in depth | Do not rely on one prompt, one filter, or one model refusal |
| Separation of duty | Keep model suggestion separate from final authorization |
| Input validation | Treat user input, retrieved documents, and tool output as untrusted |
| Output handling | Treat model output as untrusted before rendering or executing |
| Auditability | Log security-relevant decisions and actions |

## Common AI security anti-patterns

| Anti-pattern | Why it is risky |
|---|---|
| Broad service account for the assistant | Users may indirectly access data they should not see |
| Prompt-only policy | The model can be manipulated or confused |
| Unfiltered RAG retrieval | Unauthorized or malicious documents may enter context |
| Tool execution without authorization | The agent may perform actions beyond user permission |
| Blind trust in model output | Output can be wrong, malicious, or unsafe to render |
| No audit trail | Abuse and failures are hard to investigate |
| Storing all prompts forever | Sensitive data may accumulate in logs |

## Threat modeling questions

Use these questions for any AI-enabled application:

1. What are the assets?
2. Who are the users?
3. Who are the attackers?
4. What are the trust boundaries?
5. What data is trusted?
6. What data is untrusted?
7. What can the model see?
8. What can the model do?
9. What tools can the model call?
10. What permissions do those tools have?
11. What happens when the model is wrong?
12. What actions need human approval?
13. What should be logged?
14. What residual risk remains?

## Useful mental models

### Prompt injection

Prompt injection is not only a prompt problem. It can also be:

- An input handling problem
- A confused deputy problem
- An authorization problem
- A tool permission problem
- A data isolation problem
- An output handling problem

### RAG

Retrieved content is untrusted input.

Documents may contain malicious instructions, sensitive data, outdated data, or data the current user is not authorized to see.

### Agents

An agent is not only a chatbot. It is an application that can act.

Tool use should be controlled by deterministic authorization, scoped permissions, argument validation, logging, and approval gates.

## Exercise summary

You will threat model **DocAssist**, an internal AI assistant that summarizes company documents.

Your deliverables:

1. System/context diagram
2. Asset list
3. Trust boundary list
4. Abuse cases
5. Mitigation plan
6. Residual risk statement

## Final takeaway

Good AI security asks:

> What happens when the model is manipulated, wrong, overconfident, or given malicious context?

Then it designs the system so that failure is contained, visible, recoverable, and acceptable.
