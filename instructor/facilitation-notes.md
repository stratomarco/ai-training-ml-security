# Facilitation Notes

## Discussion style

Use Socratic questioning. Let students find the trust boundary and broken assumption before revealing the answer.

## Useful prompts

- What did the developer assume was true?
- Which component trusted the wrong input?
- Where should the policy decision live?
- Is this a model problem or a system problem?
- What would fail if the model is wrong?
- What would fail if the retrieved document is malicious?
- What would fail if the user is malicious?
- What would fail if the tool response is malicious?

## Handling prompt-injection discussions

Students may propose stronger prompts as the primary fix. Acknowledge that instruction design can help, but move the discussion toward controls outside the model:

- Authorization
- Tool scoping
- Data isolation
- Approval gates
- Retrieval filtering
- Output handling
- Monitoring
- Rate limits
- Sandboxing

## Handling leadership discussions

Ask students to translate technical risk into business language:

- What could be leaked?
- What could be changed?
- What could be disrupted?
- What decision could be made incorrectly?
- What compliance obligation could be affected?
- What would the incident look like?
