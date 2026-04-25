"""
Phase 22 — Report Export Layer tests.
"""

from app.browser.flask_app import app, build_browser_view_v0_1
from app.screens.export.executive_report_exporter import (
    build_executive_report_text_v0_1,
)


def test_phase22_executive_report_text_is_deterministic_and_advisory() -> None:
    report = build_executive_report_text_v0_1()

    assert report.startswith("GUS v8 Governance Interface — Executive Report")
    assert "Authority: GUS v7 Governance Integrity Vehicle (GIV)" in report
    assert "Mode: Advisory Only" in report
    assert "Pass Rate: 60%" in report
    assert "Risk Watch: 11" in report
    assert "No backend mutation was performed by this export." in report


def test_phase22_browser_view_exposes_report_download_url() -> None:
    view = build_browser_view_v0_1("metrics")

    assert view["version"] == "v0.6"
    assert view["executive_report_download_url"] == "/export/executive-report.txt"


def test_phase22_metrics_room_shows_download_action_without_home_leak() -> None:
    client = app.test_client()

    metrics_html = client.get("/room/metrics").get_data(as_text=True)
    home_html = client.get("/room/home_dashboard").get_data(as_text=True)

    assert "Download Executive Report" in metrics_html
    assert "/export/executive-report.txt" in metrics_html
    assert "Download Executive Report" not in home_html


def test_phase22_report_download_route_returns_text_attachment() -> None:
    client = app.test_client()

    response = client.get("/export/executive-report.txt")
    text = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response.mimetype == "text/plain"
    assert "attachment;" in response.headers["Content-Disposition"]
    assert "GUS_v8_executive_report.txt" in response.headers["Content-Disposition"]
    assert "GUS v8 Governance Interface — Executive Report" in text
