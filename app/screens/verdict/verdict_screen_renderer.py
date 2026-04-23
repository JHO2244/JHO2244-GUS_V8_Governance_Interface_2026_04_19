"""
GUS v8 Governance Interface
Verdict Screen Renderer v0.1
"""

from app.components.panel_card import build_panel_card_v0_1
from app.screens.verdict.verdict_screen_model import (
    build_verdict_screen_model_v0_1,
)


def build_verdict_screen_renderer_v0_1() -> dict:
    model = build_verdict_screen_model_v0_1()

    verdict_banner_panel = build_panel_card_v0_1(
        card_id="verdict_banner_panel",
        title=model["title"],
        body=(
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
            f"Permitted Verdict States: {', '.join(model['allowed_verdicts'])}",
        ),
        emphasis="high",
    )

    executive_summary_panel = build_panel_card_v0_1(
        card_id="verdict_executive_summary",
        title="Executive Summary",
        body=(
            "Decision-ready verdict display",
            "Built for one-glance governance review",
            "Advisory-only presentation layer",
        ),
        emphasis="standard",
    )

    decision_sections_panel = build_panel_card_v0_1(
        card_id="verdict_decision_sections",
        title="Decision Sections",
        body=model["display_sections"],
        emphasis="standard",
    )

    contract_binding_panel = build_panel_card_v0_1(
        card_id="verdict_contract_binding",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
        ),
        emphasis="standard",
    )

    return {
        "screen_renderer": "verdict_screen_renderer",
        "version": "v0.1",
        "screen_id": model["screen_id"],
        "layout_role": "decision_chamber",
        "panels": (
            verdict_banner_panel,
            executive_summary_panel,
            decision_sections_panel,
            contract_binding_panel,
        ),
    }
