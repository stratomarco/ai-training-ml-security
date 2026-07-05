# DVAIA Fallback Decision Guide

DVAIA is an external dependency. It should not be the single point of failure for a live cohort.

## Known-good reference

The course validation used this DVAIA revision:

```text
airtasystems/DVAIA-Damn-Vulnerable-AI-Application
commit: 23c115252554caa445c0e6ba28641c1110c118e1
```

Use the pinned revision when preparing an instructor machine or shared lab environment.

## Decision rule during delivery

Use this rule in live training:

| Situation | Instructor action |
|---|---|
| DVAIA works for most teams within 20 minutes | Continue with DVAIA as planned |
| DVAIA fails for multiple teams | Switch to BrokenPilot standalone path |
| Corporate network blocks containers or model downloads | Use BrokenPilot local deterministic mode |
| Time is running short | Use BrokenPilot for required evidence, DVAIA for optional homework |
| Instructor wants deterministic grading | Use BrokenPilot as the assessed target |

## Communication to students

Say this clearly:

> DVAIA is an external vulnerable AI lab. BrokenPilot is our controlled course target. If DVAIA is unavailable, you are not losing the learning objective. We will use BrokenPilot to demonstrate the same core security properties in a deterministic way.

## What not to do

Do not spend a live cohort debugging external dependency issues for an hour. That turns a security course into an environment troubleshooting session.

Do not grade students on DVAIA-specific behavior unless the DVAIA environment is known to be available and stable for all teams.
