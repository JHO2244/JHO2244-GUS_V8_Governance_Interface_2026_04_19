from app.screens.explanation.explanation_panel_renderer import (
    build_explanation_panel_renderer_v0_1,
)
from app.screens.metrics.metrics_dashboard_renderer import (
    build_metrics_dashboard_renderer_v0_1,
)
from app.screens.trust.trust_panel_renderer import (
    build_trust_panel_renderer_v0_1,
)


def test_phase13_trust_panel_renderer_builds_cleanly() -> None:
    rendered = build_trust_panel_renderer_v0_1()

    assert rendered["screen_renderer"] == "trust_panel_renderer"
    assert rendered["version"] == "v0.1"
    assert rendered["screen_id"] == "trust"
    assert rendered["layout_role"] == "integrity_console"
    assert len(rendered["panels"]) == 5

    assert rendered["panels"][0]["title"] == "Governance Trust Panel"
    assert rendered["panels"][1]["title"] == "Verification State"
    assert rendered["panels"][2]["title"] == "Authority Integrity"
    assert rendered["panels"][3]["title"] == "Audit Readiness"
    assert rendered["panels"][4]["title"] == "Contract Binding"


def test_phase13_explanation_panel_renderer_builds_cleanly() -> None:
    rendered = build_explanation_panel_renderer_v0_1()

    assert rendered["screen_renderer"] == "explanation_panel_renderer"
    assert rendered["version"] == "v0.1"
    assert rendered["screen_id"] == "explanation"
    assert rendered["layout_role"] == "reasoning_room"
    assert len(rendered["panels"]) == 5

    assert rendered["panels"][0]["title"] == "Governance Explanation"
    assert rendered["panels"][1]["title"] == "Decisive Reasoning"
    assert rendered["panels"][2]["title"] == "Gate Activity"
    assert rendered["panels"][3]["title"] == "Evidence and Gaps"
    assert rendered["panels"][4]["title"] == "Contract Binding"


def test_phase13_metrics_dashboard_renderer_builds_cleanly() -> None:
    rendered = build_metrics_dashboard_renderer_v0_1()

    assert rendered["screen_renderer"] == "metrics_dashboard_renderer"
    assert rendered["version"] == "v0.1"
    assert rendered["screen_id"] == "metrics"
    assert rendered["layout_role"] == "telemetry_room"
    assert len(rendered["panels"]) == 5

    assert rendered["panels"][0]["title"] == "Governance Metrics Dashboard"
    assert rendered["panels"][1]["title"] == "Reporting Window"
    assert rendered["panels"][2]["title"] == "Verdict Distribution and Trends"
    assert rendered["panels"][3]["title"] == "Usage and Refresh State"
    assert rendered["panels"][4]["title"] == "Contract Binding"


def test_phase13_trust_renderer_uses_trusted_content() -> None:
    rendered = build_trust_panel_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_TRUST_DISPLAY" in rendered["panels"][0]["body"]
    assert "verification_state" in rendered["panels"][1]["body"]
    assert "backend_authority" in rendered["panels"][2]["body"]
    assert "audit_readiness" in rendered["panels"][3]["body"]
    assert "Contract: governance_trust_output" in rendered["panels"][4]["body"]


def test_phase13_explanation_renderer_uses_trusted_content() -> None:
    rendered = build_explanation_panel_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_EXPLANATION_DISPLAY" in rendered["panels"][0]["body"]
    assert "decisive_rule" in rendered["panels"][1]["body"]
    assert "triggered_gates" in rendered["panels"][2]["body"]
    assert "evidence_references" in rendered["panels"][3]["body"]
    assert "Contract: governance_explanation_output" in rendered["panels"][4]["body"]


def test_phase13_metrics_renderer_uses_trusted_content() -> None:
    rendered = build_metrics_dashboard_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_METRICS_DISPLAY" in rendered["panels"][0]["body"]
    assert "reporting_window" in rendered["panels"][1]["body"]
    assert "verdict_distribution" in rendered["panels"][2]["body"]
    assert "usage_summary" in rendered["panels"][3]["body"]
    assert "Contract: governance_metrics_output" in rendered["panels"][4]["body"]
