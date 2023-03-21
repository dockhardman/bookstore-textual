import sqlite3
from typing import Callable, List, Text

from bookstore_textual.config import settings
from bookstore_textual.db import context_book_db
from bookstore_textual.schemas import Book
from contextlib import _GeneratorContextManager


class BookAPI(object):

    book_tb_name = settings.book_db_name
    book_schema = """(
        ID             INT PRIMARY KEY  NOT NULL,
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
            ..., _GeneratorContextManager[sqlite3.Cursor]
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


if __name__ == "__main__":
    book_api = BookAPI()
    book_api.create_db()
