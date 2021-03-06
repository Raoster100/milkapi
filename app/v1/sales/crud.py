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

    async def create(self, buyer_id: int, product_id: int) -> ProductsModel:
        async with self.base.transaction():
            return await self.base.insert(
                buyer_id=buyer_id,
                product_id=product_id
            )

    @orm_error_handler
    async def get_many_sales(self) -> List[ProductsModel]:
        async with self.base.transaction():
            return await self.base.get_many()

    @orm_error_handler
    async def get_one_by_id(self, _id: int) -> List[ProductsModel]:
        async with self.base.transaction():
            return await self.base.get_one(self.model.id == _id)
