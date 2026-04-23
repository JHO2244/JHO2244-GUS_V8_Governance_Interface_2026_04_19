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
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_EXPLANATION_DISPLAY",
        "summary": {
            "headline": "Decision passed due to sufficient transparent evidence",
            "statement": "The submitted governance case satisfied the current explanation threshold.",
        },
        "reason_codes": (
            "EVIDENCE_SUFFICIENT",
            "TRANSPARENCY_CONFIRMED",
            "NO_CONFLICT_TRIGGERED",
        ),
        "decisive_rule": "TRANSPARENT_EVIDENCE_RULE",
        "triggered_gates": (
            "EVIDENCE_GATE_PASS",
            "CONFLICT_GATE_PASS",
            "GOVERNANCE_RULE_PASS",
        ),
        "missing_evidence": (),
        "evidence_references": (
            "vendor_matrix_v2",
            "disclosure_log_checked",
            "approval_trace_complete",
        ),
        "trust_state": {
            "verification_state": "VERIFIED",
            "authority_binding": "BOUND_TO_GIV",
        },
    }
