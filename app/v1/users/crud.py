from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import BaseCRUD
from app.db.exceptions.decorators import orm_error_handler
from app.db.models import UsersModel
import psycopg2

class UsersRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = UsersModel
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def create(self, _id: int, name: str, telegram_id: int, telegram_login: str) -> UsersModel:
        async with self.base.transaction():
            return await self.base.insert(
                id=_id,
                name=name,
                telegram_id=telegram_id,
                telegram_login=telegram_login
            )

    async def delete(self, _id: int) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.delete(
                self.model.id == _id
            )

    async def update(self, _id: int, name: str, telegram_id: int, telegram_login: str) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.update(
                self.model.id == _id,
                name=name,
                telegram_id=telegram_id,
                telegram_login=telegram_login
            )

    @orm_error_handler
    async def get_many_catalogs(self) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.get_many()
