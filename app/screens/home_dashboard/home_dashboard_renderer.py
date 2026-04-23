"""
GUS v8 Governance Interface
Home Dashboard Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.screens.home_dashboard.dashboard_model import (
    build_home_dashboard_model_v0_1,
)


def build_home_dashboard_renderer_v0_1() -> dict:
    model = build_home_dashboard_model_v0_1()

    executive_overview_panel = build_panel_card_v0_1(
        card_id="home_executive_overview",
        title=model["title"],
        body=(
            model["subtitle"],
            f"Vehicle Authority: {model['backend_authority']}",
            f"Interface Theme: {model['theme_name']}",
        ),
        emphasis="high",
    )

    quick_actions_panel = build_panel_card_v0_1(
        card_id="home_quick_actions",
        title="Quick Actions",
        body=model["quick_actions"],
        emphasis="standard",
    )

    system_trust_panel = build_panel_card_v0_1(
        card_id="home_system_trust",
        title="System Trust",
        body=(
            f"Interface Status: {model['system_status']['interface_status']}",
            f"Backend Binding: {model['system_status']['backend_binding']}",
            f"Verification State: {model['system_status']['verification_state']}",
            f"Operating Mode: {model['system_status']['mode']}",
        ),
        emphasis="standard",
    )

    operational_summary_panel = build_panel_card_v0_1(
        card_id="home_operational_summary",
        title="Operational Summary",
        body=(
            model["trust_summary"]["verified_label"],
            model["trust_summary"]["audit_ready_label"],
            model["trust_summary"]["authority_label"],
        ),
        emphasis="standard",
    )

    return {
        "screen_renderer": "home_dashboard_renderer",
        "version": "v0.1",
        "screen_id": model["dashboard_id"],
        "layout_role": "executive_command_center",
        "panels": (
            executive_overview_panel,
            system_trust_panel,
            quick_actions_panel,
            operational_summary_panel,
        ),
    }
