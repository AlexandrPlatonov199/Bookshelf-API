from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class User(Base):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hash_password: Mapped[str] = mapped_column(nullable=False)

    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __str__(self):
        return f"Пользователь {self.username}"