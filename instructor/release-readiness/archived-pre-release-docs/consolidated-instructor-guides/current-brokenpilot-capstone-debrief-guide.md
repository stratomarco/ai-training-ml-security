# Instructor Debrief Guide: Current BrokenPilot Capstone

## Debrief goal

The debrief should move students from "I exploited the agent" to "I know where the system must enforce security." Keep the conversation centered on control placement.

## Suggested 30-minute debrief

1. Five minutes: ask each team for its launch recommendation.
2. Ten minutes: compare the strongest finding from each team.
3. Ten minutes: discuss the memory-poisoning plus tool-authorization defense-in-depth moment.
4. Five minutes: ask what would change if the tool became production write-capable.

## Instructor prompts

- Which part of the system made the unsafe behavior possible?
- Did the fix rely on the model, or did the application enforce it?
- What would you test in CI to prevent regression?
- What should be logged, and what must never be logged?
- Which issue is safe for a read-only pilot but unsafe for write-capable automation?

## Common correction

If students say "the fix is a better prompt," redirect them to the evidence. A better prompt may reduce frequency. It does not authorize retrieval, encode output, validate tool arguments, isolate memory, or enforce tenant boundaries.
