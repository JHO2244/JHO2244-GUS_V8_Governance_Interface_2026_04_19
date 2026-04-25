"""
Phase 23 — Role & Session Layer tests.
"""

from app.browser.flask_app import app, build_browser_view_v0_1
from app.screens.session.role_session_model import (
    build_role_session_model_v0_1,
    normalize_session_role_v0_1,
)


def test_phase23_role_session_defaults_to_executive() -> None:
    session = build_role_session_model_v0_1()

    assert session["model_name"] == "role_session_model"
    assert session["version"] == "v0.1"
    assert session["active_role"] == "executive"
    assert session["label"] == "Executive"
    assert session["mode"] == "PRESENTATION_ONLY_ROLE_CONTEXT"


def test_phase23_role_session_accepts_known_roles_and_normalizes_invalid() -> None:
    assert normalize_session_role_v0_1("executive") == "executive"
    assert normalize_session_role_v0_1("analyst") == "analyst"
    assert normalize_session_role_v0_1("auditor") == "auditor"
    assert normalize_session_role_v0_1("INVALID") == "executive"
    assert normalize_session_role_v0_1(None) == "executive"


def test_phase23_browser_view_includes_role_session_context() -> None:
    view = build_browser_view_v0_1("metrics", role_name="auditor")

    assert view["version"] == "v0.8"
    assert view["role_session"]["active_role"] == "auditor"
    assert view["role_session"]["label"] == "Auditor"
    assert view["role_session"]["mode"] == "PRESENTATION_ONLY_ROLE_CONTEXT"


def test_phase23_role_query_parameter_renders_without_authority_change() -> None:
    client = app.test_client()

    response = client.get("/room/metrics?role=analyst")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Active Role: Analyst" in html
    assert "Role:</strong> Analyst" in html
    assert "Authority: GUS v7 Governance Integrity Vehicle (GIV)" in html
