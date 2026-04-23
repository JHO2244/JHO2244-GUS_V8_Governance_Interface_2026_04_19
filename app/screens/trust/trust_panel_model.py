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
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_TRUST_DISPLAY",
        "backend_authority": "GUS v7 Governance Integrity Vehicle (GIV)",
        "backend_version": "v0.4",
        "verification_state": "VERIFIED",
        "seal_state": "SEALED",
        "advisory_mode": "ADVISORY_ONLY",
        "audit_readiness": "AUDIT_READY",
        "authority_binding": "BOUND_TO_GIV",
        "last_verified_state": "HEAD_VERIFIED",
    }
