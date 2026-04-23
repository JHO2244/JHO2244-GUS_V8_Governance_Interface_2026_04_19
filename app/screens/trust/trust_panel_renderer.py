"""
GUS v8 Governance Interface
Trust Panel Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.screens.trust.trust_panel_model import (
    build_trust_panel_model_v0_1,
)


def build_trust_panel_renderer_v0_1() -> dict:
    model = build_trust_panel_model_v0_1()

    assurance_overview_panel = build_panel_card_v0_1(
        card_id="trust_assurance_overview",
        title=model["title"],
        body=(
            f"Vehicle Authority: {model['backend_authority']}",
            f"Backend Version: {model['backend_version']}",
            f"Display Mode: {model['mode']}",
        ),
        emphasis="high",
    )

    verification_state_panel = build_panel_card_v0_1(
        card_id="trust_verification_state",
        title="Verification State",
        body=(
            f"Verification State: {model['verification_state']}",
            f"Seal State: {model['seal_state']}",
            f"Last Verified State: {model['last_verified_state']}",
        ),
        emphasis="standard",
    )

    authority_integrity_panel = build_panel_card_v0_1(
        card_id="trust_authority_integrity",
        title="Authority Integrity",
        body=(
            f"Authority Binding: {model['authority_binding']}",
            f"Advisory Mode: {model['advisory_mode']}",
            "Bound to current governance vehicle authority",
        ),
        emphasis="standard",
    )

    audit_readiness_panel = build_panel_card_v0_1(
        card_id="trust_audit_readiness",
        title="Audit Readiness",
        body=(
            f"Audit Readiness: {model['audit_readiness']}",
            "Designed for confidence review",
            "Built for governance-grade assurance",
        ),
        emphasis="standard",
    )

    contract_panel = build_panel_card_v0_1(
        card_id="trust_contract_panel",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
        ),
        emphasis="standard",
    )

    return {
        "screen_renderer": "trust_panel_renderer",
        "version": "v0.1",
        "screen_id": model["screen_id"],
        "layout_role": "integrity_console",
        "panels": (
            assurance_overview_panel,
            verification_state_panel,
            authority_integrity_panel,
            audit_readiness_panel,
            contract_panel,
        ),
    }
