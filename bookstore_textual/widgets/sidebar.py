from rich.syntax import Syntax
from textual import log
from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, ListView, ListItem, Static
from bookstore_textual.api.book_api import book_api
from bookstore_textual.config import settings
from bookstore_textual.schemas import Book
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
            book_list_view.append(BookListItem(Label(book["name"]), book=book))


class BookListView(ListView):
    def on_list_view_selected(self, message: "ListView.Selected"):
        selected_item: "BookListItem" = message.item
        book: Book = selected_item.book

        text_log = get_text_log(self)
        text_log.write(f"Select book: {book}")

        app: "App" = get_textual_app(self)
        book_content = app.query_one("#book_content", Static)

        app.sub_title = f"{book['name']} ({book['id']})"
        syntax = Syntax(
            book["content"],
            lexer="python",
            line_numbers=True,
            word_wrap=False,
            indent_guides=True,
            theme="github-dark",
        )
        book_content.update(syntax)


class BookListItem(ListItem):
    def __init__(self, *args, book: Book, **kwargs):
        super().__init__(*args, **kwargs)
        self.book = book


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield BookstoreInput(
            settings.bookstore_list.get()[0],
            placeholder="Search bookstore...",
            id="bookstore_input",
        )
        yield BookListView(id="book_list_view")
        yield Button("Add Book")
