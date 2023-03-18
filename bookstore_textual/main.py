from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container, Grid
from textual.css.query import NoMatches
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label, Static, TextLog


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield Button("Add Book")


class Body(Static):
    def compose(self) -> ComposeResult:
        yield Button("Show Book")


class LoginScreen(Screen):
    BINDINGS = [("l", "login", "Login")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Username", id="login_label_username", expand=True),
            Input(),
            Label("Password", id="login_label_password", expand=True),
            Input(),
            id="login_dialog",
        )

    def action_login(self) -> None:
        """An action to login."""

        self.app.pop_screen()


class QuitScreen(Screen):
    BINDINGS = [("q", "request_quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Static("Are you sure you want to quit?", id="quit_question"),
            Button("Quit", variant="error", id="quit_button_quit"),
            Button("Cancel", variant="primary", id="quit_button_cancel"),
            id="quit_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit_button_quit":
            self.app.exit()
        else:
            self.app.pop_screen()

    def action_request_quit(self) -> None:
        """An action to quit the app."""

        self.app.pop_screen()


class BookstoreApp(App):
    """A Textual app to manage Books."""

    CSS_PATH = "app.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("j", "toggle_log", "Toggle log widget"),
        ("l", "login", "Login"),
        ("q", "request_quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header(id="header")
        yield Container(
            Sidebar("Book List", id="sidebar"),
            Body("Book", id="body"),
            id="app-grid",
        )
        yield TextLog(highlight=True, markup=True, id="text_log")
        yield Footer()

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""

        try:
            text_log = self.query_one(TextLog)
            text_log.write(f"Key Event: {event}")
        except NoMatches:
            pass

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
