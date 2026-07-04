# Current BrokenPilot Capstone Evidence Map

Use this map to build or grade the capstone final report. It connects each report finding to the current lab path and the expected observable behavior.

| Finding | Lab path | Vulnerable observation | Controlled observation | Required student artifact |
|---|---|---|---|---|
| Direct prompt injection | `labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md` | `USER_OVERRIDE:` changes behavior and returns `DIRECT_PROMPT_INJECTION_FOLLOWED` | prompt injection control treats the message as untrusted and returns `DIRECT_PROMPT_INJECTION_BLOCKED` | Root cause and validation note |
| Insecure output handling | `labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md` | `/render` returns raw `<b>OUTPUT_SINK_TRIGGERED</b>` | `/render` returns escaped `&lt;b&gt;OUTPUT_SINK_TRIGGERED&lt;/b&gt;` | Sink-specific output control |
| Cross-tenant privacy leakage | `labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md` | beta user can see alpha restricted fake fragments from `DOC-002` or `DOC-006` | retrieval authz prevents alpha restricted docs from entering beta context | Retrieval authorization rule and logging residual risk |
| Tool confused deputy | `labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md` | cross-tenant ticket update succeeds | tool broker denies update before execution | Tool permission matrix or broker policy |
| Memory poisoning | `labs/brokenpilot/prototype-app/MEMORY_POISONING_LAB.md` | poisoned memory steers future intent | memory controls reduce influence, and tool authz blocks unsafe execution | Memory trust model and defense-in-depth explanation |

## Grading reminder

Do not give full credit for screenshots alone. A strong submission includes evidence, root cause, control, validation, and residual risk. The student should explain why the model is not the enforcement boundary.
