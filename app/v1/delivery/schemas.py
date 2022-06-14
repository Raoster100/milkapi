from datetime import datetime

from app.schemas.base import BaseModelORM


class DeliveryCreateSchema(BaseModelORM):
    street: str
    house_number: str
    date: datetime
    sale_id: int


class DeliveryGetSchema(BaseModelORM):
    id: int
    street: str
    house_number: str
    date: datetime
    sale_id: int
