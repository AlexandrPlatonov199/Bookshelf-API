from datetime import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base


class BookModel(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id = mapped_column(ForeignKey("author.id"))
    category_id = mapped_column(ForeignKey("category.id"))
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    year_publication: Mapped[int] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(unique=True, nullable=False)
    number_page: Mapped[int] = mapped_column(nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)
    cover_type: Mapped[str] = mapped_column(nullable=False)
    age_restrictions: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    category: Mapped[list["CategoryModel"]] = relationship(back_populates="book")
    author: Mapped["AuthorModels"] = relationship(back_populates="book")

    def __str__(self):
        return self.name