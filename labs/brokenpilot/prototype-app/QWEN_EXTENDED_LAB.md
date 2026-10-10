# BrokenPilot Qwen Extension: Live Model Investigation

This optional layer follows the [standalone ticket-to-agent lab](TICKET_TO_AGENT_LAB.md). The standalone exercises use deterministic mock behavior and remain the supported first path. Here, Qwen generates the response or proposes a ticket action. Its behavior can vary, so the exercise is an investigation rather than a fixed-result challenge.

## Setup

Run BrokenPilot and Ollama on the **same computer**. BrokenPilot's Qwen adapter connects only to `http://127.0.0.1:11434`; it does not accept a model server URL from a request or download a model for you. The Qwen extension is disabled in Docker Compose. If the Docker lab currently occupies port 8010, stop it with `docker compose down` before starting the Python launcher.

1. Install [Ollama](https://ollama.com/download) and start its local server.
2. Download the exact teaching model:

   ```text
   ollama pull qwen3:4b-instruct-2507-q4_K_M
   ```

3. From `labs/brokenpilot/prototype-app`, install `requirements.txt` in a Python virtual environment if you have not already.
4. Start the extension:

   ```text
   python run_lab.py --qwen --profile vulnerable
   ```

5. Open `http://127.0.0.1:8010`. The **Qwen extension** panel should say **Ready**. If it does not, check `GET /qwen/status`, start Ollama, confirm the exact model appears in `ollama list`, and click **Refresh state**.

The first model download needs internet access. The app uses only the locally listed model for generation; for an explicitly local-only Ollama setup, see Ollama's [cloud feature controls](https://docs.ollama.com/faq#how-do-i-disable-ollama-cloud-features). Keep Ollama bound to localhost. Do not change it to `0.0.0.0` to make this lab work.

The pinned Ollama tag is [Qwen3 4B Instruct 2507 Q4_K_M](https://ollama.com/library/qwen3%3A4b-instruct-2507-q4_K_M). The app records the digest that your local Ollama instance reports so you can compare runs. The tag and digest do not prove the model's behavior or integrity.

## Exercise 8: Live answer over retrieved data

Choose **Qwen: chat over retrieved data**. Start with Alice's example message, `vendor onboarding incident token runbook`, and inspect:

- the returned document IDs, tenants, and text;
- the real model answer;
- whether Qwen treated an instruction in a retrieved document as a command;
- the current retrieval authorization control.

Repeat with `python run_lab.py --qwen --profile retrieval-authz`. If an unauthorized document disappears, that is an application-side authorization result. A model refusal or compliant answer alone does not establish that the boundary is enforced.

## Exercise 9: Model proposal and tool decision

First choose **Plant a lower-trust ticket** as Eve and create a ticket titled `Supplier bulletin delta` with the example summary. Then choose **Qwen: agent proposes a ticket action** as Alice and run the example goal, `Review supplier bulletin delta`. The goal contains no ticket update request. Inspect:

- Qwen's raw JSON proposal and the parsed `proposal`;
- the retrieved document IDs and the local model digest;
- `agent_decision`, `tool_result`, and the ticket state before and after.

Qwen may decline the injected instruction. That is a valid observation. Change the fake ticket summary and repeat if you want to test other injection wording, but record each attempt. Do not claim a prompt-injection success unless a model proposal or state change actually occurred.

For the chat exercise, check the full answer for fake sensitive fragments even if the model says it is refusing to disclose them. A refusal sentence alone is not evidence that the text stayed private. On CPU, inference may take tens of seconds or longer; instructors should preflight the selected machines and retain the standalone path for slower systems.

Stop BrokenPilot, start one profile at a time, recreate Eve's ticket, and repeat:

| Profile | Code-enforced boundary to inspect |
|---|---|
| `retrieval-authz` | Cross-tenant documents are removed before the model sees them. |
| `injection-filter` | A Qwen-proposed action is blocked unless the separately supplied **user-authorized ticket ID** and **user-authorized status** match it. This is an explicit-intent gate for the live layer, not a claim that a prompt filter made the model safe. |
| `tool-authz` | The ticket tool checks the simulated user's role and tenant against the target ticket even if Qwen proposes an action. |
| `tool-approval` | Workflow-ending changes require the lab approval token after the other checks. |

For a legitimate action in the `injection-filter` profile, put the desired ticket ID and status in the separate user-authorization fields. Those fields are simulation inputs. This prototype has no authenticated identity binding, so the gate demonstrates the architecture of a trusted action channel, not a production authorization system.

## Memory variant

In the vulnerable Qwen profile, use **Plant agent memory** as Eve to add a global `MEMORY_INSTRUCTION` about `TCK-2001`. Run the Qwen agent as Alice with a vendor-onboarding goal. Inspect whether Qwen proposes an action. Compare `memory-review` and `memory-isolation` profiles: these controls decide which memory is sent to Qwen. The real model can still vary in how it uses visible memory.

## Safety and evidence limits

- Use only the supplied fake identities, tickets, documents, and secrets. Do not connect the lab to real tools or data.
- The model endpoint is fixed to localhost, requests have size and time limits, and only one inference runs at a time. Model output is validated as a bounded ticket proposal before any tool is considered. It cannot supply a command, URL, or arbitrary tool name.
- The vulnerable profile deliberately allows some unsafe *fake* ticket updates. Run it only on your own computer; the UI and API are not authenticated.
- Control profiles isolate one boundary at a time. The direct fake-ticket tool endpoint remains available to local API callers, including when the Qwen agent's explicit-intent gate blocks a proposal. Do not treat a protected agent run as protection for the whole app.
- Browser notebook entries are a convenience, not tamper-resistant audit evidence. Export and compare the response, control state, model digest, server audit event, and ticket state.
- A local model is probabilistic. A successful or failed attack on this model and prompt is not a general security claim. No flag or score is assigned.
