from typing import Any
from .controls import Controls

MALICIOUS_MARKERS = [
    "MALICIOUS_INSTRUCTION:",
    "IGNORE_PREVIOUS_INSTRUCTIONS:",
    "SYSTEM_OVERRIDE:",
]


def _find_malicious_instructions(documents: list[dict[str, Any]]) -> list[str]:
    found: list[str] = []
    for doc in documents:
        body = doc.get("body", "")
        for marker in MALICIOUS_MARKERS:
            if marker in body:
                after = body.split(marker, 1)[1].strip()
                found.append(f"{doc.get('id')}: {after}")
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


def generate_answer(
    *,
    user: dict[str, Any],
    message: str,
    retrieved_documents: list[dict[str, Any]],
    controls: Controls,
) -> dict[str, Any]:
    malicious = _find_malicious_instructions(retrieved_documents)
    sensitive = _fake_sensitive_fragments(retrieved_documents)
    titles = [f"{doc.get('id')}  -  {doc.get('title')}" for doc in retrieved_documents]

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
        "This is deterministic mock output, not a real model response.",
    ]

    return {
        "mode": "normal",
        "answer": "\n".join(answer),
        "security_observation": "No malicious retrieved instruction was detected in the selected context.",
    }
