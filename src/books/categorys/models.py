from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base

if TYPE_CHECKING:
    from src.books.models import Book


class Category(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    books: Mapped[list["Book"]] = relationship(back_populates="categorys")

    def __str__(self):
        return self.name
