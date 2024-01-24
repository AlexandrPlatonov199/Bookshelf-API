import pathlib
import uuid
from typing import Set, Type
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr

from src.common.database.service import BaseDatabaseService
from src.common.utils.empty import Empty
from src.users.database.models import Base, User
from src.users.settings import UsersSettings


class UsersDatabaseService(BaseDatabaseService):
    def get_alembic_config_path(self) -> pathlib.Path:
        return pathlib.Path(__file__).parent / "migrations"

    def get_fixtures_directory_path(self) -> pathlib.Path:
        return pathlib.Path(__file__).parent / "fixtures"

    def get_models(self) -> list[Type[Base]]:
        return [User]

    @asynccontextmanager
    async def transaction(self):
        async with self._sessionmaker() as session:
            async with session.begin():
                yield session

    async def get_user(self,
                       session: AsyncSession,
                       user_id: uuid.UUID | Type[Empty] = Empty,
                       email: str | Type[Empty] = Empty,
                       ) -> User | None:
        filters = []
        if user_id is not Empty:
            filters.append(User.id == user_id)
        if email is not Empty:
            filters.append(User.email == email)

        stmt = select(User).where(*filters)
        result = await session.execute(stmt)
        user = result.unique().scalar_one_or_none()

        return user

    async def create_user(self,
                          session: AsyncSession,
                          email: EmailStr,
                          first_name: str,
                          last_name: str,
    ):
        nested_session = await session.begin_nested()
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,

        )
        session.add(user)
        await nested_session.commit()

        await session.refresh(user)

        return user


def get_service(settings: UsersSettings) -> UsersDatabaseService:
    return UsersDatabaseService(dsn=str(settings.db_dsn))