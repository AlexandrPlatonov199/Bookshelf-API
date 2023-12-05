import asyncio
import json

import pytest
from sqlalchemy import insert

from src.books.authors.models import Author
from src.books.categorys.models import Category
from src.books.models import Book
from src.config import settings
from src.db import async_engine, Base, async_sessionmaker
from src.users.models import User


@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
    assert settings.MODE == "TEST"
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(mod: str):
        with open(f"src/test/mock_{mod}.json", encoding="utf-8") as file:
            return json.load(file)

    authors = open_mock_json("authors")
    categorys = open_mock_json("categorys")
    users = open_mock_json("users")
    books = open_mock_json("books")

    async with async_sessionmaker() as session:
        for Model, values in [
            (Author, authors),
            (Category, categorys),
            (User, users),
            (Book, books),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
