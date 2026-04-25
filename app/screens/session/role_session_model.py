"""
GUS v8 Governance Interface
Role Session Model v0.1

Presentation-only session role model.
No authentication. No permissions enforcement. No backend mutation.
"""

ALLOWED_SESSION_ROLES = ("executive", "analyst", "auditor")
DEFAULT_SESSION_ROLE = "executive"


ROLE_PROFILES = {
    "executive": {
        "label": "Executive",
        "focus": "Decision clarity, risk posture, and export-ready summary.",
        "primary_room": "metrics",
        "recommended_action": "Review Executive Insight and download the report.",
    },
    "analyst": {
        "label": "Analyst",
        "focus": "Payload detail, verdict distribution, and evidence interpretation.",
        "primary_room": "explanation",
        "recommended_action": "Review Explanation and compare Metrics signals.",
    },
    "auditor": {
        "label": "Auditor",
        "focus": "Authority binding, trust state, and export traceability.",
        "primary_room": "trust",
        "recommended_action": "Verify Trust Console before using exported reports.",
    },
}


def normalize_session_role_v0_1(role_name: str | None) -> str:
    if role_name is None:
        return DEFAULT_SESSION_ROLE

    normalized = role_name.strip().lower()

    if normalized not in ALLOWED_SESSION_ROLES:
        return DEFAULT_SESSION_ROLE

    return normalized


def build_role_session_model_v0_1(role_name: str | None = None) -> dict:
    role = normalize_session_role_v0_1(role_name)
    profile = ROLE_PROFILES[role]

    return {
        "model_name": "role_session_model",
        "version": "v0.1",
        "active_role": role,
        "allowed_roles": ALLOWED_SESSION_ROLES,
        "label": profile["label"],
        "focus": profile["focus"],
        "primary_room": profile["primary_room"],
        "recommended_action": profile["recommended_action"],
        "mode": "PRESENTATION_ONLY_ROLE_CONTEXT",
    }
