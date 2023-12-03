from fastapi import APIRouter, status, HTTPException, Response

from src.users.auth import get_password_hash, authenticate_user, create_jwt_token
from src.users.dao import UserDAO
from src.users.shemas import SUser, SUserLogin

router = APIRouter(prefix="/auth",
                   tags=["Auth"])


@router.post("")
async def auth_register(user_data: SUser):
    query = await UserDAO.find_one_or_none(email=user_data.email)
    if query:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Данный пользователь уже зарегистрирован")
    hash_password = get_password_hash(user_data.password)
    await UserDAO.add(username=user_data.username,email=user_data.email,hash_password=hash_password)

    return {"message": 200}


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(email=user_data.email, password=user_data.password)
    access_token = create_jwt_token({"sub": user.id})
    response.set_cookie("user_access_token", access_token, httponly=True)

    return {"message": "success"}


@router.get("")
async def get_all_user():
    return await UserDAO.find_all()


@router.get("/{username}")
async def get_user(username: str):
    return await UserDAO.find_one_or_none(username=username)