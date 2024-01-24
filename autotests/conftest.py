import asyncio
import random
import uuid

import pytest

from autotests.clients.rest.users.client import UsersRestClient

from .settings import AutotestsSettings


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def settings() -> AutotestsSettings:
    return AutotestsSettings()


@pytest.fixture(scope="session")
def alexandr_id(settings: AutotestsSettings) -> uuid.UUID:
    return settings.alexandr_id


@pytest.fixture(scope="session")
def random_id(settings: AutotestsSettings) -> uuid.UUID:
    return uuid.uuid4()


@pytest.fixture(scope="session")
def alexandr_email(settings: AutotestsSettings) -> str:
    return settings.alexandr_email


@pytest.fixture(scope="session")
def users_rest_client(settings: AutotestsSettings) -> UsersRestClient:
    return UsersRestClient(base_url=str(settings.users_base_url))


@pytest.fixture(scope="session")
def alexandr_activated_users_rest_client(
        settings: AutotestsSettings,
) -> UsersRestClient:
    return UsersRestClient(
        base_url=str(settings.users_base_url),
    )


@pytest.fixture(scope="session")
def alexandr_users_rest_client(
        settings: AutotestsSettings,
) -> UsersRestClient:
    return UsersRestClient(
        base_url=str(settings.users_base_url),
    )


@pytest.fixture(scope="session")
def random_users_rest_client(settings: AutotestsSettings):
    return UsersRestClient(
        base_url=str(settings.users_base_url),
    )