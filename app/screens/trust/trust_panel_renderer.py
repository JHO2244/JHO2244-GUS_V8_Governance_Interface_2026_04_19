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
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
            "Integrity assurance and verification surface",
        ),
        emphasis="high",
    )

    verification_state_panel = build_panel_card_v0_1(
        card_id="trust_verification_state",
        title="Verification State",
        body=(
            "verification_state",
            "seal_state",
            "last_verified_state",
        ),
        emphasis="standard",
    )

    authority_integrity_panel = build_panel_card_v0_1(
        card_id="trust_authority_integrity",
        title="Authority Integrity",
        body=(
            "backend_authority",
            "backend_version",
            "authority_binding",
            "advisory_mode",
        ),
        emphasis="standard",
    )

    audit_readiness_panel = build_panel_card_v0_1(
        card_id="trust_audit_readiness",
        title="Audit Readiness",
        body=(
            "audit_readiness",
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
