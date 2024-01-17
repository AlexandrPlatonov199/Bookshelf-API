import fastapi

from . import handlers

router = fastapi.APIRouter()

router.add_api_route(path="/{user_id}", methods=["GET"], endpoint=handlers.get_user)
router.add_api_route(path="/create_user", methods=["POST"], endpoint=handlers.create_user)