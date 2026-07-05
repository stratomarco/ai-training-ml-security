# Module 07 Quiz  -  Agent and Tool Security

## Questions

### 1. What is the most important security difference between a chatbot and an agent?

A. Agents always use larger models.  
B. Agents can take actions through tools and workflows.  
C. Chatbots cannot be attacked.  
D. Agents do not need authentication.

### 2. Why is a system prompt not a sufficient security boundary for an agent?

A. Prompts are too short.  
B. Models may ignore, misinterpret, or be manipulated away from prompt instructions.  
C. Prompts cannot contain security rules.  
D. Prompts only work for image models.

### 3. Which tool is generally safer?

A. `run_shell(command)`  
B. `query_database(sql)`  
C. `run_approved_diagnostic(check_name, target_id)`  
D. `send_email(to, subject, body)`

### 4. What does per-action authorization mean?

A. The user logs in once and all tool use is allowed.  
B. Every tool call is checked against user, agent, target object, action, arguments, and context.  
C. The model decides if the action is safe.  
D. Authorization happens only during deployment.

### 5. What is memory poisoning?

A. A model uses too much GPU memory.  
B. Malicious or false information is persisted in agent memory and influences future behavior.  
C. A vector database runs out of disk space.  
D. A user forgets their password.

### 6. Which action most likely requires approval?

A. Summarizing a public document.  
B. Listing allowed ticket IDs.  
C. Sending a customer-facing email.  
D. Explaining what a tool does.

### 7. Why are shared broad service accounts risky for agents?

A. They are slower.  
B. They make actions hard to attribute and often grant more privilege than needed.  
C. They prevent logging.  
D. They only work with old models.

### 8. What should an approval gate show?

A. Only the model's confidence score.  
B. The exact action, target, arguments, evidence, risk tier, and rollback path.  
C. Only the original user prompt.  
D. Nothing, because approvals should be automatic.

### 9. What is the safest approach for diagnostic tools?

A. Give the agent unrestricted shell access.  
B. Allow free-form commands if the prompt says to be careful.  
C. Provide allowlisted diagnostics with validated targets in a sandbox.  
D. Disable logging to protect privacy.

### 10. Who should enforce the final authorization decision for a tool call?

A. The model only.  
B. The user only.  
C. A policy/tool layer outside the model.  
D. The retrieved document.

## Answer key

1. B
2. B
3. C
4. B
5. B
6. C
7. B
8. B
9. C
10. C

## Short-answer prompts

1. Explain why tool schemas help but do not replace authorization.
2. Give one example of tool misuse in an internal operations agent.
3. Describe one control for memory poisoning.
4. Explain how to balance approval gates with developer velocity.
5. Write a residual risk statement for an agent that can update internal tickets.

## Expected short-answer themes

Strong answers should mention:

- model output is untrusted;
- policy must be enforced outside the model;
- least privilege;
- per-action authorization;
- narrow tools;
- memory provenance and expiry;
- human approval for sensitive actions;
- audit logging;
- monitoring;
- rollback and incident response.
