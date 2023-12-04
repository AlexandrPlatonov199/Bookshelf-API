from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base

if TYPE_CHECKING:
    from src.books.categorys.models import Category
    from src.users.models import User


class Book(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    year_publication: Mapped[int] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(unique=True, nullable=False)
    number_page: Mapped[int] = mapped_column(nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)
    cover_type: Mapped[str] = mapped_column(nullable=False)
    age_restrictions: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categorys.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    users: Mapped["User"] = relationship(back_populates="books")
    categorys: Mapped[list["Category"]] = relationship(back_populates="books")

    def __str__(self):
        return self.name