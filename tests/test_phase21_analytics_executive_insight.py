"""
Phase 21 — Analytics & Executive Insight Layer tests.
"""

from app.browser.flask_app import app, build_browser_view_v0_1
from app.screens.analytics.executive_insight_model import (
    build_executive_insight_model_v0_1,
)


def test_phase21_executive_insight_derives_from_metrics_payload() -> None:
    insight = build_executive_insight_model_v0_1()

    assert insight["model_name"] == "executive_insight_model"
    assert insight["version"] == "v0.1"
    assert insight["source_screen"] == "metrics"

    assert insight["kpis"][0]["label"] == "Cases Reviewed"
    assert insight["kpis"][0]["value"] == "30"

    assert insight["kpis"][1]["label"] == "Pass Rate"
    assert insight["kpis"][1]["value"] == "60%"

    assert insight["kpis"][2]["label"] == "Risk Watch"
    assert insight["kpis"][2]["value"] == "11"

    assert insight["verdict_bars"][0] == {
        "label": "PASS",
        "count": 18,
        "percent": 60,
    }


def test_phase21_executive_insight_only_attaches_to_metrics_route() -> None:
    metrics_view = build_browser_view_v0_1("metrics")
    home_view = build_browser_view_v0_1("home_dashboard")

    assert metrics_view["version"] == "v0.6"
    assert metrics_view["executive_insight"] is not None
    assert metrics_view["executive_insight"]["kpis"][1]["value"] == "60%"

    assert home_view["executive_insight"] is None


def test_phase21_browser_renders_executive_insight_without_leaking_to_home() -> None:
    client = app.test_client()

    metrics_response = client.get("/room/metrics")
    home_response = client.get("/room/home_dashboard")

    metrics_html = metrics_response.get_data(as_text=True)
    home_html = home_response.get_data(as_text=True)

    assert metrics_response.status_code == 200
    assert "Executive Insight Layer" in metrics_html
    assert "Pass Rate" in metrics_html
    assert "60%" in metrics_html
    assert "Risk Watch" in metrics_html

    assert home_response.status_code == 200
    assert "Executive Insight Layer" not in home_html
