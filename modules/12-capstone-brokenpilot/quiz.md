# Module 12 Quiz  -  BrokenPilot Capstone

## Questions

### 1. What is the main goal of the BrokenPilot capstone?

A. Find the most clever jailbreak prompt.  
B. Prove that AI systems should not use tools.  
C. Connect architecture, attack paths, mitigations, and residual risk.  
D. Test only the model in isolation.

### 2. Why is retrieval authorization important in a RAG system?

A. It improves token efficiency.  
B. It ensures documents are filtered according to user access before entering model context.  
C. It makes embeddings more accurate.  
D. It prevents all hallucinations.

### 3. Which statement is most correct?

A. Prompt injection is solved by writing a stronger system prompt.  
B. Prompt injection matters most when model behavior can affect data access, decisions, or actions.  
C. Prompt injection is only a model provider problem.  
D. Prompt injection is unrelated to classic security principles.

### 4. What is the best place to enforce authorization for a ticket update tool?

A. In the model prompt only.  
B. In the user interface only.  
C. In the tool gateway or backend API at execution time.  
D. In the final report.

### 5. Why can agent memory become a security problem?

A. It always reduces model quality.  
B. It can persist untrusted or sensitive information across tasks.  
C. It prevents tool calling.  
D. It removes the need for logs.

### 6. What should a high-quality AI security finding include?

A. A screenshot only.  
B. A prompt payload only.  
C. Impact, evidence, root cause, and recommended mitigation.  
D. A list of model opinions.

### 7. Which control best addresses excessive agency?

A. Give the model broader tool access.  
B. Remove all logging.  
C. Require approval gates and per-action authorization for high-impact actions.  
D. Store all context in memory.

### 8. What does “security decisions outside the model” mean?

A. The model should never be used.  
B. The model may suggest, but deterministic application controls enforce policy.  
C. Security teams should not review prompts.  
D. All decisions should be manual.

### 9. What is a residual-risk statement?

A. A claim that all risk has been eliminated.  
B. A description of remaining risk after controls and mitigations.  
C. A list of rejected prompts.  
D. A model configuration file.

### 10. Why should logs include retrieved document IDs and tool calls?

A. To increase latency.  
B. To reconstruct security-relevant events during review or incident response.  
C. To expose sensitive data to all users.  
D. To replace authorization controls.

## Answer key

1. C
2. B
3. B
4. C
5. B
6. C
7. C
8. B
9. B
10. B

## Discussion answers

### 1. What is the difference between a weak and strong AI security finding?

A weak finding describes only model behavior, such as “we jailbroke it.” A strong finding explains the security property that failed, the affected asset, the attacker persona, the evidence, the impact, and the control that should change.

### 2. Why is “better prompting” not enough?

Prompts influence model behavior but do not reliably enforce access control, authorization, validation, approval, or auditability. Critical controls must be enforced by application logic, policy engines, tool gateways, and backend systems.

### 3. How should teams balance security and developer velocity?

Use risk-based controls. Low-impact read-only workflows may allow lightweight controls. High-impact actions need stricter authorization, approval, logging, and rollback. The goal is not to block useful AI, but to scope and observe it safely.
