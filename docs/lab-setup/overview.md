# Lab Setup Overview

The course combines local hands-on targets with tabletop and design exercises. BrokenPilot is the primary course-owned application for LLM, RAG, agent, and capstone work. The toy classifier supports selected adversarial ML exercises. DVAIA is optional external practice.

## Choose a path

| Goal | Target | Runtime |
|---|---|---|
| Prompt injection, retrieval authorization, tool actions, memory, output handling | [BrokenPilot](../labs/brokenpilot/prototype-app/README.md) | Local Python or Docker Compose |
| Ticket-to-retrieval-to-agent chain | [BrokenPilot guided exercise](../labs/brokenpilot/prototype-app/TICKET_TO_AGENT_LAB.md) | Local Python |
| Evasion and other toy classifier behavior | [Toy classifier lab](../labs/toy-ml-attacks/toy-classifier-app/README.md) | Local Python |
| Architecture, MLOps, privacy, and risk review | Module handouts and supplied evidence | No service required |

## Start BrokenPilot

Install the requirements from `labs/brokenpilot/prototype-app`, then run `python run_lab.py --profile vulnerable` and open `http://127.0.0.1:8010`. The app binds to the local loopback interface. For each control comparison, stop the process with `Ctrl+C`, start the named control profile, recreate any in-memory setup, and repeat the request. The guided UI shows the active controls, responses, tickets, and an evidence notebook that stays in the same browser across server restarts.

Use only fake data. The vulnerable profile intentionally lacks several security checks and must not be exposed on a network. No course account, online service, downloaded model, or flag validation is required for the supported lab path.

The optional DVAIA materials document a separately validated historical lab path. They are not required to complete the BrokenPilot exercises. The [standalone path](brokenpilot-standalone-path.md) maps the course modules to the local target.
