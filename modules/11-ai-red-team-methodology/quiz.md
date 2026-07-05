# Module 11 Quiz  -  AI Red Team Methodology

## Questions

### 1. What is the main goal of AI red teaming?

A. Produce the most creative jailbreak possible.  
B. Prove that all models are unsafe.  
C. Identify realistic ways adversaries can cause unsafe or unauthorized outcomes and turn findings into engineering decisions.  
D. Replace threat modeling.

### 2. Why is scope especially important for AI red teaming?

A. Because AI systems are always small.  
B. Because AI tests may involve models, tools, data, logs, memory, and workflows, and unsafe actions must be bounded.  
C. Because scope only matters for compliance.  
D. Because the model decides the scope.

### 3. Which evidence is most useful for an agent tool-misuse finding?

A. Only the final model response.  
B. Only a screenshot of a chatbot.  
C. The user input, retrieved context, model output, tool-call request, tool-call response, logs, and impact.  
D. The model provider name only.

### 4. What is wrong with a finding that only says “the model was jailbroken”?

A. Nothing; that is enough.  
B. It does not explain impact, root cause, affected component, violated security property, or remediation.  
C. It is too technical.  
D. It should always be critical severity.

### 5. Which control is strongest for preventing unauthorized tool actions?

A. A longer system prompt.  
B. Per-action authorization enforced outside the model.  
C. Asking the model to be careful.  
D. Hiding the tool names.

### 6. What should severity be based on?

A. How clever the prompt is.  
B. Whether the model sounded confident.  
C. Impact, exposure, privilege, reproducibility, blast radius, detectability, and compensating controls.  
D. The number of tokens used.

### 7. In a RAG red team test, why is retrieved content dangerous?

A. It is always private.  
B. It can be attacker-controlled input that influences the model.  
C. It cannot affect the model.  
D. It is automatically trusted because it came from a vector database.

### 8. What is residual risk?

A. Risk that remains after controls and mitigations are applied.  
B. Risk that does not need to be documented.  
C. Risk that only exists before testing.  
D. Risk created by logs only.

### 9. What is a good executive readout focused on?

A. Raw prompts only.  
B. Long transcripts with no interpretation.  
C. Scope, major risks, business impact, remediation priorities, decisions needed, and residual risk.  
D. Model architecture diagrams only.

### 10. Why should AI red teaming feed back into secure design?

A. Because red team exercises are complete only when the model says no.  
B. Because findings should improve architecture, controls, monitoring, incident response, governance, and release decisions.  
C. Because mitigations are impossible.  
D. Because prompts are permanent controls.

## Answer key

1. C
2. B
3. C
4. B
5. B
6. C
7. B
8. A
9. C
10. B
