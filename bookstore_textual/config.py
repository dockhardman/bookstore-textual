from contextvars import ContextVar


class Settings(object):
    bookstore_list = ContextVar("bookstore_list", default=("Central Park Bookstore",))


settings = Settings()
