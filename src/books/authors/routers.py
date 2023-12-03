from fastapi import APIRouter

from src.books.authors.dao import AuthorDAO
from src.books.authors.shemas import SAuthors


router = APIRouter(prefix="/author",
                   tags=["Authors"])


@router.post("")
async def add_author(author: SAuthors):
    await AuthorDAO.add(**author.model_dump())
    return {"message": "200"}


@router.get("")
async def get_all_author() -> list[SAuthors]:
    return await AuthorDAO.find_all()
