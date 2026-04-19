"""
GUS v8 Governance Interface
Verdict Output Contract v0.1
"""

CONTRACT_NAME = "governance_verdict_output"
CONTRACT_VERSION = "v0.1"

ALLOWED_VERDICTS = (
    "PASS",
    "FAIL",
    "INSUFFICIENT_EVIDENCE",
    "OUT_OF_SCOPE",
)

REQUIRED_FIELDS = (
    "case_id",
    "verdict",
    "summary",
    "reason_codes",
    "backend_authority",
)

OPTIONAL_FIELDS = (
    "missing_evidence",
    "trust_state",
)

FIELD_DESCRIPTIONS = {
    "case_id": "Unique case reference associated with the evaluated decision.",
    "verdict": "Canonical backend verdict returned by GIV.",
    "summary": "Short human-readable verdict summary.",
    "reason_codes": "Deterministic backend reason identifiers.",
    "backend_authority": "Declared backend authority that produced the verdict.",
    "missing_evidence": "Optional structured list of missing evidence items.",
    "trust_state": "Optional trust or verification state for the verdict payload.",
}


def build_verdict_output_contract_v0_1() -> dict:
    return {
        "contract_name": CONTRACT_NAME,
        "contract_version": CONTRACT_VERSION,
        "allowed_verdicts": ALLOWED_VERDICTS,
        "required_fields": REQUIRED_FIELDS,
        "optional_fields": OPTIONAL_FIELDS,
        "field_descriptions": FIELD_DESCRIPTIONS,
    }
