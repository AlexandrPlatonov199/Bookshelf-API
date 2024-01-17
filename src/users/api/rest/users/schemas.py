import uuid

from pydantic import BaseModel, constr, EmailStr


class UserUpdateRequest(BaseModel):
    first_name: constr(strip_whitespace=True, min_length=1)
    last_name: constr(strip_whitespace=True, min_length=1)
    about: str | None


class UserCreateRequest(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str