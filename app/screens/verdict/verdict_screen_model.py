"""
GUS v8 Governance Interface
Verdict Screen Model v0.1
"""

from app.contracts.verdict_output.verdict_output_contract import (
    build_verdict_output_contract_v0_1,
)


def build_verdict_screen_model_v0_1() -> dict:
    contract = build_verdict_output_contract_v0_1()

    return {
        "screen_id": "verdict",
        "title": "Governance Verdict",
        "contract_name": contract["contract_name"],
        "contract_version": contract["contract_version"],
        "allowed_verdicts": contract["allowed_verdicts"],
        "display_sections": (
            "verdict_banner",
            "summary",
            "reason_codes",
            "missing_evidence",
            "trust_state",
        ),
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_VERDICT_DISPLAY",
    }
