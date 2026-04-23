from app.screens.explanation.explanation_panel_renderer import (
    build_explanation_panel_renderer_v0_1,
)
from app.screens.metrics.metrics_dashboard_renderer import (
    build_metrics_dashboard_renderer_v0_1,
)
from app.screens.trust.trust_panel_renderer import (
    build_trust_panel_renderer_v0_1,
)
from app.screens.verdict.verdict_screen_renderer import (
    build_verdict_screen_renderer_v0_1,
)


def test_phase15_verdict_renderer_uses_real_payload_content() -> None:
    rendered = build_verdict_screen_renderer_v0_1()

    assert rendered["screen_renderer"] == "verdict_screen_renderer"
    assert rendered["panels"][0]["title"] == "Governance Verdict — PASS"
    assert "Governance review passed" in rendered["panels"][0]["body"]
    assert "Transparent vendor selection accepted" == rendered["panels"][1]["title"]
    assert "EVIDENCE_SUFFICIENT" in rendered["panels"][2]["body"]
    assert "Verification: VERIFIED" in rendered["panels"][3]["body"]
    assert "Missing Evidence Count: 0" in rendered["panels"][4]["body"]


def test_phase15_trust_renderer_uses_real_payload_content() -> None:
    rendered = build_trust_panel_renderer_v0_1()

    assert rendered["screen_renderer"] == "trust_panel_renderer"
    assert "Backend Version: v0.4" in rendered["panels"][0]["body"]
    assert "Verification State: VERIFIED" in rendered["panels"][1]["body"]
    assert "Seal State: SEALED" in rendered["panels"][1]["body"]
    assert "Authority Binding: BOUND_TO_GIV" in rendered["panels"][2]["body"]
    assert "Audit Readiness: AUDIT_READY" in rendered["panels"][3]["body"]


def test_phase15_explanation_renderer_uses_real_payload_content() -> None:
    rendered = build_explanation_panel_renderer_v0_1()

    assert rendered["screen_renderer"] == "explanation_panel_renderer"
    assert rendered["panels"][0]["title"] == "Decision passed due to sufficient transparent evidence"
    assert "Decisive Rule: TRANSPARENT_EVIDENCE_RULE" in rendered["panels"][1]["body"]
    assert "EVIDENCE_GATE_PASS" in rendered["panels"][2]["body"]
    assert "Missing Evidence Count: 0" in rendered["panels"][3]["body"]
    assert "Authority Binding: BOUND_TO_GIV" in rendered["panels"][4]["body"]


def test_phase15_metrics_renderer_uses_real_payload_content() -> None:
    rendered = build_metrics_dashboard_renderer_v0_1()

    assert rendered["screen_renderer"] == "metrics_dashboard_renderer"
    assert "Total Cases Reviewed: 30" in rendered["panels"][0]["body"]
    assert "Last 30 governance reviews" in rendered["panels"][1]["body"]
    assert "PASS: 18" in rendered["panels"][2]["body"]
    assert "FAIL: 7" in rendered["panels"][2]["body"]
    assert "Last Updated: 2026-04-23T15:20:00Z" in rendered["panels"][3]["body"]
