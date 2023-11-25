from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing_extensions import AsyncGenerator

from src.config import settings


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(settings.DATABASE_URL)
async_sessionmaker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session