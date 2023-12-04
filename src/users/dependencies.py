from fastapi import Request, Depends
from jose import jwt, JWTError, ExpiredSignatureError

from src.config import settings
from src.exceptoins import TokenAbsentException, TokenExpiredException, IncorrectTokenFormatException, \
    UserIsNotPresentException
from src.users.dao import UserDAO


def get_token_user(request: Request) -> str:
    token = request.cookies.get("user_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token_user)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user