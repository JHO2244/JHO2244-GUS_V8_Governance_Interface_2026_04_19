"""
GUS v8 Governance Interface
Home Dashboard Model v0.1
"""

from app.ui_shell.theme.theme_profile import get_theme_profile

DASHBOARD_ID = "home_dashboard"
DASHBOARD_TITLE = "Governance Interface"
DASHBOARD_SUBTITLE = "Professional interface for GUS v7 Governance Integrity Vehicle"
BACKEND_AUTHORITY = "GUS v7 Governance Integrity Vehicle (GIV)"

QUICK_ACTIONS = (
    "Open Case Input",
    "View Latest Verdict",
    "Open Trust Panel",
    "Open Metrics",
)

SYSTEM_STATUS = {
    "interface_status": "READY",
    "backend_binding": "BOUND_TO_GIV",
    "verification_state": "VERIFIED",
    "mode": "ADVISORY_ONLY",
}

TRUST_SUMMARY = {
    "verified_label": "Verified",
    "audit_ready_label": "Audit Ready",
    "authority_label": "Bound to GIV",
}


def build_home_dashboard_model_v0_1() -> dict:
    theme = get_theme_profile()

    return {
        "dashboard_id": DASHBOARD_ID,
        "title": DASHBOARD_TITLE,
        "subtitle": DASHBOARD_SUBTITLE,
        "backend_authority": BACKEND_AUTHORITY,
        "quick_actions": QUICK_ACTIONS,
        "system_status": SYSTEM_STATUS,
        "trust_summary": TRUST_SUMMARY,
        "theme_name": theme["theme_name"],
    }
