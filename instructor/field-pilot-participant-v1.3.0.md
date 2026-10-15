# v1.3.0 first-time participant brief

Thank you for trying part of AI Training: ML Security. This session checks whether a new learner can find, install, and understand the course labs. It is not an exam. We want to hear where the course is confusing, including setup problems.

Allow up to two hours on your own computer. You need a browser and Python 3.12 for the full route. Docker is optional. You do not need Qwen, Ollama, LM Studio, DVAIA, a cloud account, or a real model. The exercises use fake local data and should stay on your own machine.

## Start from the published version

1. Download a fresh copy from the [v1.3.0 release](https://github.com/stratomarco/ai-training-ml-security/releases/tag/v1.3.0), or check out the `v1.3.0` Git tag into a new folder. Keep this copy separate from any earlier course checkout.
2. Use the [course website](https://stratomarco.github.io/ai-training-ml-security/) to find the Start Here and lab paths. If the live website differs from the downloaded v1.3.0 files, tell the facilitator which page differed and follow the downloaded version for commands.
3. Follow the [cross-platform setup guide](https://github.com/stratomarco/ai-training-ml-security/blob/v1.3.0/docs/start-here/cross-platform-setup.md) to start BrokenPilot locally. Stop if a service would bind to a public interface or if a step asks you to use real credentials or data.

If you cannot get past a step after about ten minutes, note the exact command, message, or page and ask for help. Please do not silently skip it. Stop at the agreed session time even if you have not finished every task.

## Tasks

1. Complete the [ticket-to-agent exercise](https://github.com/stratomarco/ai-training-ml-security/blob/v1.3.0/labs/brokenpilot/prototype-app/TICKET_TO_AGENT_LAB.md). Show the fake ticket before and after the agent run. Try a control profile and explain what changed.
2. Complete the [Mock Hub exercise](https://github.com/stratomarco/ai-training-ml-security/blob/v1.3.0/labs/brokenpilot/prototype-app/MOCK_HUB_LAB.md). Compare the `vulnerable`, `hub-redaction`, and `hub-least-privilege` profiles. Use only the generated fake token.
3. Run the three cases in the [artifact-promotion exercise](https://github.com/stratomarco/ai-training-ml-security/blob/v1.3.0/labs/mlops-supply-chain-labs/artifact-promotion/artifact-promotion-lab.md). Explain each decision in your own words.

You may keep short notes, but please do not publish token values, browser exports, screenshots with personal data, or files from outside the training folder. No score or flag is expected.

## Feedback to share with the facilitator

- Where did you first need help, and what were you trying to do?
- Which page, command, or UI label was unclear? Include the exact wording if possible.
- Which control or decision can you explain now? Which part remains unclear?
- Did any instruction seem unsafe, ask for unnecessary software, or suggest using real data?
- What is the one change that would most improve this route?

Share observations through the channel agreed with your facilitator. It is fine to say that a task was not attempted.
