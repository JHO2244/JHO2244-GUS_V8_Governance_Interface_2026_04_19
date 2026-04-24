from app.browser.flask_app import build_browser_view_v0_1, app


def test_phase17_browser_view_defaults_to_home_dashboard() -> None:
    view = build_browser_view_v0_1()

    assert view["app_name"] == "GUS Governance Interface"
    assert view["version"] == "v0.5"
    assert view["room_guidance"]["title"] == "Executive Home"
    assert "next_step" in view["room_guidance"]
    assert view["authority"] == "GUS v7 Governance Integrity Vehicle (GIV)"
    assert view["shell"]["active_route"] == "home_dashboard"


def test_phase17_browser_view_renders_verdict_room() -> None:
    view = build_browser_view_v0_1("verdict")

    assert view["shell"]["active_route"] == "verdict"
    assert (
        view["shell"]["active_screen_content"]["screen_renderer"]
        == "verdict_screen_renderer"
    )


def test_phase17_flask_home_route_returns_200() -> None:
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"GUS Governance Interface" in response.data
    assert b"home_dashboard" in response.data


def test_phase17_flask_room_route_returns_200() -> None:
    client = app.test_client()

    response = client.get("/room/trust")

    assert response.status_code == 200
    assert b"trust" in response.data
    assert b"trust_panel_renderer" in response.data
