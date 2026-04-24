"""
GUS v8 Governance Interface
Runtime Controller v0.1
"""

from app.ui_shell.layout.graphical_shell_renderer import (
    build_graphical_shell_renderer_v0_1,
)
from app.ui_shell.runtime.runtime_commands import (
    COMMAND_TO_ROUTE,
    build_runtime_command_help_v0_1,
    normalize_runtime_command_v0_1,
)
from app.ui_shell.runtime.runtime_session import (
    build_runtime_session_v0_1,
)


def handle_runtime_command_v0_1(
    command: str,
    active_route: str | None = None,
) -> dict:
    normalized = normalize_runtime_command_v0_1(command)
    session = build_runtime_session_v0_1(active_route)

    if normalized == "help":
        return {
            "result": "HELP",
            "session": session,
            "payload": build_runtime_command_help_v0_1(),
        }

    if normalized == "quit":
        return {
            "result": "QUIT",
            "session": session,
            "payload": {"message": "Runtime session closed"},
        }

    if normalized in COMMAND_TO_ROUTE:
        next_route = COMMAND_TO_ROUTE[normalized]
        next_session = build_runtime_session_v0_1(next_route)

        return {
            "result": "ROUTE_CHANGED",
            "session": next_session,
            "payload": build_graphical_shell_renderer_v0_1(
                next_route
            ),
        }

    return {
        "result": "UNKNOWN_COMMAND",
        "session": session,
        "payload": {
            "message": f"Unknown command: {normalized}",
            "behavior": "FAIL_CLOSED",
        },
    }
