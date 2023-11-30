from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.categorys.models import Category
from src.books.categorys.shemas import SCategory
from src.db import get_async_session

router = APIRouter(prefix="/category",
                   tags=["Categorys"])


@router.post("")
async def add_category(category: SCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Category).values(**category.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"message": "200"}