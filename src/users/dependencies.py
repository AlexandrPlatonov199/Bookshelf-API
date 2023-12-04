from fastapi import Request, Depends, HTTPException, status
from jose import jwt, JWTError, ExpiredSignatureError

from src.config import settings
from src.users.dao import UserDAO


def get_token_user(request: Request) -> str:
    token = request.cookies.get("user_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не найден")
    return token


async def get_current_user(token: str = Depends(get_token_user)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ошибка декодирования токена")
    user_id: str = payload.get("sub")
    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь по ид в бд не найден")
    return user