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
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_METRICS_DISPLAY",
        "reporting_window": "Last 30 governance reviews",
        "total_cases_reviewed": 30,
        "verdict_distribution": {
            "PASS": 18,
            "FAIL": 7,
            "INSUFFICIENT_EVIDENCE": 4,
            "OUT_OF_SCOPE": 1,
        },
        "trend_summary": "PASS outcomes remain the dominant result across the current review window.",
        "usage_summary": "Metrics refreshed from the current governance reporting snapshot.",
        "last_updated": "2026-04-23T15:20:00Z",
    }
