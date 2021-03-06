from app.schemas.base import BaseModelORM


class CatalogGetSchema(BaseModelORM):
    id: int
    name: str


class CatalogCreateSchema(BaseModelORM):
    name: str


class CatalogUpdateSchema(BaseModelORM):
    name: str