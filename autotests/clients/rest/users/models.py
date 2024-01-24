import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, constr


class HealthResponse(BaseModel):
    name: Literal["Users"]
    version: constr(pattern=r"^\d+\.\d+\.\d+$")


class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    is_activated: bool
    created_at: datetime
    updated_at: datetime


class CreateUserResponse(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str