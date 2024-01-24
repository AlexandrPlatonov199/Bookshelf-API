import uuid

import fastapi

from .dependencies import get_path_book
from src.books.database.models import Book
from src.books.api.rest.schemas import BookResponse


async def get_book(
        book: Book = fastapi.Depends(get_path_book)
) -> BookResponse:
    return BookResponse.model_validate(book)

