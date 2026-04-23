from app.ui_shell.layout.graphical_shell_renderer import (
    build_graphical_shell_renderer_v0_1,
)
from app.ui_shell.routing.screen_router import (
    UnknownRouteError,
    render_route_v0_1,
)
from app.ui_shell.routing.route_registry import build_route_registry_v0_1
from app.ui_shell.state.runtime_shell_state import (
    build_runtime_shell_state_v0_1,
)


def test_phase14_route_registry_uses_rich_room_builders() -> None:
    registry = build_route_registry_v0_1()

    assert registry["default_route"] == "home_dashboard"
    assert registry["allowed_routes"] == (
        "home_dashboard",
        "case_input",
        "verdict",
        "explanation",
        "trust",
        "metrics",
    )
    assert set(registry["route_builders"]) == set(registry["allowed_routes"])


def test_phase14_screen_router_returns_screen_content() -> None:
    rendered = render_route_v0_1("trust")

    assert rendered["route"] == "trust"
    assert "screen_content" in rendered
    assert rendered["screen_content"]["screen_renderer"] == "trust_panel_renderer"
    assert rendered["screen_content"]["layout_role"] == "integrity_console"


def test_phase14_screen_router_fails_closed_on_unknown_route() -> None:
    try:
        render_route_v0_1("fake_route")
        assert False, "Expected UnknownRouteError"
    except UnknownRouteError as exc:
        assert str(exc) == "Unknown runtime route: fake_route"


def test_phase14_runtime_shell_state_uses_routed_screen_content() -> None:
    shell = build_runtime_shell_state_v0_1("metrics")

    assert shell["active_route"] == "metrics"
    assert shell["active_screen"]["screen_renderer"] == "metrics_dashboard_renderer"
    assert shell["active_screen"]["layout_role"] == "telemetry_room"


def test_phase14_graphical_shell_renderer_exposes_real_home_room() -> None:
    rendered = build_graphical_shell_renderer_v0_1("home_dashboard")

    assert rendered["active_route"] == "home_dashboard"
    assert rendered["top_bar"]["component"] == "top_bar"
    assert rendered["navigation"]["title"] == "Navigation"
    assert "Home | ACTIVE" in rendered["navigation"]["body"]

    active = rendered["active_screen_content"]
    assert active["screen_renderer"] == "home_dashboard_renderer"
    assert active["layout_role"] == "executive_command_center"


def test_phase14_graphical_shell_renderer_exposes_real_verdict_room() -> None:
    rendered = build_graphical_shell_renderer_v0_1("verdict")

    assert rendered["active_route"] == "verdict"
    assert "Verdict | ACTIVE" in rendered["navigation"]["body"]

    active = rendered["active_screen_content"]
    assert active["screen_renderer"] == "verdict_screen_renderer"
    assert active["layout_role"] == "decision_chamber"


def test_phase14_graphical_shell_renderer_exposes_real_explanation_room() -> None:
    rendered = build_graphical_shell_renderer_v0_1("explanation")

    assert rendered["active_route"] == "explanation"
    assert "Explanation | ACTIVE" in rendered["navigation"]["body"]

    active = rendered["active_screen_content"]
    assert active["screen_renderer"] == "explanation_panel_renderer"
    assert active["layout_role"] == "reasoning_room"
