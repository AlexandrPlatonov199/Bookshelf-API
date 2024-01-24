import pytest

from src.users.settings import UsersSettings


@pytest.fixture()
def settings() -> UsersSettings:
    return UsersSettings()