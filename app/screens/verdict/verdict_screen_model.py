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
        "backend_authority_label": "GUS v7 Governance Integrity Vehicle (GIV)",
        "mode": "READ_ONLY_VERDICT_DISPLAY",
        "verdict_banner": {
            "verdict": "PASS",
            "label": "Governance review passed",
        },
        "summary": {
            "headline": "Transparent vendor selection accepted",
            "statement": "The proposed governance action satisfies the current review threshold.",
        },
        "reason_codes": (
            "EVIDENCE_SUFFICIENT",
            "PROCESS_TRANSPARENT",
            "CONFLICT_CHECK_CLEAR",
        ),
        "missing_evidence": (),
        "trust_state": {
            "verification_state": "VERIFIED",
            "audit_readiness": "AUDIT_READY",
            "authority_binding": "BOUND_TO_GIV",
        },
    }
