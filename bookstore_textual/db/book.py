import sqlite3
from contextlib import contextmanager
from typing import Generator, Text


@contextmanager
def context_book_db(
    database_url: Text, auto_commit: bool = True
) -> Generator[sqlite3.Cursor, None, None]:
    """Book database context manager.

    Parameters
    ----------
    database_url : Text
        Database url.
    auto_commit : bool, optional
        Commit executions before close connection, by default True

    Yields
    ------
    Generator[sqlite3.Cursor, None, None]
        Database cursor.
    """

    conn = sqlite3.connect(database_url)
    cur = conn.cursor()
    yield cur
    if auto_commit:
        conn.commit()
    conn.close()
