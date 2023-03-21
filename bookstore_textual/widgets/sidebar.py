from textual import log
from textual.app import ComposeResult
from textual.widgets import Button, Input, Static
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem

from bookstore_textual.config import settings
from bookstore_textual.utils.log import get_text_log


class BookstoreInput(Input):
    """A Bookstore Input widget."""

    def on_input_submitted(self, submitted: "Input.Submitted") -> None:
        """Handle input submitted event."""

        log.info(f"Input value: {submitted.value}")
        text_log = get_text_log(self)
        text_log.write(f"Submitted {submitted}: {submitted.value}, {submitted.input}")


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield AutoComplete(
            BookstoreInput(placeholder="Search bookstore..."),
            Dropdown(
                items=[
                    DropdownItem(bookstore_name)
                    for bookstore_name in settings.bookstore_list.get()
                ]
            ),
        )
        yield Button("Add Book")
