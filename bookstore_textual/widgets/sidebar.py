from textual.app import ComposeResult
from textual.widgets import Button, Input, Static
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem

from bookstore_textual.config import settings


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield AutoComplete(
            Input(placeholder="Search bookstore..."),
            Dropdown(
                items=[
                    DropdownItem(bookstore_name)
                    for bookstore_name in settings.bookstore_list.get()
                ]
            ),
        )
        yield Button("Add Book")
