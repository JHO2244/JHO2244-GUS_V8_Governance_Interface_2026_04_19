"""
GUS v8 Governance Interface
Runtime Contract v0.1
"""

ALLOWED_ROUTES = (
    "home_dashboard",
    "case_input",
    "verdict",
    "explanation",
    "trust",
    "metrics",
)

DEFAULT_ROUTE = "home_dashboard"

READ_ONLY_ROUTES = (
    "home_dashboard",
    "verdict",
    "explanation",
    "trust",
    "metrics",
)

INTERACTIVE_ROUTES = (
    "case_input",
)

ROUTE_LABELS = {
    "home_dashboard": "Home",
    "case_input": "Case Input",
    "verdict": "Verdict",
    "explanation": "Explanation",
    "trust": "Trust",
    "metrics": "Metrics",
}


def build_runtime_contract_v0_1() -> dict:
    return {
        "contract_name": "governance_runtime_contract",
        "contract_version": "v0.1",
        "allowed_routes": ALLOWED_ROUTES,
        "default_route": DEFAULT_ROUTE,
        "read_only_routes": READ_ONLY_ROUTES,
        "interactive_routes": INTERACTIVE_ROUTES,
        "route_labels": ROUTE_LABELS,
        "unknown_route_behavior": "FAIL_CLOSED",
        "authority_mode": "ADVISORY_ONLY",
    }
