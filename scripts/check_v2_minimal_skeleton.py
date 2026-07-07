from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "labs" / "brokenpilot-v2" / "prototype-app"

REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    "app/main.py",
    "app/orchestrator.py",
    "app/agents.py",
    "app/broker.py",
    "app/registry.py",
    "app/audit.py",
    "app/schemas.py",
    "tests/test_minimal_skeleton.py",
]

REQUIRED_TOKENS = {
    "app/orchestrator.py": ["MessageEnvelope", "descriptor_resolved", "tool_broker_decision", "agent_invoked"],
    "app/registry.py": ["descriptor_hash", "trusted=True", "mcp-desc-retrieval-agent-v1"],
    "app/broker.py": ["capability_not_advertised_by_descriptor", "descriptor_and_capability_allowed"],
    "tests/test_minimal_skeleton.py": ["test_audit_trace_records_delegation_path", "test_broker_denies_capability_not_in_descriptor"],
    "README.md": ["secure-by-default", "MCP-like descriptor registry", "not yet a student lab"],
}


def main() -> None:
    errors: list[str] = []

    if not APP.exists():
        errors.append(f"missing app directory: {APP.relative_to(ROOT)}")
    else:
        for rel in REQUIRED_FILES:
            path = APP / rel
            if not path.exists():
                errors.append(f"missing: {path.relative_to(ROOT)}")

        for rel, tokens in REQUIRED_TOKENS.items():
            path = APP / rel
            if path.exists():
                text = path.read_text(encoding="utf-8")
                for token in tokens:
                    if token not in text:
                        errors.append(f"{path.relative_to(ROOT)} missing token: {token}")

    if errors:
        print("v2 minimal skeleton check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("v2 minimal skeleton structure check passed.")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests"],
        cwd=APP,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    print("v2 minimal skeleton tests passed.")


if __name__ == "__main__":
    main()
