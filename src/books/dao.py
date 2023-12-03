from src.books.models import Book
from src.dao.base_dao import BaseDAO


class BookDAO(BaseDAO):
    model = Book