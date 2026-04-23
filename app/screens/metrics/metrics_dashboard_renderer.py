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
            f"Total Cases Reviewed: {model['total_cases_reviewed']}",
        ),
        emphasis="high",
    )

    reporting_window_panel = build_panel_card_v0_1(
        card_id="metrics_reporting_window",
        title="Reporting Window",
        body=(
            model["reporting_window"],
            model["trend_summary"],
        ),
        emphasis="standard",
    )

    distribution_trends_panel = build_panel_card_v0_1(
        card_id="metrics_distribution_trends",
        title="Verdict Distribution",
        body=(
            f"PASS: {model['verdict_distribution']['PASS']}",
            f"FAIL: {model['verdict_distribution']['FAIL']}",
            f"INSUFFICIENT_EVIDENCE: {model['verdict_distribution']['INSUFFICIENT_EVIDENCE']}",
            f"OUT_OF_SCOPE: {model['verdict_distribution']['OUT_OF_SCOPE']}",
        ),
        emphasis="standard",
    )

    usage_refresh_panel = build_panel_card_v0_1(
        card_id="metrics_usage_refresh",
        title="Usage and Refresh State",
        body=(
            model["usage_summary"],
            f"Last Updated: {model['last_updated']}",
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
