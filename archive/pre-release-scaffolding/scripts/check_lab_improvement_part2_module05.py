from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "labs" / "brokenpilot" / "prototype-app"

checks = [
    (BP / "app" / "controls.py", "ENABLE_OUTPUT_ENCODING"),
    (BP / "app" / "mock_llm.py", "USER_OVERRIDE:"),
    (BP / "app" / "mock_llm.py", "DIRECT_PROMPT_INJECTION_FOLLOWED"),
    (BP / "app" / "main.py", '@app.post("/render")'),
    (BP / "app" / "schemas.py", "class RenderRequest"),
    (BP / "tests" / "test_basic.py", "test_direct_prompt_injection_default_changes_behavior"),
    (BP / "tests" / "test_basic.py", "test_render_output_encoding_control_escapes_model_output"),
    (BP / "DIRECT_PROMPT_INJECTION_LAB.md", "Direct and indirect prompt injection have the same root cause"),
    (BP / "OUTPUT_HANDLING_LAB.md", "context-appropriate output handling at the sink"),
    (ROOT / "modules" / "05-llm-application-security" / "brokenpilot-direct-injection-output-lab.md", "Required observations"),
]

for path, needle in checks:
    if not path.exists():
        raise SystemExit(f"Missing expected file: {path.relative_to(ROOT)}")
    if needle not in path.read_text(encoding="utf-8"):
        raise SystemExit(f"Missing expected text in {path.relative_to(ROOT)}: {needle}")

docs = json.loads((BP / "data" / "documents.json").read_text(encoding="utf-8"))
if not any(doc.get("id") == "DOC-007" and "OUTPUT_SINK_TRIGGERED" in doc.get("body", "") for doc in docs):
    raise SystemExit("DOC-007 output sink training document missing")

print("Lab improvement Part 2 Module 05 checks passed.")
