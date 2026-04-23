"""
GUS v8 Governance Interface
Explanation Panel Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.screens.explanation.explanation_panel_model import (
    build_explanation_panel_model_v0_1,
)


def build_explanation_panel_renderer_v0_1() -> dict:
    model = build_explanation_panel_model_v0_1()

    reasoning_overview_panel = build_panel_card_v0_1(
        card_id="explanation_reasoning_overview",
        title=model["summary"]["headline"],
        body=(
            model["summary"]["statement"],
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
        ),
        emphasis="high",
    )

    decisive_reasoning_panel = build_panel_card_v0_1(
        card_id="explanation_decisive_reasoning",
        title="Decisive Reasoning",
        body=(
            f"Decisive Rule: {model['decisive_rule']}",
            f"Reason Codes: {', '.join(model['reason_codes'])}",
        ),
        emphasis="standard",
    )

    gate_activity_panel = build_panel_card_v0_1(
        card_id="explanation_gate_activity",
        title="Gate Activity",
        body=model["triggered_gates"],
        emphasis="standard",
    )

    evidence_panel = build_panel_card_v0_1(
        card_id="explanation_evidence_panel",
        title="Evidence and Gaps",
        body=(
            f"Evidence References: {', '.join(model['evidence_references'])}",
            f"Missing Evidence Count: {len(model['missing_evidence'])}",
            f"Verification: {model['trust_state']['verification_state']}",
        ),
        emphasis="standard",
    )

    contract_panel = build_panel_card_v0_1(
        card_id="explanation_contract_panel",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
            f"Authority Binding: {model['trust_state']['authority_binding']}",
        ),
        emphasis="standard",
    )

    return {
        "screen_renderer": "explanation_panel_renderer",
        "version": "v0.1",
        "screen_id": model["screen_id"],
        "layout_role": "reasoning_room",
        "panels": (
            reasoning_overview_panel,
            decisive_reasoning_panel,
            gate_activity_panel,
            evidence_panel,
            contract_panel,
        ),
    }
