from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import BaseCRUD
from app.db.exceptions.decorators import orm_error_handler
from app.db.models import ProductsModel


class SalesRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = ProductsModel
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    # async def create(self, id: int, name: str, description: str, price: int, available: int) -> ProductsModel:
    #     async with self.base.transaction():
    #         return await self.base.insert(
    #             id=id,
    #             name=name,
    #             description=description,
    #             price=price,
    #             available=available
    #         )

    @orm_error_handler
    async def get_many_sales(self) -> List[ProductsModel]:
        async with self.base.transaction():
            return await self.base.get_many()

    @orm_error_handler
    async def get_one_by_id(self, _id: int) -> List[ProductsModel]:
        async with self.base.transaction():
            return await self.base.get_one(self.model.id == _id)
