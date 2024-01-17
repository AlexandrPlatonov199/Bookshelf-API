import uuid

import fastapi

from src.users.database.models import User
from src.users.database.service import UsersDatabaseService


async def get_path_user(
        request: fastapi.Request,
        user_id: uuid.UUID = fastapi.Path(),
) -> User:
    print(f"dependes.get_path_user request, {request}")
    print(f"dependes.get_path_user user_id, {user_id}")
    database: UsersDatabaseService = request.app.service.database
    print(f"dependes.get_path_user database, {database}")

    async with database.transaction() as session:
        db_user = await database.get_user(session=session, user_id=user_id)
    if db_user is None:
        raise fastapi.HTTPException(status_code=404)

    return db_user