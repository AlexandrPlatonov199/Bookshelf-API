from unittest.mock import MagicMock, patch

import pytest

from src.common.database.service import BaseDatabaseService


@pytest.mark.asyncio
async def test_transaction(database_service: BaseDatabaseService):
    session_mock = MagicMock()
    sessionmaker_mock_context = MagicMock()
    sessionmaker_mock_context.__aenter__.return_value = session_mock
    sessionmaker_mock = MagicMock(return_value=sessionmaker_mock_context)

    with patch.object(database_service, "_sessionmaker", sessionmaker_mock):
        async with database_service.transaction() as session:
            pass

    assert session is session_mock
    sessionmaker_mock.assert_called_once_with()
    sessionmaker_mock_context.__aenter__.assert_called_once_with()


@patch("src.common.database.service.alembic_command")
def test_create_migration(mock_alembic_command: MagicMock, database_service: BaseDatabaseService):
    message = "Any message"
    config = MagicMock()

    with patch.object(
            database_service,
            "get_alembic_config",
            return_value=config,
    ) as get_alembic_config_mock:
        database_service.create_migration(message=message)

    get_alembic_config_mock.assert_called_once()
    mock_alembic_command.revision.assert_called_once_with(
        config,
        message=message,
        autogenerate=True,
    )


@patch("src.common.database.service.alembic_command")
def test_migrate(mock_alembic_command: MagicMock, database_service: BaseDatabaseService):
    config = MagicMock()

    with patch.object(
            database_service,
            "get_alembic_config",
            return_value=config,
    ) as get_alembic_config_mock:
        database_service.migrate()

    get_alembic_config_mock.assert_called_once()
    mock_alembic_command.upgrade.assert_called_once_with(config, "head")
