from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Header, Footer, Static, TextLog


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield Button("Add Book")


class Body(Static):
    def compose(self) -> ComposeResult:
        yield Button("Show Book")


class BookstoreApp(App):
    """A Textual app to manage Books."""

    CSS_PATH = "app.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header(id="header")
        with Container(id="app-grid"):
            yield Sidebar("Book List", id="sidebar")
            yield Body("Book", id="body")
        yield TextLog(max_lines=8, highlight=True, markup=True, id="text_log")
        yield Footer()

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(TextLog)
        text_log.write(event)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""

        self.dark = not self.dark


def run():
    app = BookstoreApp()
    app.run()


if __name__ == "__main__":
    run()
