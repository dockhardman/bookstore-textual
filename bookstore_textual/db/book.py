import sqlite3
from contextlib import contextmanager
from typing import Generator, Text


@contextmanager
def context_book_db(database_url: Text) -> Generator[sqlite3.Cursor, None, None]:
    conn = sqlite3.connect(database_url)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()
