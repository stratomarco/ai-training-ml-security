# AIGoat adoption evaluation

Status: **candidate external practice, not a validated course lab**. This is an instructor planning note. BrokenPilot remains the primary local LLM, RAG, agent, and capstone target. The current first-time learner pilot does not require AIGoat.

## Why consider it

[AIGoat](https://github.com/AISecurityConsortium/AIGoat) by AISecurityConsortium has a separate tool-using agent and MCP client/host with local models. Its [v2.0 release](https://github.com/AISecurityConsortium/AIGoat/releases/tag/v2.0) describes 46 labs across LLM, agent, and MCP surfaces. The clearest addition to this course is **MCP-specific trust boundaries** that BrokenPilot does not implement. More prompt-injection examples alone would duplicate our current path.

Use a separately downloaded upstream release for any pilot. Do not vendor its application, prompts, lab definitions, walkthroughs, images, or branding into this repository. AIGoat is maintained by AISecurityConsortium; this course is independent and has no stated endorsement from them.

## License boundary

Read AIGoat's [training license](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/TRAINING_LICENSE.md), [root license](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/LICENSE), and [NOTICE](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/NOTICE) at the exact version used before publishing a student guide. Its maintainers identify platform code as Apache 2.0, but labs, prompts, challenge logic, documentation, and media as CC BY-NC-SA 4.0. They explicitly require prior written permission for paid training that uses their labs or prompts and restrict use of their name and branding with products or services. The training-license file retains the old `config/labs.yml` path; the v2.0 NOTICE and [directory license](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/config/labs/LICENSE) explicitly cover `config/labs/`. Our course license cannot grant rights over their material. Our additional permission for internal organizational learning does not extend to AIGoat.

The proposed course use is a credited link for independent, noncommercial self-study. Do not include AIGoat in a paid workshop, corporate training delivered for a fee, certification, or commercial course package without written permission from its maintainers. Do not copy their exercise wording or use their logo. If we later adapt their content, review attribution, modification marking, and share-alike requirements first. This is a practical project boundary, not a legal opinion.

## Small pilot, then decide

| Candidate upstream lab | Course connection | Distinct question for the student |
|---|---|---|
| MCP03 tool-description poisoning | Module 07 tool provenance | Can untrusted tool metadata change an agent's choice or arguments, and which check actually stops the call? |
| MCP07 token passthrough | Module 07 identity and scope | What prevents a token issued for one audience from reaching another server? Use only AIGoat's fake lab token. |
| ASI07 unsigned agent handoff | Module 07 inter-agent trust | Where should an agent verify the source and authority of a handoff before acting? |
| Agentic Kill Chain | Module 11 optional follow-up | Does its model-driven trace add a teaching outcome beyond the BrokenPilot ticket-to-agent chain? Pilot only if the first three add value. |

These names and scenarios are drawn from AIGoat's [v2.0 lab catalog](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/README.md#attack-scenarios-owasp-llm-agentic-and-mcp-security-labs) and [release notes](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/RELEASE_NOTES_v2.0.md). They are candidates, not reproduced or validated outcomes. We would write our own short reflection prompts around the observed trace, trust boundary, control, and residual risk. AIGoat's flags and scores would remain optional upstream features, not course grading.

## Safety and delivery gates

1. **Version and terms:** evaluate the `v2.0` release at commit `e1c538badb93c6c1c2307096ab5d709a9ee0fe55` first and record any dependency or license changes. The upstream `main` branch can change independently.
2. **Contained setup:** inspect startup scripts, Compose configuration, model pulls, executable tools, MCP server launchers, external dependencies, and service bindings before running. At v2.0, [`start.sh`](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/scripts/start.sh) starts the backend on `0.0.0.0`; [Docker Compose](https://github.com/AISecurityConsortium/AIGoat/blob/v2.0/docker/docker-compose.yml) publishes 3000, 8000, and 11434 on `0.0.0.0`. The app also ships known demo credentials. A course setup must bind every exposed service to loopback, use fake data, and verify actual listeners. Neither upstream start command should be handed to students as a safe default on a shared or public network.
3. **Capacity and support:** its documented local path needs Python 3.11, Node 18+, Ollama, and at least 8 GB free RAM. Agent and MCP work needs a tool-capable model; upstream suggests `qwen3.5:9b`, which adds a substantial download. Confirm a Windows, macOS, and Linux route before promising cross-platform support. Do not treat Google Colab as the offline route.
4. **Teaching evidence:** run MCP03 and MCP07 at vulnerable and defended levels, preserve tool listing/call/result evidence, and check that the stated control matches what happened. Then test ASI07. Record model name, version, latency, reset steps, and cases where the model never attempts the unsafe call. A model refusal is an observation, not proof that the application boundary held.
5. **Learner pilot:** only after instructor smoke checks, ask a first-time learner whether setup and the chosen control comparison can be completed without coaching. Record the time and blockers. Keep it outside the required 40-hour path unless it teaches a distinct, repeatable outcome.

Adopt a student-facing optional guide only after the license, isolation, cross-platform, and teaching gates pass. If any gate fails, retain a credited upstream reference and keep BrokenPilot as the supported path. Revisit broader integration only when there is evidence that a specific course gap remains.

## Source-inspection note, 15 October 2026

The v2.0 tag resolves to the commit above. Source files were inspected without running the application. A native Windows Git checkout failed on `media/The "Adversarial" Red Team T-Shirt.png`, a filename Windows cannot create. The partial checkout was removed after reading the relevant source blobs. A Windows student path therefore needs an upstream filename change or a separately tested Linux-filesystem route. This note is not evidence that the labs run or that a safe setup has been validated.
