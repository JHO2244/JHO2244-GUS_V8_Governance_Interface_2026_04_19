"""
GUS v8 Governance Interface
Branded Report Model v0.1

Deterministic print-to-PDF report payload.
"""

from app.screens.analytics.executive_insight_model import (
    build_executive_insight_model_v0_1,
)


def build_branded_report_model_v0_1() -> dict:
    insight = build_executive_insight_model_v0_1()

    return {
        "model_name": "branded_report_model",
        "version": "v0.1",
        "title": "Executive Governance Report",
        "brand": "GUS v8 Governance Interface",
        "authority": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "Advisory Only",
        "reporting_window": insight["reporting_window"],
        "last_updated": insight["last_updated"],
        "executive_signal": insight["executive_signal"],
        "kpis": insight["kpis"],
        "verdict_bars": insight["verdict_bars"],
        "footer_notes": (
            "v8 is presentation only.",
            "v7 remains authority.",
            "No backend mutation occurred.",
            "Deterministic cockpit payload export.",
        ),
    }
