# Module 02 Quiz — ML System Architecture

## Questions

### 1. What is the main security reason to study the full ML lifecycle?

A. To understand model mathematics deeply  
B. To identify where attackers can influence model behavior or system decisions  
C. To make training faster  
D. To avoid writing application security tests

### 2. Which of the following is usually a security-sensitive asset in an ML system?

A. Training data  
B. Model artifact  
C. Evaluation dataset  
D. All of the above

### 3. Why can labeling be a security risk?

A. Labels are never used by models  
B. Labels may be treated as ground truth and can shape model behavior  
C. Labels are always public  
D. Labels only affect UI design

### 4. What is data poisoning?

A. Encrypting a dataset  
B. Compressing model artifacts  
C. Manipulating training or feedback data to influence model behavior  
D. Removing duplicate rows from a dataset

### 5. What is a model registry security concern?

A. Unauthorized replacement of a model artifact  
B. Too many slides in a training deck  
C. Users forgetting passwords  
D. Incorrect CSS rendering

### 6. Why is benchmark or test data leakage a problem?

A. It can make evaluation results look better than real-world performance  
B. It always improves security  
C. It prevents model deployment  
D. It only matters for frontend applications

### 7. In a RAG system, why is the vector database security-sensitive?

A. It stores or points to content that may be retrieved into the model context  
B. It only stores harmless numbers  
C. It replaces the need for authorization  
D. It prevents prompt injection automatically

### 8. What is the strongest statement about feedback loops?

A. Feedback always improves security  
B. Feedback should always be used directly for retraining  
C. Feedback can improve the system but can also become a poisoning path  
D. Feedback is unrelated to ML security

### 9. Which control is most appropriate for model artifacts?

A. Ignore them after training  
B. Store them only on a developer laptop  
C. Use access control, integrity checks, metadata, and approval workflow  
D. Put the model name in a spreadsheet

### 10. What is the key difference between a normal chatbot and an agent from an architecture perspective?

A. Agents cannot use models  
B. Agents can act through tools or workflows, so authorization and auditability become more important  
C. Chatbots are always insecure and agents are always secure  
D. Agents do not need logs

### 11. Which is a good architecture review question for ML systems?

A. Who can influence the data used by the model?  
B. Can the model artifact be reproduced or rolled back?  
C. Can users repeatedly query the inference API?  
D. All of the above

### 12. Why is “the dataset is internal” not enough to establish trust?

A. Internal data may still be writable by many users, vendors, systems, or compromised accounts  
B. Internal data is always encrypted  
C. Internal data cannot influence models  
D. Internal data is never used for training

## Answer key

1. **B** — The full lifecycle shows where model behavior can be influenced.
2. **D** — Training data, model artifacts, and evaluation datasets are all security-sensitive.
3. **B** — Labels shape what the model learns.
4. **C** — Poisoning manipulates training, fine-tuning, or feedback data.
5. **A** — A model registry controls deployable behavior.
6. **A** — Leakage can make evaluation results misleading.
7. **A** — Retrieved content can influence model output and data exposure.
8. **C** — Feedback loops are useful but security-sensitive.
9. **C** — Treat model artifacts like deployable software artifacts.
10. **B** — Tool use turns model output into potential action.
11. **D** — All three questions are central to ML architecture review.
12. **A** — Internal data still needs provenance, access control, and integrity checks.

## Discussion questions

1. Which lifecycle stage would you review first for a high-risk financial ML system?
2. Which lifecycle stage would you review first for an internal LLM assistant over company documents?
3. What controls can be standardized by a platform team to avoid slowing every ML team down?
4. How would you explain data poisoning risk to an engineering manager without using academic terminology?
5. What would an incident response plan for a bad model release need to include?
