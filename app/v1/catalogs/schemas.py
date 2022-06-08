from app.schemas.base import BaseModelORM


class CatalogGetSchema(BaseModelORM):
    id: int
    name: str
