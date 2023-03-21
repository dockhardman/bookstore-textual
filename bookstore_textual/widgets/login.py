from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Input, Label


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
