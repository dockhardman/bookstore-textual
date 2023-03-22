import datetime
from typing import Dict, NamedTuple, Text, TypedDict


class BookTuple(NamedTuple):
    """Bookstore data model."""

    id: int
    name: Text
    content: Text
    bookstore: Text
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @classmethod
    def from_dict(cls, book: Dict, with_id: bool = True) -> "BookTuple":
        """Create BookTuple from dict."""

        return cls(
            id=book["id"] if with_id else None,
            name=book["name"],
            content=book["content"],
            bookstore=book["bookstore"],
            created_at=book["created_at"],
            updated_at=book["updated_at"],
        )

    def to_dict(self) -> Dict:
        """Convert BookTuple to dict."""

        return Book(
            id=self.id,
            name=self.name,
            content=self.content,
            bookstore=self.bookstore,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


class BookCommentTuple(NamedTuple):
    """Book comment data model."""

    id: int
    book_id: int
    content: Text
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @classmethod
    def from_dict(cls, book_comment: Dict, with_id: bool = True) -> "BookCommentTuple":
        """Create BookCommentTuple from dict."""

        return cls(
            id=book_comment["id"] if with_id else None,
            book_id=book_comment["book_id"],
            content=book_comment["content"],
            created_at=book_comment["created_at"],
            updated_at=book_comment["updated_at"],
        )

    def to_dict(self) -> Dict:
        """Convert BookCommentTuple to dict."""

        return BookComment(
            id=self.id,
            book_id=self.book_id,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


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
