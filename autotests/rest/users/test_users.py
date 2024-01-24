import uuid

import pytest

from autotests.clients.rest.users.client import UsersRestClient


@pytest.mark.parametrize(("user_id", "client"), (
        (pytest.lazy_fixture("alexandr_id"), pytest.lazy_fixture("random_users_rest_client")),
))
@pytest.mark.asyncio
async def test_get_user(user_id: uuid.UUID, client: UsersRestClient):
    user = await client.get_user(user_id=user_id)

    assert user.id == user_id
