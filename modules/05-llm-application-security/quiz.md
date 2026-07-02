# Module 5 Quiz  -  LLM Application Security

## Questions

### 1. Why are prompts not hard security boundaries?

A. Because users cannot see them  
B. Because models are expensive  
C. Because untrusted input can influence model behavior and prompts cannot reliably enforce policy  
D. Because prompts are always public

### 2. What is indirect prompt injection?

A. A prompt written in another language  
B. A malicious instruction placed in content the model later reads  
C. A prompt sent through an API  
D. A prompt that uses encoded characters

### 3. Which is the best place to enforce document access control in a RAG application?

A. In the model’s system prompt  
B. Before retrieving or injecting documents into the model context  
C. In the final answer after generation  
D. In the user’s browser only

### 4. Why is insecure output handling dangerous?

A. LLM output is always too long  
B. LLM output may be passed to downstream interpreters such as HTML, SQL, shell, or code execution contexts  
C. LLM output cannot be logged  
D. LLM output is encrypted

### 5. Which is an example of excessive agency?

A. The assistant summarizes a public document  
B. The assistant answers a general question  
C. The assistant can delete records or trigger workflows without approval  
D. The assistant refuses to answer

### 6. Which control is most relevant to model denial of service?

A. Token budgets and rate limits  
B. Stronger fonts in the UI  
C. More detailed model cards only  
D. Disabling HTTPS

### 7. What is overreliance?

A. Using too many models  
B. Trusting model output beyond its reliability or evidence  
C. Running models on GPUs  
D. Using retrieval-augmented generation

### 8. Which statement is most correct?

A. LLM output should be trusted if it came from a trusted model provider.  
B. LLM output should be treated as untrusted when used by downstream systems.  
C. LLM output cannot contain attacker-controlled content.  
D. LLM output is safe if generated with temperature zero.

### 9. Which is a weak mitigation for sensitive disclosure?

A. Authorize retrieval before context injection  
B. Minimize context  
C. Redact secrets  
D. Put all data in the prompt and ask the model not to reveal secrets

### 10. What should a good LLM security finding include?

A. Only the prompt that worked  
B. Only a screenshot  
C. Impact, root cause, affected component, evidence, and mitigation  
D. Only the model name

## Answer key

1. C
2. B
3. B
4. B
5. C
6. A
7. B
8. B
9. D
10. C

## Discussion answers

### 1. Why are prompts not hard security boundaries?

Prompts guide behavior, but the model can still be influenced by user input, retrieved content, tool output, or ambiguous context. Security policy must be enforced by application controls outside the model.

### 2. What makes indirect prompt injection dangerous?

The malicious instruction is hidden in content the user may not notice, such as a document, webpage, email, ticket, or tool result. The model may treat that content as instruction rather than data.

### 3. Why should LLM output be treated as untrusted?

The output is influenced by untrusted input and model behavior. If passed to HTML, SQL, shell, code, or workflow systems, it can create classic security failures.

### 4. What is the main lesson of excessive agency?

A model should not have broad ability to act without external authorization, validation, and approval. The model may propose actions, but the system should enforce policy.
