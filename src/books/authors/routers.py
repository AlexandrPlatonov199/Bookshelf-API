from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.authors.models import Author
from src.books.authors.shemas import SAuthors
from src.db import get_async_session

router = APIRouter(prefix="/author",
                   tags=["Authors"])


@router.post("")
async def add_author(author: SAuthors, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Author).values(**author.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"message": "200"}