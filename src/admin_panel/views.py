from sqladmin import ModelView

from src.books.authors.models import Author
from src.books.categorys.models import Category
from src.books.models import Book


class BookAdmin(ModelView, model=Book):
    column_list = [c.name for c in Book.__table__.columns] + [Book.categorys]
    name = "Книга"
    name_plural = "Книги"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name, Category.create_date, Category.books]
    name = "Категория"
    name_plural = "Категории"


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.first_name, Author.last_name, Author.create_date]
    name = "Автор"
    name_plural = "Авторы"


