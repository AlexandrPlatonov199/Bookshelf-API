import pathlib
import uuid


import fastapi
from fastapi.responses import FileResponse


from src.users.api.rest.schemas import UserResponse
from src.users.database.models import User
from src.users.database.service import UsersDatabaseService

from .dependencies import get_path_user
from .schemas import UserUpdateRequest, UserCreateRequest


async def get_user(
        user: User = fastapi.Depends(get_path_user),
) -> UserResponse:
    print(f"handlers.getuser(), {user}")
    return UserResponse.from_db_model(user)

async def create_user(
        request: fastapi.Request,
        data: UserCreateRequest = fastapi.Body(embed=False),
):
    database: UsersDatabaseService = request.app.service.database

    async with database.transaction() as session:
        user_db = await database.create_user(
            session=session,
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name,
        )
    return UserResponse.model_validate(user_db)
