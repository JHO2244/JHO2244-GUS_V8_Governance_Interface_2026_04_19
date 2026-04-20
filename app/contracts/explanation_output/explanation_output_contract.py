"""
GUS v8 Governance Interface
Explanation Output Contract v0.1
"""

CONTRACT_NAME = "governance_explanation_output"
CONTRACT_VERSION = "v0.1"

REQUIRED_FIELDS = (
    "case_id",
    "verdict",
    "summary",
    "reason_codes",
    "backend_authority",
)

OPTIONAL_FIELDS = (
    "decisive_rule",
    "triggered_gates",
    "missing_evidence",
    "evidence_references",
    "trust_state",
)

FIELD_DESCRIPTIONS = {
    "case_id": "Unique case reference associated with the evaluated decision.",
    "verdict": "Canonical backend verdict associated with the explanation payload.",
    "summary": "Short backend-provided explanation summary for human display.",
    "reason_codes": "Deterministic backend reason identifiers tied to the explanation.",
    "backend_authority": "Declared backend authority that produced the explanation payload.",
    "decisive_rule": "Optional decisive backend rule that most directly drove the verdict.",
    "triggered_gates": "Optional structured list of backend gates triggered during evaluation.",
    "missing_evidence": "Optional structured list of missing evidence items affecting the case.",
    "evidence_references": "Optional structured list of backend evidence references used in evaluation.",
    "trust_state": "Optional trust or verification state for the explanation payload.",
}


def build_explanation_output_contract_v0_1() -> dict:
    return {
        "contract_name": CONTRACT_NAME,
        "contract_version": CONTRACT_VERSION,
        "required_fields": REQUIRED_FIELDS,
        "optional_fields": OPTIONAL_FIELDS,
        "field_descriptions": FIELD_DESCRIPTIONS,
    }
