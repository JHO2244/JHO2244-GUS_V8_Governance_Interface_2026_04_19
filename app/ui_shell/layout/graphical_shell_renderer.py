"""
GUS v8 Governance Interface
Graphical Shell Renderer v0.1
"""

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

    top_bar = {
        "component": "top_bar",
        "title": shell["layout"]["top_bar"]["title"],
        "body": (
            shell["layout"]["top_bar"]["subtitle"],
            shell["layout"]["top_bar"]["authority_mode"],
        ),
    }

    navigation_panel = build_navigation_renderer_v0_1(
        shell["active_route"],
    )

    return {
        "renderer_name": "graphical_shell_renderer",
        "renderer_version": "v0.1",
        "theme_name": shell["layout"]["theme_name"],
        "active_route": shell["active_route"],
        "top_bar": top_bar,
        "navigation": navigation_panel,
        "active_screen_content": shell["active_screen"],
    }
