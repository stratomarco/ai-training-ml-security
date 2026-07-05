# BrokenPilot Mock LLM Mode

The first BrokenPilot prototype should support a deterministic mock LLM mode.

This is intentional. The first goal is to teach architecture and controls, not model variability.

## Why mock LLM first?

A real LLM introduces cost, latency, non-determinism, rate limits, API keys, and provider-specific behavior.

For the MVP, students need a reliable way to observe the same security failure every time.

Mock mode allows:

- No external API keys
- No paid provider dependency
- Repeatable labs
- Easier grading
- Easier CI/testing later
- Clear mapping between input, retrieved context, and unsafe action

## Mock behavior model

The mock LLM should be simple rule-based logic.

Example behavior:

| Condition | Mock response |
|---|---|
| User asks for incident summary | Return summary from matching ticket + retrieved docs |
| Retrieved doc contains malicious instruction marker | Include unsafe recommendation or tool intent |
| Retrieved doc says lower priority | Emit `ticket.update` intent to lower priority |
| Memory contains poisoned preference | Prefer poisoned source in summary |
| Hardened mode labels retrieved content as untrusted | Do not emit unsafe tool intent |

## Suggested malicious markers

Use obvious markers so instructors can inspect them.

Examples:

```text
BROKENPILOT_ATTACK:LOWER_PRIORITY
BROKENPILOT_ATTACK:EXFILTRATE_SUMMARY
BROKENPILOT_ATTACK:TRUST_VENDOR_NOTE
BROKENPILOT_ATTACK:WRITE_MEMORY
```

These should not be presented as realistic prompt payloads. They are deterministic lab triggers.

## Example mock response logic

```text
If retrieved_context contains BROKENPILOT_ATTACK:LOWER_PRIORITY
and ENABLE_TOOL_APPROVAL is false:
  produce tool intent: update INC-1001 priority to low
else if ENABLE_TOOL_APPROVAL is true:
  produce response: priority change requires approval
```

## Optional real LLM mode later

After the deterministic prototype works, add optional backends:

- Ollama local OpenAI-compatible endpoint
- OpenAI-compatible API endpoint
- Other provider adapters only if needed

Real LLM mode should be optional and clearly marked as less deterministic.

## Student learning point

Mock mode is not pretending to be a real model. It is a controlled teaching harness.

The lesson is that unsafe architecture allows hostile context to influence actions, and that policy controls must sit outside the model.
