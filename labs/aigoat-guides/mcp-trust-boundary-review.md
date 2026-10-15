# Optional Module 07 extension: MCP trust boundaries

This source-review exercise adds two MCP-specific cases to the [BrokenPilot agent and tool lab](../brokenpilot/prototype-app/TOOL_CALLING_LAB.md). BrokenPilot remains the runnable course path. You can complete this exercise from the linked source without installing another application. If you already have a safely isolated AIGoat v2.0 instance, you may also compare its local UI traces. A bounded Windows student-style run completed the two UI comparisons, but a supported first-time student installation path is still open because its stock setup needs containment changes and some product images failed to load.

Credit: [AIGoat v2.0](https://github.com/AISecurityConsortium/AIGoat/releases/tag/v2.0) is maintained by [AISecurityConsortium](https://github.com/AISecurityConsortium/AIGoat). This course is independent and is not endorsed by them. Read their [training license](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/TRAINING_LICENSE.md) before adapting or reusing lab content. Their training material is licensed CC BY-NC-SA 4.0. This exercise links to upstream material and uses original questions; it does not include their code, prompts, images, or challenge text. Keep this extension in noncommercial self-study unless you have separate permission for another use.

## Before you start

Read the Module 07 [lab path](../../modules/07-agent-tool-security/lab-path.md). Use only the pinned upstream v2.0 source for the questions below. AIGoat's own flags, scores, and submissions are optional and are not course grading. Do not enter real tokens, customer data, or credentials. Its demo services are intentionally vulnerable; do not expose them to a network. The upstream default startup settings publish services beyond localhost, so do not use them on a shared machine or network as a course setup shortcut.

## Case 1: A tool changes after approval

Inspect the [`mcp03-2` definition](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/config/labs/mcp.yml), the [support server](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/app/mcp_servers/community_support.py), and the [tool pin control](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/app/defense/controls/mcp_tool_pin.py). The example starts with a ticket lookup whose approved definition covers customer-visible status. A later tool listing changes what the same named tool exposes.

Answer in your own words:

1. Which approval assumption becomes false after the second listing? Identify the trust boundary between the server's advertised definition and the client's approved definition.
2. In the vulnerable state, what happens on the second call that did not happen on the first? Separate the tool listing, client decision, server execution, and returned data.
3. In the defended state, which component refuses the second call, and at what point? Explain why scanning for instruction-like text alone would miss this case.
4. What would you pin or verify in a production tool broker besides the description? State one limit of a description pin.

## Case 2: A credential reaches the wrong server

Inspect the [`mcp07-1` definition](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/config/labs/mcp.yml), [child process environment construction](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/app/mcp/env.py), [support diagnostics](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/app/mcp_servers/community_support.py), and [catalog staff tool](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/app/mcp_servers/shop_catalog.py). The credential in this lab is a decoy generated for training.

Answer in your own words:

1. Which server owns the catalog credential? Which other server receives it in the vulnerable state, and who decides what each child process receives?
2. What does the support server reveal, and what does the catalog accept? Identify the separate credential exposure and credential use observations.
3. What changes at the defended level before the support process starts? Explain why filtering the support tool's output would be a weaker control.
4. If this were a real integration, how would you scope the credential's audience and lifetime so a copied value had less reach? Name one residual risk after process-level scoping.

## Record your result

Use a short [lab journal entry](../STUDENT_LAB_JOURNAL_GUIDE.md) for each case. Record the asset, trust boundary, evidence from the pinned source or a safely isolated local trace, control decision, and residual risk. Distinguish what you observed from what you propose for production. A source-review answer should say it is source review; do not describe it as a live exploit.

Instructor validation of these two local MCP comparisons is recorded in the [AIGoat adoption evaluation](../../instructor/aigoat-adoption-evaluation.md). AIGoat's `mcp03-1` planner example is simulated, and its `asi07-1` handoff does not authenticate a cryptographic signature. Neither is needed for this exercise.
