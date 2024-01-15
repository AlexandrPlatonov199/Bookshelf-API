import pathlib

from alembic import command as alembic_command
from alembic.config import Config as AlembicConfig
from facet import ServiceMixin
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class BaseDatabaseService(ServiceMixin):
    def __init__(self, dns: str):
        self._dns = dns
        self._engine = create_async_engine(self._dns)
        self._sessionmaker = async_sessionmaker(self._engine, expire_on_commit=False)

    def get_alembic_config_path(self) -> pathlib.Path:
        raise NotImplementedError

    def get_alembic_config(self) -> AlembicConfig:
        migrations_path = self.get_alembic_config_path()

        config = AlembicConfig()
        config.set_main_option("script_location", str(migrations_path))
        config.set_main_option("sqlalchemy.url", self._dns)

        return config

    def migrate(self):
        alembic_command.upgrade(self.get_alembic_config(), "head")

    def rollback(self, revision: str | None = None):
        revision = revision or "-1"

        alembic_command.downgrade(self.get_alembic_config(), revision)

    def show_migrations(self):
        alembic_command.history(self.get_alembic_config())

    def create_migration(self, message: str | None = None):
        alembic_command.revision(
            self.get_alembic_config(), message=message, autogenerate=True,
        )