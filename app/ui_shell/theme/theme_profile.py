"""
GUS v8 Governance Interface
Theme Profile v0.1
"""

from app.ui_shell.theme import design_tokens as t


def get_theme_profile():
    return {
        "theme_name": t.APP_THEME_NAME,
        "colors": {
            "background": t.COLOR_BACKGROUND,
            "surface": t.COLOR_SURFACE,
            "border": t.COLOR_BORDER,
            "text_primary": t.COLOR_TEXT_PRIMARY,
            "text_secondary": t.COLOR_TEXT_SECONDARY,
            "success": t.COLOR_SUCCESS,
            "danger": t.COLOR_DANGER,
            "warning": t.COLOR_WARNING,
            "info": t.COLOR_INFO,
        },
        "fonts": {
            "primary": t.FONT_PRIMARY,
            "mono": t.FONT_MONO,
        },
        "text_sizes": {
            "xl": t.TEXT_XL,
            "lg": t.TEXT_LG,
            "md": t.TEXT_MD,
            "sm": t.TEXT_SM,
            "xs": t.TEXT_XS,
        },
        "spacing": {
            "xxl": t.SPACE_XXL,
            "xl": t.SPACE_XL,
            "lg": t.SPACE_LG,
            "md": t.SPACE_MD,
            "sm": t.SPACE_SM,
            "xs": t.SPACE_XS,
        },
        "radius": {
            "card": t.RADIUS_CARD,
            "button": t.RADIUS_BUTTON,
        },
        "shadow": {
            "card": t.SHADOW_CARD,
        },
        "trust_labels": {
            "verified": t.TRUST_VERIFIED,
            "audit_ready": t.TRUST_AUDIT_READY,
            "backend_bound": t.TRUST_BACKEND_BOUND,
        },
    }
