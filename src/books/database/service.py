import pathlib
import uuid
from contextlib import asynccontextmanager
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.database.models import Book
from src.books.settings import BooksSettings
from src.common.database.service import BaseDatabaseService
from src.common.utils.empty import Empty


class BooksDatabaseService(BaseDatabaseService):
    def get_alembic_config_path(self) -> pathlib.Path:
        return pathlib.Path(__file__).parent / "migrations"

    @asynccontextmanager
    async def transaction(self):
        async with self._sessionmaker() as session:
            async with session.begin():
                yield session

    async def get_book(self,
                       session: AsyncSession,
                       book_id: uuid.UUID | Type[Empty] = Empty
                       ) -> Book | None:
        filters = []
        if book_id is not Empty:
            filters.append(Book.id == book_id)

        stmt = select(Book).where(*filters)
        result = await session.execute(stmt)
        book = result.unique().scalar_one_or_none()

        return book


def get_service(settings: BooksSettings) -> BooksDatabaseService:
    return BooksDatabaseService(dsn=str(settings.db_dsn))