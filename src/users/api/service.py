from typing import Iterable

import fastapi
from facet import ServiceMixin

from src.common.api.service import BaseAPIService
from src.users.database.service import UsersDatabaseService
from src.users.settings import UsersSettings

from .router import router


class UsersAPIService(BaseAPIService):
    def __init__(
            self,
            database: UsersDatabaseService,
            version: str = "0.0.0",
            port: int = 8000,
    ):
        self._database = database

        super().__init__(
            title="Users",
            version=version,
            port=port,
        )

    def setup_app(self, app: fastapi.FastAPI):
        app.include_router(router, prefix="/api")

    @property
    def dependencies(self) -> list[ServiceMixin]:
        return [
            self._database,
        ]

    @property
    def database(self) -> UsersDatabaseService:
        return self._database


def get_service(
        database: UsersDatabaseService,
        settings: UsersSettings,
) -> UsersAPIService:
    return UsersAPIService(
        database=database,
        version="0.0.0",
        port=settings.port,
    )
