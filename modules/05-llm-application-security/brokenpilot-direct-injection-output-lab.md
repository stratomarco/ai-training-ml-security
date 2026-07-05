# Module 05 BrokenPilot Lab: Direct Injection and Output Handling

## Purpose

This lab closes two observable gaps in Module 05:

1. Direct prompt injection through the user message.
2. Insecure output handling when model-derived text reaches an HTML sink.

## Lab assets

Use the BrokenPilot prototype:

- `labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md`
- `labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md`

## Required observations

Students must capture four observations:

| Scenario | Control | Expected observation |
|---|---|---|
| Direct injection | `ENABLE_PROMPT_INJECTION_FILTER=false` | `DIRECT_PROMPT_INJECTION_FOLLOWED` |
| Direct injection | `ENABLE_PROMPT_INJECTION_FILTER=true` | `DIRECT_PROMPT_INJECTION_BLOCKED` |
| Output handling | `ENABLE_OUTPUT_ENCODING=false` | Raw `<b>OUTPUT_SINK_TRIGGERED</b>` appears in the rendered fragment |
| Output handling | `ENABLE_OUTPUT_ENCODING=true` | Encoded `&lt;b&gt;OUTPUT_SINK_TRIGGERED&lt;/b&gt;` appears instead |

## Deliverable

Submit a short control note that explains:

1. Why direct and indirect prompt injection share the same root cause.
2. Why marker detection is not a real production control.
3. Why output encoding belongs at the sink, not in the model prompt.
4. What residual risk remains after enabling these controls.

## Round 3 output-handling student path confirmation

The insecure output-handling portion of this module must be run through `POST /render`.

- Vulnerable mode: `ENABLE_OUTPUT_ENCODING=false`; the rendered response includes the raw benign marker `<b>OUTPUT_SINK_TRIGGERED</b>`.
- Controlled mode: `ENABLE_OUTPUT_ENCODING=true`; the same marker is HTML-escaped for the sink context.
- Graded artifact: explain why the problem is downstream trust of model output, not the model producing text.
