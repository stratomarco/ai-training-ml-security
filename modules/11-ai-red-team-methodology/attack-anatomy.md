# Attack anatomy: AI red team chain

## Scenario

BrokenPilot is an internal AI agent that retrieves documents, summarizes context, stores memory, and updates tickets. A red team evaluates whether a user can manipulate the system into disclosing unauthorized data or changing a ticket outside their allowed boundary.

## Chain 1: retrieval to disclosure

1. Identify a user with limited tenant access.
2. Query for terms that match restricted documents.
3. Observe whether unauthorized context enters the model response.
4. Enable retrieval authorization.
5. Re-run the test and confirm the restricted context is blocked.

Control tested: retrieval authorization before context construction.

## Chain 2: memory poisoning to tool intent

1. Add a malicious memory instruction.
2. Trigger an agent task related to that instruction.
3. Observe that the agent intent is influenced.
4. Enable memory review or memory isolation.
5. Re-run and confirm the poisoned memory is not active.

Control tested: memory trust and activation.

## Chain 3: manipulated intent to tool execution

1. Cause the model or memory layer to propose a risky action.
2. Target an object outside the user's tenant or role boundary.
3. Observe whether the tool broker checks authorization.
4. Enable tool authorization.
5. Re-run and confirm execution is blocked.

Control tested: independent authorization at the tool boundary.

## Chain 4: model output to downstream sink

1. Cause or retrieve content that includes a benign output-sink marker.
2. Render the model output through the downstream HTML sink.
3. Observe raw versus encoded output.
4. Enable output encoding.
5. Re-run and confirm context-appropriate encoding.

Control tested: insecure output handling.

## What makes a chain useful

A useful attack chain shows the path from entry point to impact, then shows which control breaks the path. A chain that only lists prompts is not enough. The report should name the system boundary that failed.
