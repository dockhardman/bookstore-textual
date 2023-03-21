from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Static


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
