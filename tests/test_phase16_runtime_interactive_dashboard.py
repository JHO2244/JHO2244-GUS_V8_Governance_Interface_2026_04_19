from app.ui_shell.runtime.runtime_commands import (
    build_runtime_command_help_v0_1,
    normalize_runtime_command_v0_1,
)
from app.ui_shell.runtime.runtime_controller import (
    handle_runtime_command_v0_1,
)
from app.ui_shell.runtime.runtime_session import (
    build_runtime_session_v0_1,
)


def test_phase16_runtime_session_defaults_to_home() -> None:
    session = build_runtime_session_v0_1()

    assert session["active_route"] == "home_dashboard"
    assert session["authority_mode"] == "ADVISORY_ONLY"
    assert session["persistence"] == "NONE"


def test_phase16_runtime_command_normalization() -> None:
    assert normalize_runtime_command_v0_1("  HOME ") == "home"


def test_phase16_runtime_help_command() -> None:
    result = handle_runtime_command_v0_1("help")

    assert result["result"] == "HELP"
    assert "quit" in result["payload"]["available_commands"]


def test_phase16_runtime_route_change_to_verdict() -> None:
    result = handle_runtime_command_v0_1("verdict")

    assert result["result"] == "ROUTE_CHANGED"
    assert result["session"]["active_route"] == "verdict"
    assert (
        result["payload"]["active_screen_content"]["screen_id"]
        == "verdict"
    )


def test_phase16_runtime_unknown_command_fails_closed() -> None:
    result = handle_runtime_command_v0_1("hack")

    assert result["result"] == "UNKNOWN_COMMAND"
    assert result["payload"]["behavior"] == "FAIL_CLOSED"


def test_phase16_runtime_quit_command() -> None:
    result = handle_runtime_command_v0_1("quit", "trust")

    assert result["result"] == "QUIT"
    assert result["session"]["active_route"] == "trust"


def test_phase16_runtime_help_builder_locked() -> None:
    help_state = build_runtime_command_help_v0_1()

    assert help_state["authority_mode"] == "ADVISORY_ONLY"
    assert help_state["unknown_command_behavior"] == "FAIL_CLOSED"
