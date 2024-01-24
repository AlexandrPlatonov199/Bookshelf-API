import io
import uuid

import pytest
from pydantic import EmailStr

from autotests.clients.rest.users.client import UsersRestClient


class TestUserFlow:
    CONTEXT = {}

    @pytest.mark.dependency()
    @pytest.mark.asyncio
    async def test_create_user(
            self,
            alexandr_users_rest_client: UsersRestClient,
    ):
        first_name = "Not-Alexandr"
        last_name = "Not-Platonov"
        email = "sasa20sasha199910@yandex.ru"

        user = await alexandr_users_rest_client.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        self.CONTEXT["user_id"] = user.id
        self.CONTEXT["user_first_name"] = first_name
        self.CONTEXT["user_last_name"] = last_name
        self.CONTEXT["user_email"] = email

        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.email == email

    @pytest.mark.dependency(depends=["TestUserFlow::test_create_user"])
    @pytest.mark.asyncio
    async def test_get_user(self, users_rest_client: UsersRestClient):
        user_id: uuid.UUID = self.CONTEXT["user_id"]
        user_first_name: str = self.CONTEXT["user_first_name"]
        user_last_name: str = self.CONTEXT["user_last_name"]
        user_email: EmailStr = self.CONTEXT["user_email"]

        user = await users_rest_client.get_user(user_id=user_id)

        assert user.id == user_id
        assert user.first_name == user_first_name
        assert user.last_name == user_last_name
        assert user.email == user_email
