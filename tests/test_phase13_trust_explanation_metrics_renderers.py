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

    assert rendered["panels"][0]["title"] == "Decision passed due to sufficient transparent evidence"
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
    assert rendered["panels"][2]["title"] == "Verdict Distribution"
    assert rendered["panels"][3]["title"] == "Usage and Refresh State"
    assert rendered["panels"][4]["title"] == "Contract Binding"


def test_phase13_trust_renderer_uses_trusted_content() -> None:
    rendered = build_trust_panel_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_TRUST_DISPLAY" in rendered["panels"][0]["body"]
    assert "Verification State: VERIFIED" in rendered["panels"][1]["body"]
    assert "Authority Binding: BOUND_TO_GIV" in rendered["panels"][2]["body"]
    assert "Audit Readiness: AUDIT_READY" in rendered["panels"][3]["body"]
    assert "Contract: governance_trust_output" in rendered["panels"][4]["body"]


def test_phase13_explanation_renderer_uses_trusted_content() -> None:
    rendered = build_explanation_panel_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_EXPLANATION_DISPLAY" in rendered["panels"][0]["body"]
    assert "Decisive Rule: TRANSPARENT_EVIDENCE_RULE" in rendered["panels"][1]["body"]
    assert "EVIDENCE_GATE_PASS" in rendered["panels"][2]["body"]
    assert "Evidence References: vendor_matrix_v2, disclosure_log_checked, approval_trace_complete" in rendered["panels"][3]["body"]
    assert "Authority Binding: BOUND_TO_GIV" in rendered["panels"][4]["body"]


def test_phase13_metrics_renderer_uses_trusted_content() -> None:
    rendered = build_metrics_dashboard_renderer_v0_1()

    assert "Vehicle Authority: GUS v7 Governance Integrity Vehicle (GIV)" in rendered["panels"][0]["body"]
    assert "Display Mode: READ_ONLY_METRICS_DISPLAY" in rendered["panels"][0]["body"]
    assert "Last 30 governance reviews" in rendered["panels"][1]["body"]
    assert "PASS: 18" in rendered["panels"][2]["body"]
    assert "Metrics refreshed from the current governance reporting snapshot." in rendered["panels"][3]["body"]
    assert "Contract: governance_metrics_output" in rendered["panels"][4]["body"]
