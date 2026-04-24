"""
GUS v8 Governance Interface
Browser Cockpit Boundary v0.2
"""

from flask import Flask, render_template

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
        "next_step": "Return Home or begin the next case workflow.",
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


def build_browser_view_v0_1(route_name: str | None = None) -> dict:
    shell = build_graphical_shell_renderer_v0_1(route_name)
    contract = build_runtime_contract_v0_1()
    active_route = shell["active_route"]

    return {
        "app_name": "GUS Governance Interface",
        "version": "v0.4",
        "authority": "GUS v7 Governance Integrity Vehicle (GIV)",
        "shell": shell,
        "allowed_routes": contract["allowed_routes"],
        "room_guidance": ROOM_GUIDANCE[active_route],
        "display_panels": build_display_panels_v0_1(shell),
    }


@app.route("/")
def home():
    view = build_browser_view_v0_1()
    return render_template("dashboard.html", view=view)


@app.route("/room/<route_name>")
def room(route_name: str):
    view = build_browser_view_v0_1(route_name)
    return render_template("dashboard.html", view=view)


if __name__ == "__main__":
    app.run(debug=False)
