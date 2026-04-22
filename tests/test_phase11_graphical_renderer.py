from app.components.panel_card import build_panel_card_v0_1
from app.ui_shell.layout.graphical_shell_renderer import (
    build_graphical_shell_renderer_v0_1,
)
from app.ui_shell.navigation.navigation_renderer import (
    build_navigation_renderer_v0_1,
)


def test_phase11_panel_card_v0_1_builds_cleanly() -> None:
    card = build_panel_card_v0_1(
        card_id="test_card",
        title="Test Card",
        body=("Line 1", "Line 2"),
        emphasis="high",
    )

    assert card["component"] == "panel_card"
    assert card["version"] == "v0.1"
    assert card["card_id"] == "test_card"
    assert card["title"] == "Test Card"
    assert card["body"] == ("Line 1", "Line 2")
    assert card["emphasis"] == "high"


def test_phase11_navigation_renderer_marks_active_route() -> None:
    nav = build_navigation_renderer_v0_1("trust")

    assert nav["component"] == "panel_card"
    assert nav["card_id"] == "navigation_panel"
    assert nav["title"] == "Navigation"
    assert "Trust | ACTIVE" in nav["body"]
    assert "Home | READY" in nav["body"]


def test_phase11_graphical_shell_renderer_builds_trust_view() -> None:
    rendered = build_graphical_shell_renderer_v0_1("trust")

    assert rendered["renderer_name"] == "graphical_shell_renderer"
    assert rendered["renderer_version"] == "v0.1"
    assert rendered["theme_name"] == "Governance Calm"

    assert rendered["top_bar"]["title"] == "GUS v8 Governance Interface"
    assert rendered["top_bar"]["body"] == (
        "Runtime Shell",
        "ADVISORY_ONLY",
    )

    assert rendered["navigation"]["title"] == "Navigation"
    assert "Trust | ACTIVE" in rendered["navigation"]["body"]

    assert rendered["active_screen_panel"]["title"] == "Governance Trust Panel"
    assert rendered["active_screen_panel"]["body"] == (
        "Route: trust",
        "Mode: READ_ONLY_TRUST_DISPLAY",
        "Contract: governance_trust_output",
    )


def test_phase11_graphical_shell_renderer_defaults_cleanly() -> None:
    rendered = build_graphical_shell_renderer_v0_1()

    assert rendered["renderer_name"] == "graphical_shell_renderer"
    assert rendered["top_bar"]["component"] == "panel_card"
    assert rendered["navigation"]["component"] == "panel_card"
    assert rendered["active_screen_panel"]["component"] == "panel_card"
