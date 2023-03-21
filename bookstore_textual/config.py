from contextvars import ContextVar
from typing import Text


class Settings(object):
    # General Config
    CSS_PATH: Text = "app.css"

    bookstore_list = ContextVar("bookstore_list", default=("Central Park Bookstore",))


settings = Settings()
