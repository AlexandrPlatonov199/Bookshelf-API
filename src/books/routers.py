from fastapi import APIRouter, Depends

from books.shemas import SBooks

router = APIRouter(prefix="/books",
                   tags=["Books"])


@router.post("")
async def add_book(book: SBooks):
    return {"message": "200"}