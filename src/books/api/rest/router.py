import fastapi

from . import dependencies, books

router = fastapi.APIRouter()


router.include_router(books.router, prefix="/books", tags=["Books"])