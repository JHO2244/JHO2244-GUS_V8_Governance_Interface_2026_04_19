"""
GUS v8 Governance Interface
Graphical Shell Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.ui_shell.navigation.navigation_renderer import (
    build_navigation_renderer_v0_1,
)
from app.ui_shell.state.runtime_shell_state import (
    build_runtime_shell_state_v0_1,
)


def build_graphical_shell_renderer_v0_1(
    route_name: str | None = None,
) -> dict:
    shell = build_runtime_shell_state_v0_1(route_name)
    screen = shell["active_screen"]

    if "title" in screen:
        screen_title = screen["title"]
    else:
        screen_title = shell["active_route"]

    body_lines = [f"Route: {shell['active_route']}"]

    if "mode" in screen:
        body_lines.append(f"Mode: {screen['mode']}")

    if "contract_name" in screen:
        body_lines.append(f"Contract: {screen['contract_name']}")

    active_screen_panel = build_panel_card_v0_1(
        card_id="active_screen_panel",
        title=screen_title,
        body=tuple(body_lines),
        emphasis="standard",
    )

    top_bar_panel = build_panel_card_v0_1(
        card_id="top_bar_panel",
        title=shell["layout"]["top_bar"]["title"],
        body=(
            shell["layout"]["top_bar"]["subtitle"],
            shell["layout"]["top_bar"]["authority_mode"],
        ),
        emphasis="high",
    )

    navigation_panel = build_navigation_renderer_v0_1(
        shell["active_route"],
    )

    return {
        "renderer_name": "graphical_shell_renderer",
        "renderer_version": "v0.1",
        "theme_name": shell["layout"]["theme_name"],
        "top_bar": top_bar_panel,
        "navigation": navigation_panel,
        "active_screen_panel": active_screen_panel,
    }
