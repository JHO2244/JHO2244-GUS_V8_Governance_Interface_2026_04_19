"""
GUS v8 Governance Interface
Executive Insight Model v0.1

Presentation-only analytics derived from the existing metrics screen model.
No backend mutation. No invented data.
"""

from app.screens.metrics.metrics_dashboard_model import (
    build_metrics_dashboard_model_v0_1,
)


def _percent(part: int, total: int) -> int:
    if total <= 0:
        return 0
    return round((part / total) * 100)


def build_executive_insight_model_v0_1() -> dict:
    metrics = build_metrics_dashboard_model_v0_1()
    distribution = metrics["verdict_distribution"]
    total_cases = metrics["total_cases_reviewed"]

    pass_count = distribution["PASS"]
    fail_count = distribution["FAIL"]
    insufficient_count = distribution["INSUFFICIENT_EVIDENCE"]
    out_of_scope_count = distribution["OUT_OF_SCOPE"]

    risk_watch_count = fail_count + insufficient_count

    return {
        "model_name": "executive_insight_model",
        "version": "v0.1",
        "source_screen": metrics["screen_id"],
        "reporting_window": metrics["reporting_window"],
        "last_updated": metrics["last_updated"],
        "kpis": (
            {
                "label": "Cases Reviewed",
                "value": str(total_cases),
                "detail": metrics["reporting_window"],
            },
            {
                "label": "Pass Rate",
                "value": f"{_percent(pass_count, total_cases)}%",
                "detail": f"{pass_count} PASS outcomes",
            },
            {
                "label": "Risk Watch",
                "value": str(risk_watch_count),
                "detail": "FAIL + INSUFFICIENT_EVIDENCE outcomes",
            },
            {
                "label": "Trust Signal",
                "value": "Read-only",
                "detail": metrics["backend_authority_label"],
            },
        ),
        "verdict_bars": (
            {
                "label": "PASS",
                "count": pass_count,
                "percent": _percent(pass_count, total_cases),
            },
            {
                "label": "FAIL",
                "count": fail_count,
                "percent": _percent(fail_count, total_cases),
            },
            {
                "label": "INSUFFICIENT_EVIDENCE",
                "count": insufficient_count,
                "percent": _percent(insufficient_count, total_cases),
            },
            {
                "label": "OUT_OF_SCOPE",
                "count": out_of_scope_count,
                "percent": _percent(out_of_scope_count, total_cases),
            },
        ),
        "executive_signal": (
            "PASS outcomes remain dominant while FAIL and "
            "INSUFFICIENT_EVIDENCE form the active review watchlist."
        ),
    }
