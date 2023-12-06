from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqladmin import Admin

from src.admin_panel.auth import authentication_backend
from src.admin_panel.views import BookAdmin, CategoryAdmin, AuthorAdmin, UserAdmin
from src.books.authors.routers import router as router_author
from src.books.categorys.routers import router as router_category
from src.books.routers import router as router_book
from src.config import settings
from src.users.routers import router as router_user
from src.db import async_engine

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

app = FastAPI(title="Bookshelf",
              lifespan="lifespan")

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_category)
app.include_router(router_user)

admin = Admin(app, async_engine, authentication_backend=authentication_backend)

admin.add_view(BookAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(UserAdmin)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8",
                              decode_responses=True)
    yield
    FastAPICache.init(RedisBackend(redis), prefix="cache")