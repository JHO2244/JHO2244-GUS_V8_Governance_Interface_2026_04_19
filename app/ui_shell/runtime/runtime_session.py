"""
GUS v8 Governance Interface
Runtime Session v0.1
"""

from app.ui_shell.routing.runtime_contract import (
    build_runtime_contract_v0_1,
)


def build_runtime_session_v0_1(
    active_route: str | None = None,
) -> dict:
    contract = build_runtime_contract_v0_1()

    resolved_route = active_route or contract["default_route"]

    if resolved_route not in contract["allowed_routes"]:
        raise ValueError(
            f"Unknown runtime session route: {resolved_route}"
        )

    return {
        "session_name": "governance_runtime_session",
        "session_version": "v0.1",
        "active_route": resolved_route,
        "allowed_routes": contract["allowed_routes"],
        "authority_mode": contract["authority_mode"],
        "session_mode": "LOCAL_INTERACTIVE_RUNTIME",
        "persistence": "NONE",
    }
