from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from src.users.auth import get_password_hash
from src.users.dao import UserDAO
from src.users.models import User
from src.users.shemas import SUser

router = APIRouter(prefix="/auth",
                   tags=["Auth"])


@router.post("")
async def auth_register(user_data: SUser):
    query = await UserDAO.find_one_or_none(email=user_data.email)
    if query:
        raise HTTPException(status_code=404, detail="Данный пользователь уже зарегистрирован")
    hash_password = get_password_hash(user_data.password)
    stmt = await UserDAO.add(username=user_data.username,email=user_data.email,hash_password=hash_password)
    return {"message": 200}


@router.get("")
async def get_all_user():
    query = await UserDAO.find_all()
    return query

@router.get("/{username}")
async def get_user(username: str):
    query = await UserDAO.find_one_or_none(username=username)
    return query