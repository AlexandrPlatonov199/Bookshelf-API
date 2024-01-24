import os
import pathlib
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.users.database.models import User
from src.users.database.service import UsersDatabaseService


def test_get_alembic_config_path(database_service: UsersDatabaseService):
    expected_path = (
            pathlib.Path(os.curdir).absolute() / "src" / "users" / "database" / "migrations"
    )

    path = database_service.get_alembic_config_path()

    assert isinstance(path, pathlib.Path)
    assert path == expected_path


@pytest.mark.asyncio
async def test_get_user(database_service: UsersDatabaseService):
    session = MagicMock()
    result = MagicMock()
    user_id = uuid.uuid4()
    email = "test@gmail.com"

    result.unique().scalar_one_or_none.return_value = User(id=user_id, email=email)
    session.execute = AsyncMock()
    session.execute.return_value = result

    user = await database_service.get_user(
        session=session,
        email=email,
    )

    assert user is not None
    assert user.email == email


@pytest.mark.asyncio
async def test_create_user(database_service: UsersDatabaseService):
    session = AsyncMock()
    email = "test@gmail.com"
    first_name = "Test"
    last_name = "Testovich"

    user = await database_service.create_user(
        session=session,
        email=email,
        first_name=first_name,
        last_name=last_name
    )

    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name
