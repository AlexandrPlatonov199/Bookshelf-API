import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("username, email, password, status_code", [
    ("gogo", "gogo@test.com", "gogo", 200),
    ("gogo", "gogo@test.com", "gogo", 401),
    ("gogo", "dfhdfh", "gogo", 422),
])
async def test_auth_register(username, email, password, status_code, ac: AsyncClient):
    result = await ac.post("/auth/register", json={
        "username": username,
        "password": password,
        "email": email,
    })

    assert result.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200)
])
async def test_login_user(email, password, status_code, ac):
    result = await ac.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert result.status_code == status_code