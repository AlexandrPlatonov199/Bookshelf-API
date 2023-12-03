from fastapi import FastAPI
from sqladmin import Admin

from src.admin_panel.views import BookAdmin, CategoryAdmin, AuthorAdmin
from src.books.authors.routers import router as router_author
from src.books.categorys.routers import router as router_category
from src.books.routers import router as router_book
from src.users.routers import router as router_user
from src.db import async_engine

app = FastAPI(title="Bookshelf")

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_category)
app.include_router(router_user)

admin = Admin(app, async_engine)

admin.add_view(BookAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(AuthorAdmin)