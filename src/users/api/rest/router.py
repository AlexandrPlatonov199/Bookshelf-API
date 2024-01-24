import fastapi

from . import dependencies, users

router = fastapi.APIRouter()


router.include_router(users.router, prefix="/users", tags=["Users"])









