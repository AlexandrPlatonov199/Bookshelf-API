import pytest

from src.users.dao import UserDAO


@pytest.mark.parametrize("username, email", [
    ("test", "test@test.com"),
    ("sasa", "sasha@example.com")
])
async def test_user_find_one_or_none(username, email):
    user = await UserDAO.find_one_or_none(email=email, username=username)

    assert user.username == username
    assert user.email == email




