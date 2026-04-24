"""
GUS v8 Governance Interface
Runtime Commands v0.1
"""

from typing import Final


COMMAND_TO_ROUTE: Final[dict[str, str]] = {
    "home": "home_dashboard",
    "case_input": "case_input",
    "verdict": "verdict",
    "explanation": "explanation",
    "trust": "trust",
    "metrics": "metrics",
}

CONTROL_COMMANDS: Final[tuple[str, ...]] = (
    "help",
    "quit",
)

RUNTIME_COMMANDS: Final[tuple[str, ...]] = tuple(COMMAND_TO_ROUTE) + CONTROL_COMMANDS


def normalize_runtime_command_v0_1(command: str) -> str:
    if not isinstance(command, str):
        raise TypeError("runtime command must be a str")

    return command.strip().lower()


def build_runtime_command_help_v0_1() -> dict:
    return {
        "help_name": "runtime_command_help",
        "help_version": "v0.1",
        "available_commands": RUNTIME_COMMANDS,
        "command_mode": "DETERMINISTIC_LOCAL_RUNTIME",
        "authority_mode": "ADVISORY_ONLY",
        "unknown_command_behavior": "FAIL_CLOSED",
    }
