# BrokenPilot Prototype Instructor Runbook

This runbook defines how an instructor should use the future runnable BrokenPilot prototype.

## Instructor goals

The prototype should help instructors teach:

- Why prompts are not security boundaries
- Why RAG needs query-time authorization
- Why tool execution needs independent policy checks
- Why memory needs provenance and review
- Why audit logs matter for model-mediated actions

## Recommended delivery formats

### 45-minute demo

Use only one attack path:

1. Show vulnerable architecture.
2. Trigger indirect prompt injection.
3. Show unsafe tool intent or action.
4. Enable approval or retrieval authorization.
5. Repeat and show blocked behavior.

### 2-hour workshop

Use three tasks:

1. Indirect prompt injection.
2. Cross-document authorization failure.
3. Tool confused deputy.

End with one written finding.

### 1-day workshop

Use full prototype flow:

1. Architecture mapping.
2. Three exploit paths.
3. Control comparison.
4. Risk register.
5. Executive summary.

## Pre-class checklist

- [ ] App builds locally.
- [ ] Reset script works.
- [ ] Fake data is loaded.
- [ ] Vulnerable mode works.
- [ ] Hardened control toggles work.
- [ ] Audit log is visible.
- [ ] No real secrets are present.
- [ ] Network exposure is localhost only.

## Instructor evidence to prepare

Before teaching, prepare one known-good example for each:

- Successful app startup
- Poisoned document retrieval
- Unauthorized retrieval
- Unsafe tool action
- Blocked hardened-mode tool action
- Audit log entry

## Grading emphasis

Reward students for:

- Correct trust-boundary reasoning
- Specific root-cause explanation
- Implementable controls
- Clear evidence
- Balanced remediation
- Good risk communication

Do not over-reward students for clever prompt payloads alone.

## Common teaching failure

The most common failure mode is allowing the session to become a jailbreak contest.

Redirect with:

> What security property failed? Which component trusted the wrong thing? Where should the control live?
