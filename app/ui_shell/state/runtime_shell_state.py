"""
GUS v8 Governance Interface
Runtime Shell State v0.1
"""

from app.ui_shell.layout.shell_layout_model import build_shell_layout_model_v0_1
from app.ui_shell.routing.screen_router import render_route_v0_1


def build_runtime_shell_state_v0_1(route_name: str | None = None) -> dict:
    layout = build_shell_layout_model_v0_1()
    rendered = render_route_v0_1(route_name)

    return {
        "shell_name": "governance_runtime_shell_state",
        "shell_version": "v0.1",
        "active_route": rendered["route"],
        "layout": layout,
        "active_screen": rendered["screen_content"],
    }
