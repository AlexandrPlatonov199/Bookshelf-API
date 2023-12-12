from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.config import settings
from src.exceptoins import IncorrectEmailOrPasswordException, UserIsNotPresentException
from src.users.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hash_password) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encode_jwt


async def authenticate_user(email: EmailStr, password):
    user = await UserDAO.find_one_or_none(email=email)
    if not user:
        raise UserIsNotPresentException
    if not verify_password(password, user.hash_password):
        raise IncorrectEmailOrPasswordException
    return user
