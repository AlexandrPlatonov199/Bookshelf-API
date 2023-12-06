from fastapi import APIRouter, Response, Depends

from src.exceptoins import UserIsNotPresentException
from src.users.auth import get_password_hash, authenticate_user, create_jwt_token
from src.users.dao import UserDAO
from src.users.dependencies import get_current_user
from src.users.models import User
from src.users.shemas import SUser, SUserLogin

router = APIRouter(prefix="/auth",
                   tags=["Auth"])


@router.post("/register")
async def auth_register(user_data: SUser):
    query = await UserDAO.find_one_or_none(email=user_data.email)
    if query:
        raise UserIsNotPresentException
    hash_password = get_password_hash(user_data.password)
    await UserDAO.add(username=user_data.username,email=user_data.email,hash_password=hash_password)

    return {"message": 200}


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    access_token = create_jwt_token({"sub": str(user.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)

    return {"message": "success"}


@router.post("/logaut")
async def logaut_user(response: Response):
    response.delete_cookie("user_access_token")
    return {"message": "Вы вышли из профиля"}

@router.post("/me")
async def read_users_me(user: User = Depends(get_current_user)):
    return user


@router.get("")
async def get_all_user():
    return await UserDAO.find_all()


@router.get("/{username}")
async def get_user(username: str):
    return await UserDAO.find_one_or_none(username=username)