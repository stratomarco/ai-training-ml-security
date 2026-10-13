"""Start one explicit BrokenPilot teaching profile on the loopback interface."""

from __future__ import annotations

import argparse
import os

import uvicorn


CONTROL_NAMES = {
    "retrieval_authz": "ENABLE_RETRIEVAL_AUTHZ",
    "prompt_injection_filter": "ENABLE_PROMPT_INJECTION_FILTER",
    "tool_authz": "ENABLE_TOOL_AUTHZ",
    "tool_approval": "ENABLE_TOOL_APPROVAL",
    "memory_review": "ENABLE_MEMORY_REVIEW",
    "memory_isolation": "ENABLE_MEMORY_ISOLATION",
    "output_encoding": "ENABLE_OUTPUT_ENCODING",
    "hub_least_privilege": "ENABLE_HUB_LEAST_PRIVILEGE",
    "hub_diagnostic_redaction": "ENABLE_HUB_DIAGNOSTIC_REDACTION",
}

PROFILES = {
    "vulnerable": set(),
    "retrieval-authz": {"retrieval_authz"},
    "injection-filter": {"prompt_injection_filter"},
    "tool-authz": {"tool_authz"},
    "tool-approval": {"tool_approval"},
    "memory-review": {"memory_review"},
    "memory-isolation": {"memory_isolation"},
    "output-encoding": {"output_encoding"},
    "hub-least-privilege": {"hub_least_privilege"},
    "hub-redaction": {"hub_diagnostic_redaction"},
    "all-controls": set(CONTROL_NAMES),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=PROFILES, default="vulnerable")
    parser.add_argument("--port", type=int, default=8010)
    parser.add_argument("--qwen", action="store_true", help="Enable the optional local Ollama/Qwen extension")
    args = parser.parse_args()

    for short_name, env_name in CONTROL_NAMES.items():
        os.environ[env_name] = "true" if short_name in PROFILES[args.profile] else "false"
    os.environ["ENABLE_AUDIT_LOG"] = "true"
    os.environ["BROKENPILOT_QWEN_ENABLED"] = "1" if args.qwen else "0"

    print(f"BrokenPilot profile: {args.profile}", flush=True)
    print(f"Open http://127.0.0.1:{args.port}", flush=True)
    if args.qwen:
        print("Qwen extension: local Ollama model required at 127.0.0.1:11434.", flush=True)
    print("Stop with Ctrl+C before switching profiles.", flush=True)
    uvicorn.run("app.main:app", host="127.0.0.1", port=args.port)


if __name__ == "__main__":
    main()
