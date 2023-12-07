from fastapi import APIRouter

from src.books.categorys.dao import CategoryDAO
from src.books.categorys.shemas import SCategory

router = APIRouter(prefix="/category",
                   tags=["Categorys"])


@router.post("")
async def add_category(category: SCategory):
    await CategoryDAO.add(**category.model_dump())
    return {"message": "200"}


@router.get("")
async def get_all_category() -> list[SCategory]:
    return await CategoryDAO.find_all()