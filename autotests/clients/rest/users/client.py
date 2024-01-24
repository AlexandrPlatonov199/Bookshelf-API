import io
import uuid

import httpx
from pydantic import EmailStr

from autotests.clients.rest.base_client import BaseRestClient
from autotests.clients.rest.exceptions import ResponseException

from .models import HealthResponse, UserResponse, CreateUserResponse


class UsersRestClient(BaseRestClient):
    async def get_health(self) -> HealthResponse:
        path = "/health"

        return await self.rest_get(path=path, response_model=HealthResponse)

    async def get_user(self, user_id: uuid.UUID) -> UserResponse:
        path = f"/api/rest/users/{user_id}"

        return await self.rest_get(path=path, response_model=UserResponse)

    async def create_user(
            self,
            email: EmailStr,
            first_name: str,
            last_name: str,
    ) -> UserResponse:
        path = "api/rest/users/create_user"
        request = CreateUserResponse(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        return await self.rest_post(path=path, data=request, response_model=UserResponse)


