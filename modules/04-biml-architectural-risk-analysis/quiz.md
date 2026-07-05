# Quiz  -  BIML and Architectural Risk Analysis

## Questions

### 1. What is the main purpose of architectural risk analysis?

A. To replace penetration testing  
B. To identify design-level security risks before implementation  
C. To generate jailbreak prompts  
D. To measure model benchmark accuracy

### 2. Why is BIML useful for ML Security training?

A. It treats ML security as an architecture and security engineering problem  
B. It provides a replacement for authentication  
C. It eliminates the need for threat modeling  
D. It only focuses on prompt engineering

### 3. Which is a design-level risk?

A. A typo in an error message  
B. A CSS alignment issue  
C. The system allows the model to decide whether a privileged tool action is authorized  
D. A missing comma in a configuration file

### 4. Which control should usually live outside the model?

A. Authorization  
B. Natural language generation  
C. Summarization style  
D. Tone adjustment

### 5. Why is retrieved content risky in a RAG system?

A. It is always too large  
B. It may be untrusted content inserted into the model context  
C. It prevents all prompt injection  
D. It removes the need for access control

### 6. What is an abuse case?

A. A normal user story  
B. A performance benchmark  
C. A description of how an attacker may misuse the system  
D. A model card

### 7. Which is the strongest requirement?

A. Add guardrails  
B. Make the model safer  
C. The retrieval service must enforce document ACLs before context insertion  
D. Tell users not to attack the system

### 8. Why is memory risky in an AI assistant?

A. It always improves security  
B. It can persist attacker-controlled instructions or sensitive data  
C. It prevents data leakage  
D. It removes the need for logging

### 9. What should a residual risk statement explain?

A. Only the fixed bugs  
B. Only the model benchmark score  
C. What can still go wrong after mitigations and who owns the risk  
D. The marketing benefits of the feature

### 10. Which statement is most correct?

A. Prompt injection is always the root cause  
B. Prompt injection is often a trigger; the root cause is frequently architectural trust failure  
C. Prompt injection is impossible in internal systems  
D. Prompt injection is solved by longer system prompts

## Answer key

1. B
2. A
3. C
4. A
5. B
6. C
7. C
8. B
9. C
10. B

## Discussion answers

### 1. Architectural risk analysis

Architectural risk analysis identifies security risks in the design before they become expensive implementation problems. For AI systems, this includes model, data, prompt, retrieval, tool, memory, feedback, and workflow design.

### 2. BIML value

BIML is useful because it applies security engineering to ML systems. It helps students reason about lifecycle and architecture instead of only memorizing attack names.

### 3. Design-level risk

A design-level risk is created by the system structure. If the model is allowed to authorize privileged actions, that is a flawed design even if every line of code works as intended.

### 4. Controls outside the model

Authorization, access control, tool permissions, output encoding, logging, and approvals should not depend only on model behavior.

### 5. RAG risk

RAG systems insert retrieved content into the model context. If the content is malicious, unauthorized, stale, or sensitive, it can affect confidentiality, integrity, and decision quality.

### 6. Abuse cases

Abuse cases make attacker intent explicit. They help convert vague concerns into reviewable scenarios.

### 7. Strong requirements

Strong requirements are specific, testable, and owned by a component or team. “Add guardrails” is too vague.

### 8. Memory risk

Memory can increase usability, but it can also store sensitive data, attacker instructions, or stale assumptions that affect future interactions.

### 9. Residual risk

Residual risk is what remains after mitigation. It must be documented, owned, monitored, and revisited.

### 10. Prompt injection root cause

Prompt injection is often the visible trigger. The serious engineering question is why untrusted text was allowed to affect sensitive data, privileged actions, or business decisions.
