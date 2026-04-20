"""
GUS v8 Governance Interface
Metrics Output Contract v0.1
"""

CONTRACT_NAME = "governance_metrics_output"
CONTRACT_VERSION = "v0.1"

REQUIRED_FIELDS = (
    "backend_authority",
    "reporting_window",
    "total_cases_reviewed",
)

OPTIONAL_FIELDS = (
    "pass_count",
    "fail_count",
    "insufficient_evidence_count",
    "out_of_scope_count",
    "trend_summary",
    "usage_summary",
    "last_updated",
)

FIELD_DESCRIPTIONS = {
    "backend_authority": "Declared backend authority that produced the metrics payload.",
    "reporting_window": "Structured time window covered by the metrics report.",
    "total_cases_reviewed": "Total number of reviewed cases in the reporting window.",
    "pass_count": "Optional count of PASS verdicts.",
    "fail_count": "Optional count of FAIL verdicts.",
    "insufficient_evidence_count": "Optional count of INSUFFICIENT_EVIDENCE verdicts.",
    "out_of_scope_count": "Optional count of OUT_OF_SCOPE verdicts.",
    "trend_summary": "Optional backend-provided trend summary.",
    "usage_summary": "Optional backend-provided usage summary.",
    "last_updated": "Optional timestamp for the latest metrics refresh.",
}


def build_metrics_output_contract_v0_1() -> dict:
    return {
        "contract_name": CONTRACT_NAME,
        "contract_version": CONTRACT_VERSION,
        "required_fields": REQUIRED_FIELDS,
        "optional_fields": OPTIONAL_FIELDS,
        "field_descriptions": FIELD_DESCRIPTIONS,
    }
