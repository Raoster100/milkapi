from datetime import datetime

from app.schemas.base import BaseModelORM


class DeliveryCreateSchema:
    street: str
    house_number: str
    date: datetime
    sale_id: int


class DeliveryGetSchema:
    id: int
    street: str
    house_number: str
    date: datetime
    sale_id: int
