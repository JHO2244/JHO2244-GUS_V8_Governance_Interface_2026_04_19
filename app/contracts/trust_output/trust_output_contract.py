"""
GUS v8 Governance Interface
Trust Output Contract v0.1
"""

CONTRACT_NAME = "governance_trust_output"
CONTRACT_VERSION = "v0.1"

REQUIRED_FIELDS = (
    "backend_authority",
    "backend_version",
    "verification_state",
    "seal_state",
    "advisory_mode",
)

OPTIONAL_FIELDS = (
    "audit_readiness",
    "authority_binding",
    "last_verified_state",
)

FIELD_DESCRIPTIONS = {
    "backend_authority": "Declared backend authority that produced the governance result.",
    "backend_version": "Declared backend version associated with the current authority.",
    "verification_state": "Structured verification state reported for the backend authority.",
    "seal_state": "Structured seal status reported for the backend authority.",
    "advisory_mode": "Explicit statement that the interface remains advisory-only.",
    "audit_readiness": "Optional indicator showing whether the current result is audit-ready.",
    "authority_binding": "Optional statement describing the active binding between v8 and backend authority.",
    "last_verified_state": "Optional reference to the latest known verification checkpoint.",
}


def build_trust_output_contract_v0_1() -> dict:
    return {
        "contract_name": CONTRACT_NAME,
        "contract_version": CONTRACT_VERSION,
        "required_fields": REQUIRED_FIELDS,
        "optional_fields": OPTIONAL_FIELDS,
        "field_descriptions": FIELD_DESCRIPTIONS,
    }
