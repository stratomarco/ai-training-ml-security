# BrokenPilot Instructor Guide

This is the single instructor entry point for BrokenPilot. BrokenPilot is the supported runnable environment for Modules 05, 06, 07, 09, 11, and 12.

## What BrokenPilot teaches

BrokenPilot is an internal AI-agent scenario with retrieval, tool use, memory, controls, and audit evidence. It is designed to make students reason about security engineering decisions around an ML-enabled system, not to reward prompt-hacking tricks.

The lab family covers:

- direct prompt injection
- insecure output handling
- RAG authorization and cross-tenant leakage
- tool authorization and confused-deputy behavior
- approval gates
- memory poisoning and memory isolation
- audit evidence and final reporting

## Instructor preparation

Run the supported app and tests from the current target directory:

```powershell
cd labs/brokenpilot/prototype-app
python -m pip install -r requirements.txt
python -m pytest -q
python run_lab.py --profile vulnerable
```

Open `http://127.0.0.1:8010`. Start with the deterministic ticket-to-agent exercise, then restart with one named control profile at a time. The launcher sets the profile explicitly and binds the app to localhost. Reset fake state before repeating a scenario within one process.

Supported entry points:

- [Prototype app README](../labs/brokenpilot/prototype-app/README.md)
- [Ticket-to-agent guided exercise](../labs/brokenpilot/prototype-app/TICKET_TO_AGENT_LAB.md)
- [Main lab guide](../labs/brokenpilot/prototype-app/LAB_GUIDE.md)
- [Direct prompt injection lab](../labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md)
- [Output handling lab](../labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md)
- [Tool calling lab](../labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md)
- [Memory poisoning lab](../labs/brokenpilot/prototype-app/MEMORY_POISONING_LAB.md)
- [Cross-tenant privacy leakage lab](../labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md)
- [Capstone checkpoints](../modules/12-capstone-brokenpilot/capstone-checkpoints.md)
- [Capstone final report path](../modules/12-capstone-brokenpilot/final-report-current-path.md)

## Optional live-model extension

Use the [Qwen extension](../labs/brokenpilot/prototype-app/QWEN_EXTENDED_LAB.md) only after students complete the deterministic path. Run the [classroom preflight](qwen-classroom-preflight.md) on the machines you intend to use. If model setup or response time would consume the lab period, keep the standalone exercises as the supported path.

When discussing Qwen output, separate the retrieved source, raw model response, parsed proposal, application decision, and final ticket state. A refusal can still echo fake sensitive text. A model proposal does not authorize a tool call. Record the digest and timing for each run; do not promise a fixed attack result.

## How to run the lab family

Use BrokenPilot as a progressive system, not as isolated tricks.

1. Start with the system model: users, tenants, retrieval, memory, tool execution, controls, and audit logs.
2. Demonstrate one failure with controls off.
3. Turn on the relevant control and require students to explain what changed.
4. Ask what the control does not solve.
5. Capture evidence as students go: request, response, control state, observed impact, and residual risk.
6. Use the final capstone to force prioritization across multiple failures.

## Module mapping

- Module 05: direct prompt injection and output handling.
- Module 06: RAG authorization and indirect/contextual injection risks.
- Module 07: tool authorization, approval gates, and agent action boundaries.
- Module 09: cross-tenant leakage and privacy impact.
- Module 11: red-team methodology, evidence collection, and finding quality.
- Module 12: capstone synthesis and final report.

## Debrief prompts

Use these prompts after each BrokenPilot segment:

- What failed: instruction handling, authorization, output handling, memory, tool execution, or auditability?
- Was the model the root cause, or did the surrounding system give the model unsafe authority?
- Which control reduced the risk? What did it not cover?
- What evidence would you need to convince an engineering lead this is worth fixing?
- What would a naive fix look like, and how would it fail?

## Common instructor corrections

- Do not frame the prompt-injection filter as the real defense. It is a teaching stand-in. The stronger lesson is instruction/data separation, least privilege, and constrained authority.
- Do not let students stop at exploit reproduction. The deliverable is a defensible security finding with evidence, impact, recommendation, and residual risk.
- Do not describe tool authorization as an LLM feature. It is application authorization around an LLM-mediated action.
- Do not treat memory poisoning as only a prompt problem. It is also a storage, review, scope, isolation, and provenance problem.

## Optional feedback and solution references

- [BrokenPilot instructor solution](../labs/brokenpilot/instructor-solution.md)
- [Complete final report example](../labs/brokenpilot/worked-examples/current-complete-final-report.md)
- [Final report evidence map](../labs/brokenpilot/worked-examples/current-final-report-evidence-map.md)
- [BrokenPilot final report rubric](../labs/brokenpilot/grading-rubric.md) (optional feedback guidance)
- [Module 12 instructor notes](../modules/12-capstone-brokenpilot/instructor-notes.md)
