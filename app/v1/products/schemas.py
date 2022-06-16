from app.schemas.base import BaseModelORM
from app.v1.catalogs.schemas import CatalogGetSchema


class ProductCreateSchema(BaseModelORM):
    name: str
    description: str
    price: str
    available: int
    catalog_id: CatalogGetSchema


class ProductUpdateSchema(BaseModelORM):
    name: str
    description: str
    price: int
    available: int


class ProductGetSchema(BaseModelORM):
    name: str
    description: str
    price: str
    available: int
    catalog: CatalogGetSchema
