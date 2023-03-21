from textual.app import ComposeResult
from textual.widgets import Button, Static


class Body(Static):
    def compose(self) -> ComposeResult:
        yield Button("Show Book")
