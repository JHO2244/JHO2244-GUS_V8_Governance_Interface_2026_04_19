"""
GUS v8 Governance Interface
Explanation Panel Model v0.1
"""

from app.contracts.explanation_output.explanation_output_contract import (
    build_explanation_output_contract_v0_1,
)


def build_explanation_panel_model_v0_1() -> dict:
    contract = build_explanation_output_contract_v0_1()

    return {
        "screen_id": "explanation",
        "title": "Governance Explanation",
        "contract_name": contract["contract_name"],
        "contract_version": contract["contract_version"],
        "display_sections": (
            "summary",
            "reason_codes",
            "decisive_rule",
            "triggered_gates",
            "missing_evidence",
            "evidence_references",
            "trust_state",
        ),
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_EXPLANATION_DISPLAY",
    }
