import sqlite3
from collections import OrderedDict
from typing import Callable, Dict, List, Optional, Text

from bookstore_textual.config import settings
from bookstore_textual.db import context_book_db
from bookstore_textual.schemas import Book, BookTuple
from contextlib import _GeneratorContextManager


class BookAPI:
    book_tb_name = settings.book_db_name
    book_schema = """(
        ID             INTEGER          PRIMARY KEY,
        Name           VARCHAR(50)      NOT NULL,
        Content        TEXT NOT NULL    NOT NULL,
        Bookstore      CHAR(50),
        CreatedAt      TIMESTAMP,
        UpdatedAt      TIMESTAMP
    );"""

    def __init__(
        self,
        bookstore_database_url: Text = settings.bookstore_database_url,
        database_context: Callable[
            ..., "_GeneratorContextManager[sqlite3.Cursor]"
        ] = context_book_db,
    ) -> None:
        self.bookstore_database_url = bookstore_database_url
        self.db = database_context

    def create_db(self) -> None:
        """Create table."""

        with self.db(self.bookstore_database_url) as cursor:
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.book_tb_name} {self.book_schema}"
            )

    def create_book(self, books: List[Book]) -> None:
        """Create book.

        Parameters
        ----------
        books : List[Book]
            List of books.
        """

        if isinstance(books, Dict):
            books = [books]

        q_marks = ", ".join(["?"] * len(BookTuple._fields))
        query = f"INSERT INTO {self.book_tb_name} VALUES ({q_marks});"

        with self.db(self.bookstore_database_url) as cursor:
            for book in books:
                cursor.execute(query, BookTuple.from_dict(book, with_id=False))

    def get_book(
        self,
        book_id: Optional[int] = None,
        bookstore: Optional[Text] = None,
        limit: int = 20,
        page: int = 1,
    ) -> List[Book]:
        """Get book.

        Parameters
        ----------
        book_id : int
            Book id.
        bookstore : Text
            Bookstore name.
        limit : int
            Limit.
        page : int
            Page.

        Returns
        -------
        List[Book]
            List of books.
        """

        query_where = OrderedDict()
        if book_id is not None:
            query_where["ID"] = book_id
        if bookstore is not None:
            query_where["Bookstore"] = bookstore

        query = (
            f"SELECT * FROM {self.book_tb_name} "
            + "%WHERE$ "
            + f"LIMIT {limit} OFFSET {(page - 1) * limit} "
            + ";"
        )

        if query_where:
            query = query.replace(
                "%WHERE$",
                "WHERE " + " AND ".join([f"{key} = ?" for key in query_where.keys()]),
            )
        else:
            query = query.replace("%WHERE$", "")

        books: List[Book] = []
        with self.db(self.bookstore_database_url) as cursor:
            for row in cursor.execute(query, list(query_where.values())):
                books.append(BookTuple(*row).to_dict())

        return books


book_api = BookAPI()


if __name__ == "__main__":
    from pathlib import Path

    db_url = settings.bookstore_database_url + ".test"
    Path(db_url).unlink(missing_ok=True)

    test_book_api = BookAPI(bookstore_database_url=db_url)
    test_book_api.create_db()
    test_book_api.create_book(
        [
            Book(
                name="Book 1",
                content="Content 1",
                bookstore="Central Park Bookstore",
                created_at="2021-01-01 00:00:00",
                updated_at="2021-01-01 00:00:00",
            ),
            Book(
                name="Book 2",
                content="Content 2",
                bookstore="Central Park Bookstore",
                created_at="2021-01-01 00:00:01",
                updated_at="2021-01-01 00:00:01",
            ),
        ]
    )
    assert len(test_book_api.get_book()) == 2
    assert len(test_book_api.get_book(bookstore="Central Park Bookstore")) == 2
    assert len(test_book_api.get_book(book_id=1)) == 1
    assert len(test_book_api.get_book(bookstore="Unknown Bookstore")) == 0
