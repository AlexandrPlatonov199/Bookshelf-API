import fastapi
from . import handlers

router = fastapi.APIRouter()

router.add_api_route(path="/{book_id}", methods=["GET"], endpoint=handlers.get_book)