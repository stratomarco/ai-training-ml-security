# Strong Executive Readout Example — BrokenPilot

## Decision summary

BrokenPilot should proceed as a limited pilot, not a full production launch, until three launch-blocking controls are in place: retrieval authorization, tool-call approval gates, and audit logging.

## Business value

The assistant can reduce incident response overhead by summarizing tickets, retrieving relevant documentation, and helping responders prepare updates.

## Key risk

The current design allows untrusted model context to influence privileged actions. A malicious document or ticket comment could cause the agent to update incident metadata incorrectly or expose restricted information.

## Launch blockers

1. Retrieval-time authorization for all RAG chunks.
2. External policy check before tool execution.
3. Human approval for destructive or high-impact actions.

## Acceptable for pilot

- Summarization-only mode.
- Read-only ticket access.
- Restricted user group.
- Logging and review of all prompts, retrieved document IDs, and tool attempts.

## Recommendation

Approve a limited pilot for read-only use. Delay write-capable tool access until the launch blockers are implemented and tested.
