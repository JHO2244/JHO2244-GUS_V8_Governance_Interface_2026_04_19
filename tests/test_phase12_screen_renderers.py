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
    assert len(rendered["panels"]) == 5

    assert rendered["panels"][0]["title"] == "Governance Verdict — PASS"
    assert rendered["panels"][1]["title"] == "Transparent vendor selection accepted"
    assert rendered["panels"][2]["title"] == "Reason Codes"
    assert rendered["panels"][3]["title"] == "Trust State"
    assert rendered["panels"][4]["title"] == "Contract Binding"


def test_phase12_home_dashboard_renderer_uses_trusted_content() -> None:
    rendered = build_home_dashboard_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Backend Binding: BOUND_TO_GIV" in rendered["panels"][1]["body"]
    assert "Open Case Input" in rendered["panels"][2]["body"]
    assert "Verified" in rendered["panels"][3]["body"]


def test_phase12_verdict_renderer_uses_trusted_content() -> None:
    rendered = build_verdict_screen_renderer_v0_1()

    assert "Governance review passed" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_VERDICT_DISPLAY" in rendered["panels"][0]["body"]
    assert "The proposed governance action satisfies the current review threshold." in rendered["panels"][1]["body"]
    assert "EVIDENCE_SUFFICIENT" in rendered["panels"][2]["body"]
    assert "Verification: VERIFIED" in rendered["panels"][3]["body"]
    assert "Missing Evidence Count: 0" in rendered["panels"][4]["body"]
