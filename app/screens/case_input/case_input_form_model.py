"""
GUS v8 Governance Interface
Case Input Form Model v0.1
"""

from app.contracts.case_input.case_input_contract import (
    build_case_input_contract_v0_1,
)


def build_case_input_form_model_v0_1() -> dict:
    contract = build_case_input_contract_v0_1()

    fields = {}

    for field_name in contract["required_fields"]:
        fields[field_name] = {
            "value": "",
            "required": True,
            "description": contract["field_descriptions"][field_name],
        }

    for field_name in contract["optional_fields"]:
        fields[field_name] = {
            "value": "",
            "required": False,
            "description": contract["field_descriptions"][field_name],
        }

    return {
        "screen_id": "case_input",
        "title": "Governance Case Input",
        "contract_name": contract["contract_name"],
        "contract_version": contract["contract_version"],
        "fields": fields,
        "submission_mode": "MANUAL_REVIEW_ONLY",
    }
