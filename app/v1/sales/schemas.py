from app.schemas.base import BaseModelORM
from app.v1.products.schemas import ProductGetSchema
from app.v1.users.schemas import UsersGetSchema


class GetSalesSchema(BaseModelORM):
    buyer_id: UsersGetSchema
    product_id: ProductGetSchema


class PostSalesSchema(BaseModelORM):
    buyer_id: int
    product_id: int
