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

## Graded deliverable

A tool permission matrix or tool-control design with authorization rules, approval rules, audit fields, and validation steps.

## Keep central

- Memory poisoning can steer intent while tool authorization still blocks unsafe execution
- The model may propose; the system must decide and enforce

## Avoid

- Do not split the module across duplicate paper agent labs
- Do not grade only the exploit path

## Instructor note

Use this file as the first stop when deciding what to run live, what to assign as self-study, and what to grade. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning lab and grade the artifact instead of pretending it is runnable.
