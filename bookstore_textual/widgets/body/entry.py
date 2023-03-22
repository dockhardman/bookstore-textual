from textual.app import ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical


class Body(Static):
    def compose(self) -> ComposeResult:
        yield Vertical(Static(id="book_content"), id="book_content_container")
        yield Button("Show Book")
