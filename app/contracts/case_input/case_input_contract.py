"""
GUS v8 Governance Interface
Case Input Contract v0.1
"""

CONTRACT_NAME = "governance_case_input"
CONTRACT_VERSION = "v0.1"

REQUIRED_FIELDS = (
    "case_id",
    "case_title",
    "decision_context",
    "proposed_action",
    "expected_impact",
    "evidence_summary",
    "submitted_by",
)

OPTIONAL_FIELDS = (
    "notes",
    "attachments",
)

FIELD_DESCRIPTIONS = {
    "case_id": "Unique case reference provided by operator or system.",
    "case_title": "Short human-readable title for the governance case.",
    "decision_context": "Context explaining the decision environment.",
    "proposed_action": "The action or decision being evaluated.",
    "expected_impact": "Expected consequences or affected areas.",
    "evidence_summary": "Structured summary of available supporting evidence.",
    "submitted_by": "Submitting human or authorized interface source.",
    "notes": "Optional supporting notes.",
    "attachments": "Optional attachment references only.",
}


def build_case_input_contract_v0_1() -> dict:
    return {
        "contract_name": CONTRACT_NAME,
        "contract_version": CONTRACT_VERSION,
        "required_fields": REQUIRED_FIELDS,
        "optional_fields": OPTIONAL_FIELDS,
        "field_descriptions": FIELD_DESCRIPTIONS,
    }
