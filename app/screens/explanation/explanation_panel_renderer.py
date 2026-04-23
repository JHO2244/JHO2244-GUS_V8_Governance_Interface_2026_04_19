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
        title=model["title"],
        body=(
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
            "Transparent reasoning and evidence surface",
        ),
        emphasis="high",
    )

    decisive_reasoning_panel = build_panel_card_v0_1(
        card_id="explanation_decisive_reasoning",
        title="Decisive Reasoning",
        body=(
            "summary",
            "reason_codes",
            "decisive_rule",
        ),
        emphasis="standard",
    )

    gate_activity_panel = build_panel_card_v0_1(
        card_id="explanation_gate_activity",
        title="Gate Activity",
        body=(
            "triggered_gates",
            "trust_state",
            "Built for transparent governance review",
        ),
        emphasis="standard",
    )

    evidence_panel = build_panel_card_v0_1(
        card_id="explanation_evidence_panel",
        title="Evidence and Gaps",
        body=(
            "evidence_references",
            "missing_evidence",
            "Structured for human-readable analysis",
        ),
        emphasis="standard",
    )

    contract_panel = build_panel_card_v0_1(
        card_id="explanation_contract_panel",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
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
