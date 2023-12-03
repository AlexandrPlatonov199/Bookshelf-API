from fastapi import APIRouter

from src.books.dao import BookDAO
from src.books.shemas import SBooks

router = APIRouter(prefix="/books",
                   tags=["Books"])


@router.post("")
async def add_book(book: SBooks):
    await BookDAO.add(**book.model_dump())
    return {"message": "200"}


@router.get("")
async def get_all_book() -> list[SBooks]:
    return await BookDAO.find_all()
