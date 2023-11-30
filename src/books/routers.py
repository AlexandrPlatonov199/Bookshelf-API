from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.models import Book
from src.books.shemas import SBooks
from src.db import get_async_session

router = APIRouter(prefix="/books",
                   tags=["Books"])


@router.post("")
async def add_book(book: SBooks, session: AsyncSession = Depends(get_async_session)):

    data = book.model_dump()
    print(data)
    stmt = insert(Book).values(**book.model_dump(),)
    await session.execute(stmt)
    await session.commit()
    return {"message": "200"}