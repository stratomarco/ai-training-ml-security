# Threat Model Template

## System name

`Name of the AI-enabled system`

## System purpose

Describe what the system does and why it exists.

## Scope

### In scope

- Component one
- Component two
- Component three

### Out of scope

- Component one
- Component two

## Users and roles

| Role | Description | Permissions |
|---|---|---|
| User | | |
| Admin | | |
| Service account | | |
| Model provider | | |

## Assets

| Asset | Why it matters | Sensitivity |
|---|---|---|
| Prompts | May contain sensitive data or instructions | |
| Model output | May trigger actions or leak data | |
| Retrieved documents | May contain sensitive data or malicious instructions | |
| Tools | May create operational impact | |
| Logs | May contain secrets or personal data | |
| Model artifact | May contain intellectual property | |

## Architecture

```text
user
  |
  v
application
  |
  +-- model gateway
  +-- retrieval service
  +-- vector database
  +-- tool service
  +-- business data
  +-- logs and monitoring
```

## Trust boundaries

| Boundary | Trusted side | Untrusted side | Notes |
|---|---|---|---|
| User to application | Application | User input | |
| App to model | Application policy | Model behavior | |
| App to retrieval | Application | Retrieved content | |
| Model to tools | Tool policy | Model request | |

## Threats

| ID | Threat | Attacker | Asset | Impact | Existing control | Gap |
|---|---|---|---|---|---|---|
| T-001 | | | | | | |

## Abuse cases

| ID | Abuse case | Expected impact | Detection | Mitigation |
|---|---|---|---|---|
| A-001 | | | | |

## Risk rating

| Risk | Likelihood | Impact | Severity | Owner | Status |
|---|---|---|---|---|---|
| | | | | | |

## Mitigations

| Mitigation | Threats addressed | Trade-off | Owner |
|---|---|---|---|
| | | | |

## Residual risk

Describe what remains unsafe after mitigations.

## Open questions

- Question one
- Question two
