# Quiz  -  Module 01: Security Engineering for AI

## Student questions

### 1. What is the most important security message from this module?

A. The system prompt should contain all security rules.  
B. The model is not the security boundary.  
C. AI security is unrelated to software security.  
D. Prompt injection can always be solved with filtering.

### 2. Which control is strongest for preventing unauthorized document retrieval in a RAG system?

A. Ask the model not to reveal confidential documents.  
B. Add a warning in the UI.  
C. Enforce user authorization before retrieved chunks enter the model context.  
D. Increase the model temperature.

### 3. Why is retrieved content risky?

A. It is always encrypted.  
B. It is always too large.  
C. It may be malicious, unauthorized, outdated, or instruction-bearing.  
D. It cannot influence model behavior.

### 4. In an agent system, tool execution should be treated primarily as what kind of problem?

A. Authorization and workflow security.  
B. CSS styling.  
C. User interface preference.  
D. Model creativity.

### 5. Which of the following is an AI-specific version of insecure output handling?

A. Rendering model-generated HTML without validation or encoding.  
B. Using TLS for API calls.  
C. Rotating service account keys.  
D. Applying least privilege.

### 6. What is wrong with giving an AI assistant a broad service account and relying on the prompt to control access?

A. It is always cheaper.  
B. It moves authorization into a probabilistic component that can be manipulated or fail.  
C. It prevents all prompt injection.  
D. It makes logging unnecessary.

### 7. Which statement best describes prompt injection?

A. It is only a problem with weak passwords.  
B. It is only a user-interface issue.  
C. It can combine untrusted input, confused deputy behavior, weak authorization, and mixed instructions/data.  
D. It is impossible in RAG systems.

### 8. What should be logged in an AI system?

A. Nothing. Logging is always unsafe.  
B. Everything forever, including all sensitive data.  
C. Security-relevant events with appropriate minimization, redaction, access control, and retention.  
D. Only model temperature settings.

### 9. Which mitigation is usually weakest if used alone?

A. Per-action authorization.  
B. Permission-aware retrieval.  
C. Prompt hardening.  
D. Scoped service accounts.

### 10. What is residual risk?

A. The risk that remains after controls are applied.  
B. A type of model parameter.  
C. The risk that exists only before design review.  
D. A log format.

## Short-answer questions

### 11. List three trust boundaries in a RAG-based AI assistant.

### 12. Give one example of an abuse case for an internal document assistant.

### 13. Explain why model output should be treated as untrusted.

### 14. What is one practical way to balance security and developer velocity in AI systems?

### 15. What is the difference between “the model refused” and “the system prevented”?

---

# Answer key

## Multiple choice

1. B
2. C
3. C
4. A
5. A
6. B
7. C
8. C
9. C
10. A

## Short-answer guidance

### 11. List three trust boundaries in a RAG-based AI assistant.

Good answers include:

- User/browser to application
- Application to identity provider
- Application to retrieval service
- Retrieval service to document store
- Application to vector database
- Application to model gateway/provider
- Model output to web renderer
- Logs to monitoring system

### 12. Give one example of an abuse case for an internal document assistant.

Example:

```text
As an employee with limited access, I want the assistant to summarize documents I cannot open directly, so that I can learn confidential project information.
```

### 13. Explain why model output should be treated as untrusted.

Good answers mention that model output can be incorrect, manipulated, unsafe to render, unsafe to execute, or influenced by untrusted input and retrieved content.

### 14. What is one practical way to balance security and developer velocity in AI systems?

Good answers include reusable authorization middleware, tool allowlists, approval gates only for high-risk actions, standard logging wrappers, secure prompt templates, or permission-aware retrieval built into the platform.

### 15. What is the difference between “the model refused” and “the system prevented”?

A model refusal is behavioral and probabilistic. The model may refuse based on instructions or training, but it can be manipulated or fail. System prevention means a deterministic control outside the model blocked unauthorized access or action.
