"""
GUS v8 Governance Interface
Navigation Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.ui_shell.layout.shell_layout_model import (
    build_shell_layout_model_v0_1,
)


def build_navigation_renderer_v0_1(
    active_route: str,
) -> dict:
    if not isinstance(active_route, str):
        raise TypeError("active_route must be a str")

    layout = build_shell_layout_model_v0_1()

    lines = []

    for item in layout["side_nav"]["items"]:
        marker = "ACTIVE" if item["route"] == active_route else "READY"
        lines.append(f"{item['label']} | {marker}")

    return build_panel_card_v0_1(
        card_id="navigation_panel",
        title="Navigation",
        body=tuple(lines),
        emphasis="high",
    )
