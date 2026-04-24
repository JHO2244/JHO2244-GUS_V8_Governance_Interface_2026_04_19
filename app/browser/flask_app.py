"""
GUS v8 Governance Interface
Browser Cockpit Boundary v0.1
"""

from flask import Flask, render_template

from app.ui_shell.layout.graphical_shell_renderer import (
    build_graphical_shell_renderer_v0_1,
)
from app.ui_shell.routing.runtime_contract import (
    build_runtime_contract_v0_1,
)

app = Flask(__name__)


def build_browser_view_v0_1(route_name: str | None = None) -> dict:
    shell = build_graphical_shell_renderer_v0_1(route_name)
    contract = build_runtime_contract_v0_1()

    return {
        "app_name": "GUS Governance Interface",
        "version": "v0.3",
        "authority": "GUS v7 Governance Integrity Vehicle (GIV)",
        "shell": shell,
        "allowed_routes": contract["allowed_routes"],
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
