import pathlib

from pydantic import AnyUrl, conint, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.common.api.settings import BaseAPISettings
from src.common.database.settings import BaseDatabaseSettings


class UsersSettings(BaseAPISettings, BaseDatabaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow", secrets_dir="/run/secrets")

    db_dsn: AnyUrl = AnyUrl("sqlite+aiosqlite:///users.sqlite3")

    media_dir_path: pathlib.Path = pathlib.Path("/media")
    load_file_chunk_size: PositiveInt = 1024 * 1024  # 1 Mb


def get_settings() -> UsersSettings:
    return UsersSettings()