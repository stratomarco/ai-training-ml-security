from typing import Any
import re
from .controls import Controls

MALICIOUS_MARKERS = [
    "MALICIOUS_INSTRUCTION:",
    "IGNORE_PREVIOUS_INSTRUCTIONS:",
    "SYSTEM_OVERRIDE:",
]

USER_INJECTION_MARKERS = [
    "USER_OVERRIDE:",
    "IGNORE_PREVIOUS_INSTRUCTIONS:",
    "SYSTEM_OVERRIDE:",
]

OUTPUT_SINK_RE = re.compile(r"\[\[INJECT:\s*(.*?)\]\]", re.IGNORECASE | re.DOTALL)


def _find_malicious_instructions(documents: list[dict[str, Any]]) -> list[str]:
    found: list[str] = []
    for doc in documents:
        body = doc.get("body", "")
        for marker in MALICIOUS_MARKERS:
            if marker in body:
                after = body.split(marker, 1)[1].strip()
                found.append(f"{doc.get('id')}: {after}")
    return found


def _find_user_injection(message: str) -> list[str]:
    found: list[str] = []
    for marker in USER_INJECTION_MARKERS:
        if marker in message:
            after = message.split(marker, 1)[1].strip()
            found.append(f"{marker} {after}")
    return found


def _fake_sensitive_fragments(documents: list[dict[str, Any]]) -> list[str]:
    fragments: list[str] = []
    for doc in documents:
        if doc.get("classification") in {"restricted", "confidential"}:
            # Keep it fake and explicit. This is teaching evidence, not a real leak.
            fragments.append(
                f"{doc.get('id')} ({doc.get('title')}): "
                f"{doc.get('training_secret', 'FAKE-SECRET-NOT-REAL')}"
            )
    return fragments


def _output_sink_fragments(documents: list[dict[str, Any]]) -> list[str]:
    fragments: list[str] = []
    for doc in documents:
        body = doc.get("body", "")
        for match in OUTPUT_SINK_RE.findall(body):
            fragments.append(f"{doc.get('id')}: {match.strip()}")
    return fragments


def generate_answer(
    *,
    user: dict[str, Any],
    message: str,
    retrieved_documents: list[dict[str, Any]],
    controls: Controls,
) -> dict[str, Any]:
    user_injections = _find_user_injection(message)
    malicious = _find_malicious_instructions(retrieved_documents)
    sensitive = _fake_sensitive_fragments(retrieved_documents)
    output_fragments = _output_sink_fragments(retrieved_documents)
    titles = [f"{doc.get('id')} - {doc.get('title')}" for doc in retrieved_documents]

    if user_injections and not controls.prompt_injection_filter:
        context_lines = [f"- {title}" for title in titles] if titles else ["- No retrieved context was available"]
        answer = [
            "DIRECT_PROMPT_INJECTION_FOLLOWED",
            "The mock assistant treated instruction-like text from the user message as authoritative.",
            "This simulates direct prompt injection at the user-input boundary.",
            "Injected user instruction(s):",
            *[f"- {item}" for item in user_injections],
            "The mock assistant exposed retrieved context summaries instead of staying within the intended task:",
            *context_lines,
        ]
        if sensitive:
            answer.extend(
                [
                    "Because retrieval authorization is not part of the prompt-injection control, fake sensitive fragments may still be present in retrieved context:",
                    *[f"- {item}" for item in sensitive],
                ]
            )
        if output_fragments:
            answer.extend(
                [
                    "Model supplied display fragment(s):",
                    *[f"- {item}" for item in output_fragments],
                ]
            )
        return {
            "mode": "vulnerable",
            "answer": "\n".join(answer),
            "security_observation": "User-controlled text was treated as instruction.",
        }

    if user_injections and controls.prompt_injection_filter:
        answer = [
            "DIRECT_PROMPT_INJECTION_BLOCKED",
            "The message contained instruction-like text, but the assistant treated it as untrusted user data.",
            "The user message can ask for work, but it cannot redefine system behavior or disclosure policy.",
            "Ignored user instruction marker(s):",
            *[f"- {item.split(':', 1)[0]}" for item in user_injections],
        ]
        return {
            "mode": "controlled",
            "answer": "\n".join(answer),
            "security_observation": "Instruction/data separation control was applied to user input.",
        }

    if malicious and not controls.prompt_injection_filter:
        answer = [
            "VULNERABLE_BEHAVIOR_DETECTED",
            "The mock assistant treated an instruction inside retrieved content as authoritative.",
            "This simulates indirect prompt injection in a RAG-style application.",
            "Retrieved instruction(s):",
            *[f"- {item}" for item in malicious],
        ]
        if sensitive:
            answer.extend(
                [
                    "Because the mock assistant followed the injected instruction, it included fake sensitive fragments from retrieved context:",
                    *[f"- {item}" for item in sensitive],
                ]
            )
        else:
            answer.append("No restricted fake fragments were present in the retrieved context.")
        if output_fragments:
            answer.extend(
                [
                    "Model supplied display fragment(s):",
                    *[f"- {item}" for item in output_fragments],
                ]
            )
        return {
            "mode": "vulnerable",
            "answer": "\n".join(answer),
            "security_observation": "Retrieved content was treated as instruction.",
        }

    if malicious and controls.prompt_injection_filter:
        answer = [
            "CONTROLLED_BEHAVIOR",
            "Retrieved content contained instruction-like text, but the assistant treated it as untrusted data.",
            "The user request will be answered only using trusted task context and allowed retrieved facts.",
            "Ignored retrieved instruction marker(s):",
            *[f"- {item.split(':', 1)[0]}" for item in malicious],
        ]
        return {
            "mode": "controlled",
            "answer": "\n".join(answer),
            "security_observation": "Instruction/data separation control was applied.",
        }

    retrieved_lines = [f"- {title}" for title in titles] if titles else ["- No matching documents"]
    answer = [
        f"User {user.get('id')} asked: {message}",
        "The mock assistant retrieved the following documents:",
        *retrieved_lines,
    ]
    if output_fragments:
        answer.extend(
            [
                "Model supplied display fragment(s):",
                *[f"- {item}" for item in output_fragments],
            ]
        )
    answer.append("This is deterministic mock output, not a real model response.")
    return {
        "mode": "normal",
        "answer": "\n".join(answer),
        "security_observation": "No malicious retrieved instruction was detected in the selected context.",
    }
