# Qwen classroom preflight

Run this before offering the optional live-model exercises. The deterministic BrokenPilot exercises remain the supported path for every student.

## Prepare

Use a machine representative of each laptop class in the cohort. Start Ollama locally and install the exact model in the [Qwen extended lab](../labs/brokenpilot/prototype-app/QWEN_EXTENDED_LAB.md). Keep Ollama bound to localhost. The first download requires internet; the preflight itself uses the local model and fake seeded data.

From `labs/brokenpilot/prototype-app`, install the pinned direct requirements and run:

```text
python -m pip install -r requirements.txt
python preflight_qwen.py --output qwen-preflight.json
```

The output file must not exist already. The script does not need a running BrokenPilot server. It sets the vulnerable teaching profile in its own process, runs one chat request and one agent-proposal request, and resets only its own fake state before exiting. A separately running BrokenPilot server is unaffected. It never downloads a model or contacts a course service. The report includes platform, host logical CPU count, model digest, response times, retrieved document IDs, full model text, proposal, application decision, and final fake-ticket state. Record any Ollama container CPU or memory limit separately; the host CPU count does not describe that limit.

## Decide whether to use it live

- **Ready for a classroom trial:** model status is `ready`, report outcome is `completed`, and both requests return HTTP 200 within your allocated lab time.
- **Use the standalone path:** the model is missing, either request fails or times out, or the response time would consume the exercise period. Do not widen the network bind to troubleshoot.
- **Record behavior, do not grade it:** a refusal, a fake-token echo inside a refusal, a proposal, and no proposal are all possible observations. A single run does not establish a model's general resistance to prompt injection.

Run the preflight on the operating systems and hardware you plan to support. One successful instructor laptop does not qualify a full cohort. For the first offering, retain an instructor-controlled machine for the optional Qwen demonstration if student hardware is uncertain. Capture the report and note the decision to include or defer Exercises 8 and 9.

One local Windows check on 11 October 2026 used a Docker Ollama container limited to four CPU cores and 8 GB of memory. The chat took 67.44 seconds and echoed a fake token within a refusal; the agent took 23.47 seconds and proposed no ticket update. Both requests returned HTTP 200 with model digest prefix `0edcdef34593`. This is one timing and behavior sample, not a class-wide performance estimate or an attack-success rate.

The report contains only seeded fake lab content when the script is run against the supplied data. Store it with your normal class preparation notes. This is a readiness record, not tamper-resistant audit evidence.
