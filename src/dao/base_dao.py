from sqlalchemy import select, insert

from src.db import async_sessionmaker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_sessionmaker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls):
        async with async_sessionmaker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        query = insert(cls.model).values(**data).returning(cls.model.__table__.columns)
        async with async_sessionmaker() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()
