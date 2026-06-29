# AI Architecture Review Template

## System name

`System name`

## Business purpose

Describe the business purpose.

## Architecture summary

Describe the system at a high level.

## Components

| Component | Purpose | Owner | Trust level |
|---|---|---|---|
| Application | | | |
| Model gateway | | | |
| Retrieval service | | | |
| Vector database | | | |
| Tool service | | | |
| Logging | | | |

## Data flows

| Flow | Source | Destination | Data | Sensitivity | Control |
|---|---|---|---|---|---|
| DF-001 | | | | | |

## Trust boundaries

| Boundary | Risk | Control |
|---|---|---|
| User to application | | |
| Application to model | | |
| Model to tools | | |
| Retrieval to model context | | |

## Key questions

1. What can the model see?
2. What can the model do?
3. What tools are available?
4. What data can be retrieved?
5. How is retrieval authorized?
6. What actions require approval?
7. What is logged?
8. What is monitored?
9. How are prompts, outputs, and documents retained?
10. How is the model or provider isolated from sensitive data?

## Findings

| ID | Finding | Risk | Recommendation |
|---|---|---|---|
| AR-001 | | | |

## Recommended controls

- Policy layer outside the model
- Least-privilege tool access
- Retrieval authorization
- Tenant isolation
- Human approval gates
- Tool argument validation
- Output handling controls
- Sandboxing
- Egress control
- Audit logging
- Abuse detection
- Rate limiting
- Incident response process

## Residual risk

Describe the risks that remain after recommended controls.
