"""
GUS v8 Governance Interface
Browser Cockpit Boundary v0.5
"""

from flask import Flask, Response, render_template, request

from app.screens.analytics.executive_insight_model import (
    build_executive_insight_model_v0_1,
)
from app.screens.export.executive_report_exporter import (
    build_executive_report_text_v0_1,
)
from app.screens.session.role_session_model import (
    build_role_session_model_v0_1,
)
from app.ui_shell.layout.graphical_shell_renderer import (
    build_graphical_shell_renderer_v0_1,
)
from app.ui_shell.routing.runtime_contract import (
    build_runtime_contract_v0_1,
)

app = Flask(__name__)


ROOM_GUIDANCE = {
    "home_dashboard": {
        "title": "Executive Home",
        "purpose": "Review overall governance cockpit state and system readiness.",
        "next_step": "Start with Case Input or review the latest Verdict.",
    },
    "case_input": {
        "title": "Case Input",
        "purpose": "Prepare structured governance decision material for review.",
        "next_step": "Enter evidence cleanly, then proceed to Verdict.",
    },
    "verdict": {
        "title": "Verdict Room",
        "purpose": "Inspect the current governance outcome and decision status.",
        "next_step": "Review Explanation to understand why this verdict was reached.",
    },
    "explanation": {
        "title": "Explanation Room",
        "purpose": "Trace the reasoning, decisive rules, and evidence path.",
        "next_step": "Check Trust to confirm authority binding and assurance state.",
    },
    "trust": {
        "title": "Trust Console",
        "purpose": "Verify backend authority, seal state, and audit readiness.",
        "next_step": "Review Metrics for operational pattern visibility.",
    },
    "metrics": {
        "title": "Metrics Room",
        "purpose": "Review governance telemetry and decision distribution signals.",
        "next_step": "Download the Executive Report or begin the next case workflow.",
    },
}


def build_display_panels_v0_1(shell: dict) -> tuple[dict, ...]:
    screen = shell["active_screen_content"]
    panels = screen.get("panels", ())

    display_panels = []

    for panel in panels:
        body = panel.get("body", ())

        if isinstance(body, (tuple, list)):
            body_items = tuple(str(item) for item in body)
        else:
            body_items = (str(body),)

        display_panels.append(
            {
                "title": panel["title"],
                "items": body_items,
                "emphasis": panel.get("emphasis", "standard"),
            }
        )

    return tuple(display_panels)


def build_executive_insight_for_route_v0_1(active_route: str) -> dict | None:
    if active_route != "metrics":
        return None

    return build_executive_insight_model_v0_1()


def build_browser_view_v0_1(
    route_name: str | None = None,
    role_name: str | None = None,
) -> dict:
    shell = build_graphical_shell_renderer_v0_1(route_name)
    contract = build_runtime_contract_v0_1()
    active_route = shell["active_route"]

    return {
        "app_name": "GUS Governance Interface",
        "version": "v0.7",
        "authority": "GUS v7 Governance Integrity Vehicle (GIV)",
        "shell": shell,
        "allowed_routes": contract["allowed_routes"],
        "room_guidance": ROOM_GUIDANCE[active_route],
        "display_panels": build_display_panels_v0_1(shell),
        "executive_insight": build_executive_insight_for_route_v0_1(active_route),
        "executive_report_download_url": "/export/executive-report.txt",
        "role_session": build_role_session_model_v0_1(role_name),
    }


@app.route("/")
def home():
    view = build_browser_view_v0_1(role_name=request.args.get("role"))
    return render_template("dashboard.html", view=view)


@app.route("/room/<route_name>")
def room(route_name: str):
    view = build_browser_view_v0_1(
        route_name,
        role_name=request.args.get("role"),
    )
    return render_template("dashboard.html", view=view)


@app.route("/export/executive-report.txt")
def executive_report_download():
    report_text = build_executive_report_text_v0_1()

    return Response(
        report_text,
        mimetype="text/plain; charset=utf-8",
        headers={
            "Content-Disposition": (
                "attachment; filename=GUS_v8_executive_report.txt"
            )
        },
    )


if __name__ == "__main__":
    app.run(debug=False)
