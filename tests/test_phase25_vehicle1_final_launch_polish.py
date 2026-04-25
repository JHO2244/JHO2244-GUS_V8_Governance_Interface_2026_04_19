"""
Phase 25 — Vehicle 1 Final Launch Polish tests.
"""

from app.browser.flask_app import app


def test_phase25_metrics_page_contains_vehicle1_badge() -> None:
    client = app.test_client()

    html = client.get("/room/metrics").get_data(as_text=True)

    assert "VEHICLE 1 · ADVISORY ONLY · VERIFIED" in html


def test_phase25_metrics_page_contains_role_switcher_class() -> None:
    client = app.test_client()

    html = client.get("/room/metrics").get_data(as_text=True)

    assert "role-switcher" in html


def test_phase25_metrics_page_contains_export_actions_group() -> None:
    client = app.test_client()

    html = client.get("/room/metrics").get_data(as_text=True)

    assert "export-actions" in html
    assert "Download Executive Report" in html
    assert "Open Branded Print Report" in html


def test_phase25_home_dashboard_still_loads() -> None:
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
