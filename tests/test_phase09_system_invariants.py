from app.screens.verdict.verdict_screen_model import build_verdict_screen_model_v0_1
from app.screens.explanation.explanation_panel_model import build_explanation_panel_model_v0_1
from app.screens.trust.trust_panel_model import build_trust_panel_model_v0_1
from app.screens.metrics.metrics_dashboard_model import build_metrics_dashboard_model_v0_1


def test_backend_authority_labels_are_consistent():
    screens = [
        build_verdict_screen_model_v0_1(),
        build_explanation_panel_model_v0_1(),
        build_trust_panel_model_v0_1(),
        build_metrics_dashboard_model_v0_1(),
    ]

    for screen in screens:
        assert screen["backend_authority_label"] == "GUS v7 Governance Integrity Vehicle (GIV)"


def test_read_only_modes_are_enforced():
    screens = [
        build_verdict_screen_model_v0_1(),
        build_explanation_panel_model_v0_1(),
        build_trust_panel_model_v0_1(),
        build_metrics_dashboard_model_v0_1(),
    ]

    for screen in screens:
        assert screen["mode"].startswith("READ_ONLY_")


def test_screen_ids_are_unique():
    screens = [
        build_verdict_screen_model_v0_1(),
        build_explanation_panel_model_v0_1(),
        build_trust_panel_model_v0_1(),
        build_metrics_dashboard_model_v0_1(),
    ]

    ids = [screen["screen_id"] for screen in screens]

    assert len(ids) == len(set(ids))
