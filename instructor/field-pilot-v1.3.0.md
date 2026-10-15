# v1.3.0 first-time learner pilot

Use this guide with two or three people who have not used this course and one instructor who did not build the new labs. This is a delivery check, not an exam. Do not infer learning outcomes from CI or a maintainer walkthrough.

## Preparation

Give each participant the v1.3.0 release link, the [course website](https://stratomarco.github.io/ai-training-ml-security/), and the [cross-platform setup guide](https://stratomarco.github.io/ai-training-ml-security/start-here/cross-platform-setup/). Ask them to use a fresh checkout or download on their own machine. Use fake lab data only. No model download is needed for this pilot; the Qwen3 extension can be evaluated separately if the participant already has the supported local setup.

Ask participants to speak aloud when an instruction is unclear, but do not coach them through the answer. Record the operating system, Python version, Docker availability, start and finish times, exact failing command or page, help requested, and what the participant thought the control demonstrated. Do not collect real credentials, personal tickets, or browser storage exports containing other data.

## Student route, 90 to 120 minutes

1. From the website, find the first-run route and start BrokenPilot in the vulnerable profile. Record setup time and any missing prerequisite.
2. Complete the [ticket-to-agent exercise](../labs/brokenpilot/prototype-app/TICKET_TO_AGENT_LAB.md). Show the fake ticket state before and after, then run a relevant control profile and explain the changed decision.
3. Complete the [Mock Hub exercise](../labs/brokenpilot/prototype-app/MOCK_HUB_LAB.md). Compare the leaked fake token, diagnostic redaction, and read-only scope. Explain which control limits a leaked credential's effect.
4. Run the three cases in the [artifact-promotion lab](../labs/mlops-supply-chain-labs/artifact-promotion/artifact-promotion-lab.md). Explain why matching artifact and manifest hashes alone cannot authorize promotion.
5. Ask the participant where they got stuck, which page or UI label caused confusion, and which security decision they can now explain. Invite one concrete improvement.

The static MLOps evidence review remains the main Module 08 teaching path. The new exercises supplement it. If the full route is too long, stop after the BrokenPilot core exercise and record where the participant stopped rather than marking later steps as passed.

## Instructor route, 45 minutes

Ask the instructor to find the lab sequence from `instructor/README.md`, set up a fresh BrokenPilot session, demonstrate vulnerable and controlled Mock Hub behavior, and explain how the artifact gate complements the static evidence review. Note missing teaching context, reset ambiguity, timing problems, and any claim that sounds stronger than the lab evidence supports.

## Record and decide

For each task, record `completed without help`, `completed with help`, `blocked`, or `not attempted`, plus the exact observation. Separate setup failures, confusing instructions, incorrect lab behavior, and enhancement requests. Reproduce a blocker on a clean checkout before changing the course. Fix broken links, unsafe defaults, and repeatable blockers before recommending a wider class. Prioritize other changes only when the same confusion recurs or the instructor identifies a concrete teaching gap. Keep rubrics optional and do not assign scores to pilot participants.

Pilot status: **not run**. Fill in the participant count, dates, environments, observations, and resulting changes after real sessions. Do not treat this guide as evidence that the pilot happened.
