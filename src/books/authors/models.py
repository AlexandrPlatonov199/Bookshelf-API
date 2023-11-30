from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Author(Base):
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"