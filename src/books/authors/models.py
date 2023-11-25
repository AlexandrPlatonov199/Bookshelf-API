from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.db import Base


class AuthorModels(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    book: Mapped[list["BookModel"]] = relationship(back_populates="author")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"