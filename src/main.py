from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin
import time
from fastapi_versioning import VersionedFastAPI

from src.admin_panel.auth import authentication_backend
from src.admin_panel.views import AuthorAdmin, BookAdmin, CategoryAdmin, UserAdmin
from src.books.authors.routers import router as router_author
from src.books.categorys.routers import router as router_category
from src.books.routers import router as router_book
from src.config import settings
from src.db import async_engine
from src.logger import logger
from src.users.routers import router as router_user


sentry_sdk.init(
    dsn="https://53e3a1594151c2f94cc637f2f8d5cd7f@o4506359447355392.ingest.sentry.io/4506359449255936",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield

app = FastAPI(title="Bookshelf", lifespan=lifespan)

app.include_router(router_author)
app.include_router(router_book)
app.include_router(router_category)
app.include_router(router_user)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response


app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}')


admin = Admin(app, async_engine, authentication_backend=authentication_backend)

admin.add_view(BookAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(UserAdmin)