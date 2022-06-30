from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import BaseCRUD
from app.db.exceptions.decorators import orm_error_handler
from app.db.models import UsersModel
import psycopg2
from uuid import UUID


class UsersRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = UsersModel
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def create(self, name: str, telegram_id: int, telegram_login: str, password: str) -> UsersModel:
        async with self.base.transaction():
            return await self.base.insert(
                name=name,
                telegram_id=telegram_id,
                telegram_login=telegram_login,
                password=password
            )

    async def delete(self, _id: int) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.delete(
                self.model.id == _id
            )

    async def update(self, _id: int, name: str, telegram_id: int, telegram_login: str, password: str) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.update(
                self.model.id == _id,
                name=name,
                telegram_id=telegram_id,
                telegram_login=telegram_login,
                password=password
            )

    @orm_error_handler
    async def get_many_users(self) -> List[UsersModel]:
        async with self.base.transaction():
            return await self.base.get_many()

    @orm_error_handler
    async def get_by_id(self, _id: int) -> UsersModel:
        async with self.base.transaction():
            return await self.base.get_one(self.model.id == _id)
