from contextvars import ContextVar
from typing import Text


class Settings(object):
    # General Config
    CSS_PATH: Text = "app.css"

    # Application Config
    bookstore_list = ContextVar("bookstore_list", default=("Central Park Bookstore",))

    # Data Config
    bookstore_database_url: Text = "data/bookstore.db"
    book_db_name: Text = "Book"


settings = Settings()
