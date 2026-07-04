# Teaching Modules 01 to 04 After the Depth Pass

## Purpose

Modules 01 to 04 are the foundation for the rest of the course. They should not feel like introductory filler. They teach the thinking pattern students use in every later lab:

1. Identify the system role of the model.
2. Draw the architecture and trust boundaries.
3. Map risk categories to concrete failure paths.
4. Convert architecture risk into controls and validation.

## Instructor emphasis

Module 01 should establish the sentence: the model may influence a decision, but the system must enforce the boundary.

Module 02 should force students to draw more than a model box. Ask where retrieval, tools, logs, output sinks, and promotion paths live.

Module 03 should stop students from using OWASP categories as findings. Make them write the failure path.

Module 04 should make students practice design change, not just risk identification.

## Recommended pacing in the 40-hour course

Use these modules as a compressed but active foundation. Do not lecture every paragraph. Give students a small architecture scenario and make them apply the reading.

A strong pattern is:

- 20 minutes reading discussion.
- 20 minutes architecture or risk mapping.
- 20 minutes finding rewrite or control placement.
- 10 minutes exit ticket.

## Bridge to later labs

Before starting BrokenPilot, remind students that Module 01 explains why model behavior is not the control.

Before starting the toy-classifier app, remind students that Module 03 explains why category labels need system impact.

Before starting the MLOps evidence pack, remind students that Module 04 explains why artifact trust is an architecture decision.
