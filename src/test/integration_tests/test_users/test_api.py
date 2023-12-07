import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "username, password, email, status_cod",
    [
        ("user1", "user1", "user1@user1.com", 200),
    ],
)
async def test_register_login_logaut_user(
    username, password, email, status_cod, ac: AsyncClient
):
    response_register = await ac.post(
        "/auth/register",
        json={"username": username, "password": password, "email": email},
    )

    assert response_register.status_code == status_cod

    response_login = await ac.post(
        "/auth/login", json={"password": password, "email": email}
    )

    assert response_login.status_code == status_cod

    response_logaut = await ac.post("/auth/logaut")

    assert response_logaut.status_code == status_cod
