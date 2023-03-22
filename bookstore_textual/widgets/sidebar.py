from textual import log
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem
from textual.app import ComposeResult
from textual.widgets import Button, Input, Label, ListView, ListItem, Static

from bookstore_textual.api.book_api import book_api
from bookstore_textual.config import settings
from bookstore_textual.utils.textual import get_text_log, get_textual_app


class BookstoreInput(Input):
    """A Bookstore Input widget."""

    def on_input_submitted(self, submitted: "Input.Submitted") -> None:
        """Handle input submitted event."""

        bookstore_name = submitted.value.strip()
        get_textual_app(self).current_bookstore = bookstore_name

        text_log = get_text_log(self)
        text_log.write(f"Submitted bookstore: {bookstore_name}")
        log.info(f"Input value: {submitted.value}")

        # Search books from bookstore
        books = book_api.get_book(bookstore=submitted.value.strip())
        get_textual_app(self).current_books = books
        text_log.write(f"Get {len(books)} books: {books[:3]}")
        log.info(f"Get books: {books}")

        # Update book list view
        for node in self.ancestors:
            if node.id == "sidebar":
                book_list_view: "ListView" = node.query_one("#book_list_view")
                break
        book_list_view.clear()
        for book in books:
            book_list_view.append(ListItem(Label(book["name"])))


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield AutoComplete(
            BookstoreInput(placeholder="Search bookstore...", id="bookstore_input"),
            Dropdown(
                items=[
                    DropdownItem(bookstore_name)
                    for bookstore_name in settings.bookstore_list.get()
                ]
            ),
        )
        yield ListView(id="book_list_view")
        yield Button("Add Book")
