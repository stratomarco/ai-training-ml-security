# AI Red Team Scope Template

## Engagement name

<!-- Name of the assessment. -->

## Mission statement

<!-- What question is this red team exercise trying to answer? -->

## Business context

<!-- Why does this system matter? What decisions or workflows depend on it? -->

## Systems in scope

| System/component | Environment | Notes |
|---|---|---|
| | | |

## Systems out of scope

| System/component | Reason |
|---|---|
| | |

## Approved accounts and roles

| Account/role | Permissions | Purpose |
|---|---|---|
| | | |

## Approved data

| Data type | Real/fake/synthetic | Handling rule |
|---|---|---|
| | | |

## Forbidden actions

- [ ] Production destructive actions
- [ ] Real customer data exposure
- [ ] Unauthorized credential access
- [ ] Out-of-scope phishing or social engineering
- [ ] Persistence outside approved lab
- [ ] External scanning outside scope
- [ ] Other:

## Allowed test categories

- [ ] Prompt injection
- [ ] Indirect prompt injection
- [ ] RAG authorization
- [ ] Tool misuse
- [ ] Memory poisoning
- [ ] Sensitive information disclosure
- [ ] Model DoS/cost abuse
- [ ] Model extraction
- [ ] MLOps supply chain review
- [ ] Privacy testing
- [ ] Robustness testing
- [ ] Infrastructure review

## Rate limits and safety limits

| Limit | Value | Owner |
|---|---|---|
| Token budget | | |
| API request limit | | |
| Tool-call limit | | |
| Cost limit | | |
| Stop condition | | |

## Evidence requirements

- [ ] Prompt/input
- [ ] Retrieved context
- [ ] Model output
- [ ] Tool-call trace
- [ ] API response
- [ ] Logs/traces
- [ ] Screenshots/transcripts
- [ ] Impact statement
- [ ] Reproduction steps

## Escalation contacts

| Situation | Contact | Method |
|---|---|---|
| Safety stop | | |
| Production impact | | |
| Sensitive data exposure | | |
| Legal/policy question | | |

## Approval

| Role | Name | Approval date |
|---|---|---|
| System owner | | |
| Security owner | | |
| Legal/policy if needed | | |
