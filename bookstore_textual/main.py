from textual import events, log
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, TextLog

from bookstore_textual.config import settings
from bookstore_textual.widgets import Body, LoginScreen, QuitScreen, Sidebar
from bookstore_textual.utils.log import get_text_log


class BookstoreApp(App):
    """A Textual app to manage Books."""

    CSS_PATH = settings.CSS_PATH
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("j", "toggle_log", "Toggle log widget"),
        ("l", "login", "Login"),
        ("q", "request_quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header(id="header", show_clock=True)
        yield Container(
            Sidebar("Book List", id="sidebar"),
            Body("Book", id="body"),
            id="app-grid",
        )
        yield TextLog(highlight=True, markup=True, id="text_log")
        yield Footer()

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""

        log.info(f"Key Event: {event}")
        text_log = get_text_log(self)
        text_log.write(f"Key Event: {event}")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""

        self.dark = not self.dark

    def action_toggle_log(self) -> None:
        """An action to toggle log widget."""

        text_log = self.query_one(TextLog)
        if text_log.styles.display == "block":
            text_log.styles.display = "none"
        elif text_log.styles.display == "none":
            text_log.styles.display = "block"

    def action_login(self) -> None:
        """An action to login."""

        self.push_screen(LoginScreen())

    def action_request_quit(self) -> None:
        """An action to quit the app."""

        self.push_screen(QuitScreen())


def run():
    app = BookstoreApp()
    app.run()


if __name__ == "__main__":
    run()
