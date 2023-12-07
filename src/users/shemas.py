from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    username: str
    password: str
    email: EmailStr


class SUserLogin(BaseModel):
    password: str
    email: EmailStr
