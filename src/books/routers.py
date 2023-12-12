from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from fastapi_versioning import version

from src.books.dao import BookDAO
from src.books.shemas import SBooks
from src.users.dependencies import get_current_user
from src.users.models import User

router = APIRouter(prefix="/books", tags=["Books"])


@version(1)
@router.post("")
async def add_book(book: SBooks, user: User = Depends(get_current_user)):
    await BookDAO.add(**book.model_dump())
    return {"message": "200"}


@router.get("")
@cache(expire=60)
async def get_all_book() -> list[SBooks]:
    return await BookDAO.find_all()


@router.get("{name}")
async def get_book(name: str) -> list[SBooks]:
    return await BookDAO.find_one_or_none(name=name)
