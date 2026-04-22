"""
GUS v8 Governance Interface
Panel Card Component v0.1
"""


def build_panel_card_v0_1(
    *,
    card_id: str,
    title: str,
    body: tuple[str, ...],
    emphasis: str = "standard",
) -> dict:
    if not isinstance(card_id, str):
        raise TypeError("card_id must be a str")
    if not isinstance(title, str):
        raise TypeError("title must be a str")
    if not isinstance(body, tuple):
        raise TypeError("body must be a tuple")
    if not isinstance(emphasis, str):
        raise TypeError("emphasis must be a str")

    if card_id.strip() == "":
        raise ValueError("card_id must be non-empty")
    if title.strip() == "":
        raise ValueError("title must be non-empty")
    if len(body) == 0:
        raise ValueError("body must be non-empty")

    for line in body:
        if not isinstance(line, str):
            raise TypeError("body lines must be str")
        if line.strip() == "":
            raise ValueError("body lines must be non-empty")

    return {
        "component": "panel_card",
        "version": "v0.1",
        "card_id": card_id,
        "title": title,
        "body": body,
        "emphasis": emphasis,
    }
