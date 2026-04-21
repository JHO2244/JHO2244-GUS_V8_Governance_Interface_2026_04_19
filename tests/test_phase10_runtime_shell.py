from app.ui_shell.layout.shell_layout_model import build_shell_layout_model_v0_1
from app.ui_shell.routing.route_registry import build_route_registry_v0_1
from app.ui_shell.routing.runtime_contract import build_runtime_contract_v0_1
from app.ui_shell.routing.screen_router import (
    UnknownRouteError,
    render_route_v0_1,
)
from app.ui_shell.state.runtime_shell_state import build_runtime_shell_state_v0_1


def test_phase10_runtime_contract_v0_1_is_locked() -> None:
    contract = build_runtime_contract_v0_1()

    assert contract["contract_name"] == "governance_runtime_contract"
    assert contract["contract_version"] == "v0.1"
    assert contract["default_route"] == "home_dashboard"
    assert contract["unknown_route_behavior"] == "FAIL_CLOSED"
    assert contract["authority_mode"] == "ADVISORY_ONLY"
    assert contract["allowed_routes"] == (
        "home_dashboard",
        "case_input",
        "verdict",
        "explanation",
        "trust",
        "metrics",
    )


def test_phase10_route_registry_v0_1_matches_contract() -> None:
    registry = build_route_registry_v0_1()

    assert registry["registry_name"] == "governance_route_registry"
    assert registry["registry_version"] == "v0.1"
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


def test_phase10_shell_layout_model_v0_1_uses_runtime_contract() -> None:
    layout = build_shell_layout_model_v0_1()

    assert layout["layout_name"] == "governance_runtime_shell"
    assert layout["layout_version"] == "v0.1"
    assert layout["default_route"] == "home_dashboard"
    assert layout["top_bar"]["authority_mode"] == "ADVISORY_ONLY"
    assert layout["content_frame"]["unknown_route_behavior"] == "FAIL_CLOSED"
    assert layout["content_frame"]["panel_mode"] == "DETERMINISTIC_SCREEN_LOAD"
    assert layout["theme_name"] == "Governance Calm"
    assert layout["side_nav"]["items"] == (
        {"route": "home_dashboard", "label": "Home"},
        {"route": "case_input", "label": "Case Input"},
        {"route": "verdict", "label": "Verdict"},
        {"route": "explanation", "label": "Explanation"},
        {"route": "trust", "label": "Trust"},
        {"route": "metrics", "label": "Metrics"},
    )


def test_phase10_screen_router_v0_1_defaults_to_home_dashboard() -> None:
    rendered = render_route_v0_1()

    assert rendered["route"] == "home_dashboard"
    assert rendered["screen_model"]["dashboard_id"] == "home_dashboard"


def test_phase10_screen_router_v0_1_renders_known_route() -> None:
    rendered = render_route_v0_1("explanation")

    assert rendered["route"] == "explanation"
    assert rendered["screen_model"]["screen_id"] == "explanation"
    assert rendered["screen_model"]["mode"] == "READ_ONLY_EXPLANATION_DISPLAY"


def test_phase10_screen_router_v0_1_fails_closed_on_unknown_route() -> None:
    try:
        render_route_v0_1("fake_route")
        assert False, "Expected UnknownRouteError"
    except UnknownRouteError as exc:
        assert str(exc) == "Unknown runtime route: fake_route"


def test_phase10_runtime_shell_state_v0_1_composes_layout_and_screen() -> None:
    shell = build_runtime_shell_state_v0_1("trust")

    assert shell["shell_name"] == "governance_runtime_shell_state"
    assert shell["shell_version"] == "v0.1"
    assert shell["active_route"] == "trust"
    assert shell["layout"]["layout_name"] == "governance_runtime_shell"
    assert shell["active_screen"]["screen_id"] == "trust"
    assert shell["active_screen"]["mode"] == "READ_ONLY_TRUST_DISPLAY"
