from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base

if TYPE_CHECKING:
    from src.books.models import Book


class User(Base):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hash_password: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    books: Mapped[list["Book"]] = relationship(back_populates="users")

    def __str__(self):
        return f"Пользователь {self.username}"