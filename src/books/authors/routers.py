from fastapi import APIRouter

from books.authors.shemas import SAuthors

router = APIRouter(prefix="/author",
                   tags=["Authors"])


@router.post("")
async def add_author(author: SAuthors):
    return {"message": "200"}