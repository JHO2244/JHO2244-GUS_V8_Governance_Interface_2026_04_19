"""
GUS v8 Governance Interface
Metrics Dashboard Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.screens.metrics.metrics_dashboard_model import (
    build_metrics_dashboard_model_v0_1,
)


def build_metrics_dashboard_renderer_v0_1() -> dict:
    model = build_metrics_dashboard_model_v0_1()

    telemetry_overview_panel = build_panel_card_v0_1(
        card_id="metrics_telemetry_overview",
        title=model["title"],
        body=(
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
            "Operational telemetry and oversight surface",
        ),
        emphasis="high",
    )

    reporting_window_panel = build_panel_card_v0_1(
        card_id="metrics_reporting_window",
        title="Reporting Window",
        body=(
            "reporting_window",
            "total_cases_reviewed",
            "Structured for executive visibility",
        ),
        emphasis="standard",
    )

    distribution_trends_panel = build_panel_card_v0_1(
        card_id="metrics_distribution_trends",
        title="Verdict Distribution and Trends",
        body=(
            "verdict_distribution",
            "trend_summary",
            "Built for one-glance telemetry review",
        ),
        emphasis="standard",
    )

    usage_refresh_panel = build_panel_card_v0_1(
        card_id="metrics_usage_refresh",
        title="Usage and Refresh State",
        body=(
            "usage_summary",
            "last_updated",
            "Supports operational monitoring",
        ),
        emphasis="standard",
    )

    contract_panel = build_panel_card_v0_1(
        card_id="metrics_contract_panel",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
        ),
        emphasis="standard",
    )

    return {
        "screen_renderer": "metrics_dashboard_renderer",
        "version": "v0.1",
        "screen_id": model["screen_id"],
        "layout_role": "telemetry_room",
        "panels": (
            telemetry_overview_panel,
            reporting_window_panel,
            distribution_trends_panel,
            usage_refresh_panel,
            contract_panel,
        ),
    }
