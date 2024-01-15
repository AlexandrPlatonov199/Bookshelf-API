import pathlib

from src.common.database.service import BaseDatabaseService
from src.users.settings import UsersSettings


class UsersDatabaseService(BaseDatabaseService):
    def get_alembic_config_path(self) -> pathlib.Path:
        return pathlib.Path(__file__).parent / "migrations"


def get_service(settings: UsersSettings) -> UsersDatabaseService:
    return UsersDatabaseService(dns=str(settings.db_dns))