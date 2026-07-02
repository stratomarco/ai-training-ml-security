# Controls and Remediations Template

Use this template to turn a finding into implementable engineering work.

## Finding

Name the finding.

## Security property required

What must the system guarantee?

Examples:

- Users can only retrieve documents they are authorized to see.
- Tools must enforce tenant authorization independently of the model.
- Memory entries must not become active without review.
- Model output must not be rendered as trusted HTML.

## Control objective

Describe the objective in one or two sentences.

## Proposed control

Describe the control precisely enough for an engineer to implement.

## Policy rules

| Rule ID | Rule | Enforced by | Failure behavior |
|---|---|---|---|
| | | | |

## Data required

What data or metadata does the control need?

- 

## Enforcement point

Where is the control enforced?

- Application layer
- Retrieval layer
- Tool/API layer
- Model gateway
- Policy engine
- CI/CD pipeline
- Runtime monitor

## Example allowed case

Describe a request that should be allowed.

## Example blocked case

Describe a request that should be blocked.

## Test cases

| Test | Expected result |
|---|---|
| | |

## Logging and audit

What should be logged?

What should not be logged?

## Rollout plan

1. 
2. 
3. 

## Residual risk

What remains risky after the control is implemented?
