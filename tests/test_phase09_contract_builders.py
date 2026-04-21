from app.contracts.case_input.case_input_contract import build_case_input_contract_v0_1
from app.contracts.verdict_output.verdict_output_contract import build_verdict_output_contract_v0_1
from app.contracts.explanation_output.explanation_output_contract import build_explanation_output_contract_v0_1
from app.contracts.trust_output.trust_output_contract import build_trust_output_contract_v0_1
from app.contracts.metrics_output.metrics_output_contract import build_metrics_output_contract_v0_1


def test_all_contract_builders_return_dict():
    builders = [
        build_case_input_contract_v0_1,
        build_verdict_output_contract_v0_1,
        build_explanation_output_contract_v0_1,
        build_trust_output_contract_v0_1,
        build_metrics_output_contract_v0_1,
    ]

    for builder in builders:
        result = builder()
        assert isinstance(result, dict)


def test_all_contracts_have_core_keys():
    contracts = [
        build_case_input_contract_v0_1(),
        build_verdict_output_contract_v0_1(),
        build_explanation_output_contract_v0_1(),
        build_trust_output_contract_v0_1(),
        build_metrics_output_contract_v0_1(),
    ]

    for contract in contracts:
        assert "contract_name" in contract
        assert "contract_version" in contract
        assert "required_fields" in contract
        assert "optional_fields" in contract
        assert "field_descriptions" in contract
