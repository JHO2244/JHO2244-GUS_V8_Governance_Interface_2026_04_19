"""
GUS v8 Governance Interface
Screen Router v0.1
"""

from app.ui_shell.routing.route_registry import build_route_registry_v0_1


class UnknownRouteError(Exception):
    """Raised when the runtime shell receives an unknown route."""


def render_route_v0_1(route_name: str | None = None) -> dict:
    registry = build_route_registry_v0_1()

    resolved_route = route_name or registry["default_route"]

    if resolved_route not in registry["allowed_routes"]:
        raise UnknownRouteError(
            f"Unknown runtime route: {resolved_route}"
        )

    builder = registry["route_builders"][resolved_route]

    return {
        "route": resolved_route,
        "screen_content": builder(),
    }
