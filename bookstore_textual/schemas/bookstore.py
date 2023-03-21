import datetime
from typing import Text, TypedDict


class Book(TypedDict):
    """Bookstore data model."""

    id: int
    name: Text
    content: Text
    bookstore: Text
    created_at: datetime.datetime
    updated_at: datetime.datetime


class BookComment(TypedDict):
    """Book comment data model."""

    id: int
    book_id: int
    content: Text
    created_at: datetime.datetime
    updated_at: datetime.datetime
