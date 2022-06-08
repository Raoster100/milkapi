from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field

from app.v1.users.crud import UsersRepository
from app.v1.users.schemas import UsersPostSchema, UsersGetSchema

users_router = APIRouter()


@users_router.post("/users")
async def create_user(
        data: UsersPostSchema,
        db: UsersRepository
):
    return await db.create(name=data.name, telegram_id=data.telegram_id, telegram_login=data.telegram_login)
