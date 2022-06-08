from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import BaseCRUD
from app.db.exceptions.decorators import orm_error_handler
from app.db.models import CatalogsModel


class CatalogsRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = CatalogsModel
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def create(self, id: int, name: str) -> CatalogsModel:
        async with self.base.transaction():
            return await self.base.insert(
                id=id,
                name=name
            )

    async def delete(self, _id: int) -> List[CatalogsModel]:
        async with self.base.transaction():
            return await self.base.delete(
                self.model.id == _id
            )

    async def update(self, _id: int, name: str) -> List[CatalogsModel]:
        async with self.base.transaction():
            return await self.base.update(
                self.model.id == _id,
                name=name
            )

    @orm_error_handler
    async def get_many_catalogs(self) -> List[CatalogsModel]:
        async with self.base.transaction():
            return await self.base.get_many()
