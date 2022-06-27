from app.schemas.base import BaseModelORM
from app.v1.catalogs.schemas import CatalogGetSchema


class ProductCreateSchema(BaseModelORM):
    name: str
    description: str
    price: float
    available: int
    catalog_id: int


class ProductUpdateSchema(BaseModelORM):
    name: str
    description: str
    price: float
    available: int


class ProductGetSchema(BaseModelORM):
    id: int
    name: str
    description: str
    price: float
    available: int
    catalog: CatalogGetSchema
