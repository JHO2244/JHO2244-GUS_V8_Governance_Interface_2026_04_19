"""
GUS v8 Governance Interface
Metrics Dashboard Model v0.1
"""

from app.contracts.metrics_output.metrics_output_contract import (
    build_metrics_output_contract_v0_1,
)


def build_metrics_dashboard_model_v0_1() -> dict:
    contract = build_metrics_output_contract_v0_1()

    return {
        "screen_id": "metrics",
        "title": "Governance Metrics Dashboard",
        "contract_name": contract["contract_name"],
        "contract_version": contract["contract_version"],
        "display_sections": (
            "reporting_window",
            "total_cases_reviewed",
            "verdict_distribution",
            "trend_summary",
            "usage_summary",
            "last_updated",
        ),
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_METRICS_DISPLAY",
    }
