# LLM Application Security Review Template

## 1. System overview

### Application name

### Business purpose

### Users

### Main workflows

### Model/provider/local runtime

## 2. Architecture

Provide a diagram or description.

```text
User
  -> Application
  -> LLM gateway
  -> Retrieval/tools/data
  -> Output handling
  -> Logs/monitoring
```

## 3. Assets

| Asset | Sensitivity | Owner | Notes |
|---|---|---|---|
| | | | |

## 4. Trust boundaries

| Boundary | From | To | Risk |
|---|---|---|---|
| | | | |

## 5. Data and context

| Context source | Trusted? | Authorized before use? | Sensitive? | Notes |
|---|---|---|---|---|
| System prompt | | | | |
| User prompt | | | | |
| Retrieved documents | | | | |
| Tool output | | | | |
| Memory | | | | |
| Logs | | | | |

## 6. Tool/function inventory

| Tool | Action | Data access | AuthZ method | Approval required? |
|---|---|---|---|---|
| | | | | |

## 7. Risk review

| Risk category | Present? | Evidence | Impact | Mitigation |
|---|---|---|---|---|
| Prompt injection | | | | |
| Indirect prompt injection | | | | |
| Insecure output handling | | | | |
| Sensitive disclosure | | | | |
| Model DoS | | | | |
| Supply chain | | | | |
| Tool/plugin risk | | | | |
| Excessive agency | | | | |
| Overreliance | | | | |
| Model theft | | | | |

## 8. Findings

### Finding 1  -  Title

**Category:**  
**Severity:**  
**Affected component:**  
**Attacker capability:**  
**Impact:**  
**Evidence:**  
**Root cause:**  
**Recommended mitigation:**  
**Residual risk:**  

## 9. Recommended controls

| Control | Priority | Owner | Notes |
|---|---|---|---|
| Authorization before retrieval | | | |
| Tool gateway | | | |
| Output validation | | | |
| Human approval gates | | | |
| Token and cost budgets | | | |
| Safe logging | | | |
| Monitoring and alerting | | | |

## 10. Residual risk statement

## 11. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Engineering owner | | | |
| Security owner | | | |
| Product owner | | | |
| Risk owner | | | |
