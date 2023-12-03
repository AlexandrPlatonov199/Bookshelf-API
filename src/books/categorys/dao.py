from src.books.categorys.models import Category
from src.dao.base_dao import BaseDAO


class CategoryDAO(BaseDAO):
    model = Category