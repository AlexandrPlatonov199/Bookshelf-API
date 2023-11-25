from fastapi import FastAPI

from books.authors.routers import router as router_author
from books.categorys.routers import router as router_category
from books.routers import router as router_book

app = FastAPI(title="Bookshelf")

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_category)