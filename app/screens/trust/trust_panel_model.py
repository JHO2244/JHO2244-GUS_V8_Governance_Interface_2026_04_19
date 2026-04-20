"""
GUS v8 Governance Interface
Trust Panel Model v0.1
"""

from app.contracts.trust_output.trust_output_contract import (
    build_trust_output_contract_v0_1,
)


def build_trust_panel_model_v0_1() -> dict:
    contract = build_trust_output_contract_v0_1()

    return {
        "screen_id": "trust",
        "title": "Governance Trust Panel",
        "contract_name": contract["contract_name"],
        "contract_version": contract["contract_version"],
        "display_sections": (
            "backend_authority",
            "backend_version",
            "verification_state",
            "seal_state",
            "advisory_mode",
            "audit_readiness",
            "authority_binding",
            "last_verified_state",
        ),
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_TRUST_DISPLAY",
    }
