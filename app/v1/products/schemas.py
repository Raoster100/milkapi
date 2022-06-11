from app.schemas.base import BaseModelORM
from app.v1.catalogs.schemas import CatalogGetSchema


class ProductCreateSchema(BaseModelORM):
    name: str
    description: str
    price: str
    available: int
    catalog_id: int


class ProductUpdateSchema(BaseModelORM):
    price: int


class ProductGetSchema(BaseModelORM):
    name: str
    description: str
    price: str
    available: int
    catalog: CatalogGetSchema
