from pydantic import AnyUrl, conint
from pydantic_settings import BaseSettings




class BooksSettings(BaseSettings):
    port: conint(ge=1, le=65535) = 8000

    db_dsn: AnyUrl = AnyUrl("sqlite+aiosqlite:///books.sqlite3")


def get_settings() -> BooksSettings:
    return BooksSettings()