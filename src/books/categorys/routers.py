from fastapi import APIRouter

from books.categorys.shemas import SCategory

router = APIRouter(prefix="/category",
                   tags=["Categorys"])


@router.post("")
async def add_category(category: SCategory):
    return {"message": "200"}