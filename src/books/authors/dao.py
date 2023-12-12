from src.books.authors.models import Author
from src.dao.base_dao import BaseDAO


class AuthorDAO(BaseDAO):
    model = Author
