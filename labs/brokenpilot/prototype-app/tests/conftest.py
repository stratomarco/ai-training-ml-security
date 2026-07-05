from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CONTROL_ENV_VARS = [
    "ENABLE_RETRIEVAL_AUTHZ",
    "ENABLE_PROMPT_INJECTION_FILTER",
    "ENABLE_TOOL_AUTHZ",
    "ENABLE_TOOL_APPROVAL",
    "ENABLE_MEMORY_REVIEW",
    "ENABLE_MEMORY_ISOLATION",
    "ENABLE_AUDIT_LOG",
    "ENABLE_OUTPUT_ENCODING",
]


def _clear_control_env_vars() -> None:
    """Keep tests deterministic even after manual lab validation.

    The BrokenPilot labs intentionally use environment variables to toggle controls.
    Instructors often run manual validations in the same shell, for example:

        $env:ENABLE_TOOL_AUTHZ="true"

    Without clearing those variables, tests that are meant to validate the vulnerable
    default mode may unexpectedly run in hardened mode. The app still reads controls
    from the environment at request time; this fixture only ensures each test starts
    from the documented lab defaults.
    """
    for name in CONTROL_ENV_VARS:
        os.environ.pop(name, None)


def pytest_runtest_setup(item):
    _clear_control_env_vars()
