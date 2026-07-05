# Module 6 Quiz  -  RAG Security and Indirect Prompt Injection

## Questions

### 1. What is the main security lesson of this module?

A. RAG removes the need for access control  
B. Retrieved content should be treated as untrusted input  
C. Vector databases automatically enforce document permissions  
D. Citations prove that an answer is safe  

### 2. What is indirect prompt injection?

A. A user directly asks the model to ignore instructions  
B. A model hallucinates an answer  
C. Malicious instructions are hidden in content the model later retrieves or reads  
D. A vector database returns no results  

### 3. Why is “retrieve everything and tell the model not to reveal restricted content” a weak design?

A. It is too slow  
B. It exposes unauthorized content to the model before enforcement  
C. It requires too many citations  
D. It only works with local models  

### 4. Which statement is correct?

A. Embeddings are an access-control mechanism  
B. Semantic similarity is equivalent to authorization  
C. Vector search should be combined with policy filters  
D. Prompt templates replace document permissions  

### 5. Which metadata should usually survive chunking?

A. Tenant, owner, classification, source ID, and access policy  
B. Only the text body  
C. Only the embedding vector  
D. Only the file name  

### 6. What is citation laundering?

A. Encrypting citations  
B. Using a citation to make an incorrect or unsafe answer appear trustworthy  
C. Removing citations from output  
D. Sorting sources alphabetically  

### 7. Where should authorization happen in a secure RAG design?

A. Only in the model prompt  
B. Only after the model generates an answer  
C. Before unauthorized context reaches the model, usually in the retrieval/data layer  
D. Only in the UI  

### 8. Give two examples of sources that may contain indirect prompt injection.

Free response.

### 9. Name three controls that reduce RAG data leakage risk.

Free response.

### 10. What should be logged for RAG security investigation without over-collecting sensitive data?

Free response.

## Answer key

1. B
2. C
3. B
4. C
5. A
6. B
7. C
8. Examples: webpage, email, ticket, wiki page, markdown file, PDF, source code comment, vendor document.
9. Examples: pre-retrieval authorization, tenant filters, classification filters, metadata-preserving chunking, source trust scoring, output validation, sensitive data exclusion, protected logs, adversarial tests.
10. Useful logs include user identity, query, retrieved document IDs, source classifications, policy decisions, blocked retrievals, model ID, output metadata, and tool calls. Raw prompts and chunks should be minimized, redacted, or access-controlled.
