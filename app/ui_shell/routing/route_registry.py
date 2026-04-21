"""
GUS v8 Governance Interface
Route Registry v0.1
"""

from app.screens.case_input.case_input_form_model import (
    build_case_input_form_model_v0_1,
)
from app.screens.explanation.explanation_panel_model import (
    build_explanation_panel_model_v0_1,
)
from app.screens.home_dashboard.dashboard_model import (
    build_home_dashboard_model_v0_1,
)
from app.screens.metrics.metrics_dashboard_model import (
    build_metrics_dashboard_model_v0_1,
)
from app.screens.trust.trust_panel_model import (
    build_trust_panel_model_v0_1,
)
from app.screens.verdict.verdict_screen_model import (
    build_verdict_screen_model_v0_1,
)
from app.ui_shell.routing.runtime_contract import build_runtime_contract_v0_1


ROUTE_BUILDERS = {
    "home_dashboard": build_home_dashboard_model_v0_1,
    "case_input": build_case_input_form_model_v0_1,
    "verdict": build_verdict_screen_model_v0_1,
    "explanation": build_explanation_panel_model_v0_1,
    "trust": build_trust_panel_model_v0_1,
    "metrics": build_metrics_dashboard_model_v0_1,
}


def build_route_registry_v0_1() -> dict:
    contract = build_runtime_contract_v0_1()

    return {
        "registry_name": "governance_route_registry",
        "registry_version": "v0.1",
        "default_route": contract["default_route"],
        "allowed_routes": contract["allowed_routes"],
        "route_builders": ROUTE_BUILDERS,
    }
