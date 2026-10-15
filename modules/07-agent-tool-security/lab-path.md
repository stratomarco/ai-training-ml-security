# Module 07 Lab Path: Agent and Tool Security

## Role in the 40-hour course

Module 07 remains the reference lab standard. BrokenPilot demonstrates the tool confused-deputy problem, tool authorization, approval gates, audit logging, and defense in depth with memory poisoning.

## Runnable path

- BrokenPilot tool authorization lab
- BrokenPilot memory poisoning lab
- BrokenPilot tool approval and audit behavior

## Reasoning path

- Separate model intent from system authorization
- Design a tool broker that enforces target-object authorization
- Optional [AIGoat MCP trust-boundary source review](../../labs/aigoat-guides/mcp-trust-boundary-review.md): compare tool-definition pinning and credential scoping in two independently maintained training cases. No AIGoat installation is required for the source review.

## Suggested practice deliverable

A tool permission matrix or tool-control design with authorization rules, approval rules, audit fields, and validation steps.

## Keep central

- Memory poisoning can steer intent while tool authorization still blocks unsafe execution
- The model may propose; the system must decide and enforce

## Avoid

- Do not split the module across duplicate paper agent labs
- Do not treat the exploit path as the whole learning outcome

## Instructor note

Use this file as the first stop when deciding what to run live and what to offer for self-study. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning exercise with a written artifact instead of pretending it is runnable. Rubrics are optional feedback guidance.
