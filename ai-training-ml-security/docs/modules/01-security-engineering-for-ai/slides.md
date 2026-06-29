# Module 01 Slides — Security Engineering for AI

These slides are written in Markdown so they can be used directly in GitHub, converted with tools such as Marp, or copied into a presentation later.

---

# 1. Security Engineering for AI

## Core idea

AI security starts with security engineering.

Machine learning changes the attack surface, but it does not remove classic security problems.

**Speaker notes:**
Open by setting the tone. This is not a prompt-hacking course. This is a course about securing systems that contain ML, LLMs, RAG, and agents.

---

# 2. The central claim

> The model is not the security boundary.

The system around the model must enforce security.

**Speaker notes:**
This is the most important sentence in the module. Repeat it throughout the course. Prompts can guide behavior, but they should not be responsible for access control, authorization, data isolation, transaction approval, or auditability.

---

# 3. Why this matters now

AI systems are being connected to:

- Internal documents
- Customer data
- Ticketing systems
- Source code
- Cloud APIs
- Email
- Calendars
- Databases
- CI/CD workflows
- Security tools

**Speaker notes:**
A chatbot that only talks is one risk category. An assistant that can retrieve data and use tools is an application with privileges. An agent that can plan and act is a workflow automation system with a probabilistic decision-making component.

---

# 4. AI systems still fail like software

Common failures still matter:

- Broken access control
- Injection
- Insecure output handling
- SSRF-style tool abuse
- Secrets exposure
- Weak authentication
- Weak authorization
- Poor logging
- Supply chain compromise
- Insecure defaults

**Speaker notes:**
The course should not create the impression that AI security is completely new. The new part is how old problems appear through model interfaces, prompts, retrieved content, tools, and autonomous workflows.

---

# 5. What is different?

AI systems introduce unusual components:

- Training data
- Model artifacts
- Embeddings
- Vector databases
- Prompts
- System instructions
- Retrieved context
- Model outputs
- Tool calls
- Memory
- Feedback loops

**Speaker notes:**
Ask students: which of these are code, which are data, and which are policy? The uncomfortable answer is that some of them act like all three depending on context.

---

# 6. Data becomes part of behavior

In traditional software, source code mostly defines behavior.

In ML systems, behavior also comes from:

- Training data
- Fine-tuning data
- System prompts
- Retrieved documents
- Feedback signals
- Tool responses

**Speaker notes:**
This is where ML security expands beyond AppSec. A poisoned dataset or malicious retrieved document can influence behavior without changing source code.

---

# 7. Prompts are not policy enforcement

A system prompt can say:

> “Never reveal confidential data.”

But real enforcement should happen in:

- Authorization checks
- Retrieval filters
- Data access controls
- Tool permissions
- Output validation
- Audit logs
- Human approval gates

**Speaker notes:**
Make clear that prompts are useful. The problem is treating them as sufficient. A prompt can be one layer, not the control plane.

---

# 8. Classic principle: least privilege

For AI systems, least privilege applies to:

- Users
- Model access
- Retrieved data
- Tool permissions
- Agent actions
- API tokens
- Memory
- Logs
- Training data

**Speaker notes:**
A common anti-pattern is giving the AI assistant a broad service account and relying on the prompt to decide what the user should see. That is broken authorization with extra steps.

---

# 9. Classic principle: complete mediation

Every sensitive action should be checked every time.

For AI systems, check:

- User identity
- User authorization
- Data access rights
- Tool arguments
- Action type
- Business impact
- Approval requirements

**Speaker notes:**
Complete mediation is especially important for agents. The model suggesting an action is not the same as the system authorizing that action.

---

# 10. Classic principle: fail-safe defaults

When uncertain, the system should fail closed.

Examples:

- No retrieved document access without authorization
- No destructive tool calls without approval
- No cross-tenant search by default
- No hidden tool invocation
- No silent data export

**Speaker notes:**
AI systems can be uncertain often. If uncertainty leads to permissive behavior, the system is dangerous.

---

# 11. Classic principle: defense in depth

A secure AI system may need:

- Authentication
- Authorization
- Retrieval filtering
- Prompt hardening
- Tool allowlists
- Schema validation
- Policy engine
- Output validation
- Rate limiting
- Monitoring
- Human approval

**Speaker notes:**
No single guardrail is enough. The right question is not “which one control stops prompt injection?” but “what happens after prompt injection succeeds?”

---

# 12. Threat modeling questions

Ask:

1. What are the assets?
2. Who are the users?
3. Who are the attackers?
4. What are the trust boundaries?
5. What can the model see?
6. What can the model do?
7. What data is untrusted?
8. What happens when the model is wrong?

**Speaker notes:**
These questions are intentionally simple. They work before we introduce OWASP, BIML, MITRE ATLAS, or NIST mappings.

---

# 13. AI-specific trust boundaries

Common boundaries:

- User input to app
- App to model provider
- App to retrieval system
- Retrieval system to document store
- Model output to renderer
- Model output to tool execution
- Agent memory to future sessions
- Logs to analytics or training pipelines

**Speaker notes:**
Many AI incidents happen when teams fail to mark retrieved documents, tool output, or memory as untrusted input.

---

# 14. Prompt injection as architecture failure

Prompt injection is not just “bad words in a prompt.”

It often combines:

- Untrusted input
- Confused deputy behavior
- Weak authorization
- Mixed instructions and data
- Excessive tool privileges
- Weak output handling

**Speaker notes:**
This helps students avoid the trap of thinking the solution is a better system prompt. Good prompting helps; architecture is still required.

---

# 15. RAG as an input-validation problem

Retrieved documents are input.

They may be:

- Incorrect
- Outdated
- Unauthorized
- Malicious
- Cross-tenant
- Poisoned
- Instruction-bearing

**Speaker notes:**
A retrieved document can contain instructions to the model. The app must treat retrieved text as content, not policy.

---

# 16. Agents as authorization problems

Once a model can use tools, ask:

- Which tools exist?
- Who may use them?
- What arguments are allowed?
- What actions need approval?
- What is logged?
- How can we recover?

**Speaker notes:**
Agent security is mostly workflow security plus authorization plus monitoring. The model should not be the root of trust.

---

# 17. Practical guardrail hierarchy

Prefer controls that are:

1. Deterministic
2. Enforced outside the model
3. Testable
4. Auditable
5. Fail-closed
6. Easy for developers to use

**Speaker notes:**
This slide introduces the course’s design bias. We want controls that support developer velocity rather than one-off fragile prompts.

---

# 18. Balancing security and velocity

Good controls should:

- Reduce high-impact risk
- Avoid blocking safe use cases
- Be easy to integrate
- Provide clear failure modes
- Produce useful logs
- Support progressive rollout

**Speaker notes:**
Security that is impossible to adopt will be bypassed. The goal is not maximum restriction. The goal is appropriate control for the risk.

---

# 19. Exercise: DocAssist threat model

Scenario:

DocAssist is an internal AI assistant that summarizes company documents.

It can:

- Search internal documents
- Retrieve snippets
- Summarize answers
- Store chat history
- Log prompts and responses

Student tasks:

- Identify assets
- Draw trust boundaries
- Write abuse cases
- Propose mitigations
- Discuss residual risk

**Speaker notes:**
Move students into groups if possible. Keep them focused on system design rather than clever prompts.

---

# 20. Closing message

ML Security is not separate from security engineering.

It is security engineering applied to systems where:

- Models influence behavior
- Data acts like code
- Prompts shape execution
- Retrieval expands context
- Tools create action
- Agents automate workflows

**Speaker notes:**
End by connecting to the next module: before we attack ML systems, we need to understand the ML lifecycle and system architecture.
