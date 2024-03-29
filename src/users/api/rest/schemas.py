import uuid

from pydantic import BaseModel, ConfigDict, EmailStr, NaiveDatetime

from src.users.database.models import User


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    is_activated: bool
    updated_at: NaiveDatetime
    created_at: NaiveDatetime

    @classmethod
    def from_db_model(cls, user: User, with_email: bool = True) -> "UserResponse":
        return cls(
            id=user.id,
            email=user.email if with_email else None,
            first_name=user.first_name,
            last_name=user.last_name,
            is_activated=user.is_activated,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )