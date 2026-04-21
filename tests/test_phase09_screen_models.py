from app.screens.home_dashboard.dashboard_model import build_home_dashboard_model_v0_1
from app.screens.case_input.case_input_form_model import build_case_input_form_model_v0_1
from app.screens.verdict.verdict_screen_model import build_verdict_screen_model_v0_1
from app.screens.explanation.explanation_panel_model import build_explanation_panel_model_v0_1
from app.screens.trust.trust_panel_model import build_trust_panel_model_v0_1
from app.screens.metrics.metrics_dashboard_model import build_metrics_dashboard_model_v0_1


def test_all_screen_builders_return_dict():
    builders = [
        build_home_dashboard_model_v0_1,
        build_case_input_form_model_v0_1,
        build_verdict_screen_model_v0_1,
        build_explanation_panel_model_v0_1,
        build_trust_panel_model_v0_1,
        build_metrics_dashboard_model_v0_1,
    ]

    for builder in builders:
        result = builder()
        assert isinstance(result, dict)


def test_operational_screens_have_required_core_fields():
    screens = [
        build_case_input_form_model_v0_1(),
        build_verdict_screen_model_v0_1(),
        build_explanation_panel_model_v0_1(),
        build_trust_panel_model_v0_1(),
        build_metrics_dashboard_model_v0_1(),
    ]

    for screen in screens:
        assert "screen_id" in screen
        assert "title" in screen
        assert "contract_name" in screen
        assert "contract_version" in screen


def test_home_dashboard_has_required_core_fields():
    dashboard = build_home_dashboard_model_v0_1()

    assert dashboard["dashboard_id"] == "home_dashboard"
    assert dashboard["title"] == "Governance Interface"
    assert dashboard["backend_authority"] == "GUS v7 Governance Integrity Vehicle (GIV)"
    assert dashboard["theme_name"] == "Governance Calm"
