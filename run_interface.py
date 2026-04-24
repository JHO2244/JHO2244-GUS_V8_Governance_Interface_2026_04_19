"""
GUS v8 Governance Interface
Canonical Entrypoint v0.2
"""

from app.ui_shell.runtime.runtime_controller import (
    handle_runtime_command_v0_1,
)

APP_NAME = "GUS Governance Interface"
VERSION = "v0.2"
BACKEND_AUTHORITY = "GUS v7 Governance Integrity Vehicle (GIV)"


def print_runtime_result(result: dict) -> None:
    print("Result:", result["result"])
    print("Active Route:", result["session"]["active_route"])

    payload = result["payload"]

    if result["result"] == "ROUTE_CHANGED":
        print("Screen:", payload["active_screen_content"]["screen_id"])
        print("Renderer:", payload["active_screen_content"]["screen_renderer"])
        return

    if result["result"] == "HELP":
        print("Available Commands:", ", ".join(payload["available_commands"]))
        return

    print("Message:", payload["message"])


def launch_interface() -> None:
    print("=" * 50)
    print(APP_NAME)
    print(VERSION)
    print("Backend Authority:", BACKEND_AUTHORITY)
    print("Status: Interactive Runtime Dashboard Initialized")
    print("Type 'help' for commands. Type 'quit' to exit.")
    print("=" * 50)

    active_route = "home_dashboard"

    while True:
        command = input("gus-v8> ")
        result = handle_runtime_command_v0_1(command, active_route)
        print_runtime_result(result)

        if result["result"] == "QUIT":
            break

        active_route = result["session"]["active_route"]


if __name__ == "__main__":
    launch_interface()
