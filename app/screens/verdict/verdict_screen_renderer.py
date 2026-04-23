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
        title=f"{model['title']} — {model['verdict_banner']['verdict']}",
        body=(
            model["verdict_banner"]["label"],
            f"Vehicle Authority: {model['backend_authority_label']}",
            f"Display Mode: {model['mode']}",
        ),
        emphasis="high",
    )

    executive_summary_panel = build_panel_card_v0_1(
        card_id="verdict_executive_summary",
        title=model["summary"]["headline"],
        body=(
            model["summary"]["statement"],
            f"Allowed Verdict States: {', '.join(model['allowed_verdicts'])}",
        ),
        emphasis="standard",
    )

    reason_codes_panel = build_panel_card_v0_1(
        card_id="verdict_reason_codes",
        title="Reason Codes",
        body=model["reason_codes"],
        emphasis="standard",
    )

    trust_state_panel = build_panel_card_v0_1(
        card_id="verdict_trust_state",
        title="Trust State",
        body=(
            f"Verification: {model['trust_state']['verification_state']}",
            f"Audit Readiness: {model['trust_state']['audit_readiness']}",
            f"Authority Binding: {model['trust_state']['authority_binding']}",
        ),
        emphasis="standard",
    )

    contract_binding_panel = build_panel_card_v0_1(
        card_id="verdict_contract_binding",
        title="Contract Binding",
        body=(
            f"Contract: {model['contract_name']}",
            f"Version: {model['contract_version']}",
            f"Missing Evidence Count: {len(model['missing_evidence'])}",
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
            reason_codes_panel,
            trust_state_panel,
            contract_binding_panel,
        ),
    }
