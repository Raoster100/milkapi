from app.schemas.base import BaseModelORM


class UsersPostSchema(BaseModelORM):
    name: str
    telegram_id: int
    telegram_login: str


class UsersGetSchema(BaseModelORM):
    name: str
    telegram_id: int
    telegram_login: str
