from typing import Optional, TYPE_CHECKING, Text

from textual.widgets import TextLog

if TYPE_CHECKING:
    from textual.app import App
    from textual.dom import DOMNode


def get_text_log(node: "DOMNode", id: Optional[Text] = None) -> "TextLog":
    """Get main application TextLog."""

    app: App = node.ancestors_with_self[-1]

    if id:
        text_log = app.query_one(f"#{id}")
    else:
        text_log = app.query_one(TextLog)

    return text_log
