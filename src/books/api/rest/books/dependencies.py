import uuid

import fastapi

from src.books.database.models import Book
from src.books.database.service import BooksDatabaseService


async def get_path_book(
        request: fastapi.Request,
        book_id: uuid.UUID = fastapi.Path(),
) -> Book:
    database_service: BooksDatabaseService = request.app.service.database

    async with database_service.transaction() as session:
        db_book = await database_service.get_book(session=session, book_id=book_id)