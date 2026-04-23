from app.screens.home_dashboard.home_dashboard_renderer import (
    build_home_dashboard_renderer_v0_1,
)
from app.screens.verdict.verdict_screen_renderer import (
    build_verdict_screen_renderer_v0_1,
)


def test_phase12_home_dashboard_renderer_builds_cleanly() -> None:
    rendered = build_home_dashboard_renderer_v0_1()

    assert rendered["screen_renderer"] == "home_dashboard_renderer"
    assert rendered["version"] == "v0.1"
    assert rendered["screen_id"] == "home_dashboard"
    assert rendered["layout_role"] == "executive_command_center"
    assert len(rendered["panels"]) == 4

    assert rendered["panels"][0]["title"] == "Governance Interface"
    assert rendered["panels"][1]["title"] == "System Trust"
    assert rendered["panels"][2]["title"] == "Quick Actions"
    assert rendered["panels"][3]["title"] == "Operational Summary"


def test_phase12_verdict_screen_renderer_builds_cleanly() -> None:
    rendered = build_verdict_screen_renderer_v0_1()

    assert rendered["screen_renderer"] == "verdict_screen_renderer"
    assert rendered["version"] == "v0.1"
    assert rendered["screen_id"] == "verdict"
    assert rendered["layout_role"] == "decision_chamber"
    assert len(rendered["panels"]) == 4

    assert rendered["panels"][0]["title"] == "Governance Verdict"
    assert rendered["panels"][1]["title"] == "Executive Summary"
    assert rendered["panels"][2]["title"] == "Decision Sections"
    assert rendered["panels"][3]["title"] == "Contract Binding"


def test_phase12_home_dashboard_renderer_uses_trusted_content() -> None:
    rendered = build_home_dashboard_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Backend Binding: BOUND_TO_GIV" in rendered["panels"][1]["body"]
    assert "Open Case Input" in rendered["panels"][2]["body"]
    assert "Verified" in rendered["panels"][3]["body"]


def test_phase12_verdict_renderer_uses_trusted_content() -> None:
    rendered = build_verdict_screen_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_VERDICT_DISPLAY" in rendered["panels"][0]["body"]
    assert "Decision-ready verdict display" in rendered["panels"][1]["body"]
    assert "summary" in rendered["panels"][2]["body"]
    assert "Contract: governance_verdict_output" in rendered["panels"][3]["body"]
