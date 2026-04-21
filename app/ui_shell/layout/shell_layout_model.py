"""
GUS v8 Governance Interface
Shell Layout Model v0.1
"""

from app.ui_shell.routing.runtime_contract import build_runtime_contract_v0_1
from app.ui_shell.theme.theme_profile import get_theme_profile


def build_shell_layout_model_v0_1() -> dict:
    contract = build_runtime_contract_v0_1()
    theme = get_theme_profile()

    nav_items = []

    for route in contract["allowed_routes"]:
        nav_items.append(
            {
                "route": route,
                "label": contract["route_labels"][route],
            }
        )

    return {
        "layout_name": "governance_runtime_shell",
        "layout_version": "v0.1",
        "default_route": contract["default_route"],
        "top_bar": {
            "title": "GUS v8 Governance Interface",
            "subtitle": "Runtime Shell",
            "authority_mode": contract["authority_mode"],
        },
        "side_nav": {
            "items": tuple(nav_items),
        },
        "content_frame": {
            "unknown_route_behavior": contract["unknown_route_behavior"],
            "panel_mode": "DETERMINISTIC_SCREEN_LOAD",
        },
        "theme_name": theme["theme_name"],
    }
