import fastapi
from facet import ServiceMixin

from src.common.api.service import BaseAPIService
from src.books.database.service import BooksDatabaseService
from src.books.settings import BooksSettings

from .router import router


class BooksAPIService(BaseAPIService):
    def __init__(
            self,
            database: BooksDatabaseService,
            port: int = 8000,
            version: str = "0.0.0",
    ):
        self._database = database

        super().__init__(
            title="Books",
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
    def database(self) -> BooksDatabaseService:
        return self._database


def get_service(
        database: BooksDatabaseService,
        settings: BooksSettings,
) -> BooksAPIService:
    return BooksAPIService(
        database=database,
        version="0.0.0",
        port=settings.port,
    )