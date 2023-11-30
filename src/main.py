from fastapi import FastAPI

from src.books.authors.routers import router as router_author
from src.books.categorys.routers import router as router_category
from src.books.routers import router as router_book

app = FastAPI(title="Bookshelf")

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_category)