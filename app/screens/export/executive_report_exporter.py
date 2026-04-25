"""
GUS v8 Governance Interface
Executive Report Exporter v0.1

Presentation-only deterministic export builder.
No backend mutation. No external calls. No invented evidence.
"""

from app.screens.analytics.executive_insight_model import (
    build_executive_insight_model_v0_1,
)


def build_executive_report_text_v0_1() -> str:
    insight = build_executive_insight_model_v0_1()

    lines = [
        "GUS v8 Governance Interface — Executive Report",
        "Authority: GUS v7 Governance Integrity Vehicle (GIV)",
        "Mode: Advisory Only",
        "Export Type: Deterministic Presentation Report",
        f"Reporting Window: {insight['reporting_window']}",
        f"Last Updated: {insight['last_updated']}",
        "",
        "Executive Signal:",
        insight["executive_signal"],
        "",
        "KPI Summary:",
    ]

    for kpi in insight["kpis"]:
        lines.append(f"- {kpi['label']}: {kpi['value']} ({kpi['detail']})")

    lines.extend(
        [
            "",
            "Verdict Distribution:",
        ]
    )

    for item in insight["verdict_bars"]:
        lines.append(
            f"- {item['label']}: {item['count']} cases ({item['percent']}%)"
        )

    lines.extend(
        [
            "",
            "Integrity Notes:",
            "- v8 is a presentation cockpit only.",
            "- v7 remains the governance authority.",
            "- No backend mutation was performed by this export.",
            "- This report reflects the current deterministic cockpit payload.",
        ]
    )

    return "\n".join(lines) + "\n"
