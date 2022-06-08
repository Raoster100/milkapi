import datetime
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud import BaseCRUD
from app.db.exceptions.decorators import orm_error_handler
from app.db.models import DeliveryModel


class DeliveryRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = DeliveryModel
        self.base = BaseCRUD(db_session=db_session, model=self.model)

    async def create(self, id: int, street: str, house_number: str, date: datetime) -> DeliveryModel:
        async with self.base.transaction():
            return await self.base.insert(
                id=id,
                street=street,
                house_number=house_number,
                date=date
            )

    async def delete(self, _id: int) -> List[DeliveryModel]:
        async with self.base.transaction():
            return await self.base.delete(
                self.model.id == _id
            )

    @orm_error_handler
    async def get_many_delivery(self) -> List[DeliveryModel]:
        async with self.base.transaction():
            return await self.base.get_many()

    @orm_error_handler
    async def get_one_by_id(self, _id: int) -> List[DeliveryModel]:
        async with self.base.transaction():
            return await self.base.get_one(self.model.id == _id)
