"""
Phase 24 — Branded PDF Export Layer tests.
"""

from app.browser.flask_app import app, build_browser_view_v0_1
from app.screens.export.branded_report_model import (
    build_branded_report_model_v0_1,
)


def test_phase24_branded_report_model_payload() -> None:
    report = build_branded_report_model_v0_1()

    assert report["model_name"] == "branded_report_model"
    assert report["version"] == "v0.1"
    assert report["title"] == "Executive Governance Report"
    assert report["brand"] == "GUS v8 Governance Interface"
    assert len(report["kpis"]) == 4


def test_phase24_browser_view_exposes_branded_report_url() -> None:
    view = build_browser_view_v0_1("metrics")

    assert view["version"] == "v0.8"
    assert view["branded_report_url"] == "/export/branded-report"


def test_phase24_branded_report_route_renders() -> None:
    client = app.test_client()

    response = client.get("/export/branded-report")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Executive Governance Report" in html
    assert "GUS v8 Governance Interface" in html
    assert "Advisory Only" in html


def test_phase24_metrics_room_contains_both_export_actions() -> None:
    client = app.test_client()

    html = client.get("/room/metrics").get_data(as_text=True)

    assert "Download Executive Report" in html
    assert "Open Branded Print Report" in html
