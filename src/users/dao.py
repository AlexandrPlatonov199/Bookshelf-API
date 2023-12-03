from src.dao.base_dao import BaseDAO
from src.users.models import User


class UserDAO(BaseDAO):
    model = User

    # @classmethod
    # async def add_user(cls, data):
    #     async with async_sessionmaker() as session:
    #         query = select(User).filter_by(username=data.get("username"), email=data.get("email"))
    #         res_query = await session.execute(query)
    #         res = res_query.mappings().one_or_none()
    #         if res:
    #             raise HTTPException(status_code=404, detail="Данный пользователь уже зарегистрирован")
    #         hash_passw = get_password_hash(data.get("password"))
    #         stmt = insert(User).values(username=data.get("username"), email=data.get("email"), hash_password=hash_passw)
    #         await session.execute(stmt)
    #         await session.commit()
    #         return {"message": 200}