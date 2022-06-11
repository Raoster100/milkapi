from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.users.dependencies import UsersDependencyMarker
from app.v1.users.crud import UsersRepository
from app.v1.users.schemas import UsersPostSchema, UsersGetSchema

users_router = APIRouter()


@users_router.post("/users",
                   response_model=UsersPostSchema)
async def create_user(
        data: UsersPostSchema,
        db: UsersRepository = Depends(UsersDependencyMarker)
):
    return await db.create(
        name=data.name,
        telegram_id=data.telegram_id,
        telegram_login=data.telegram_login
    )


@users_router.get("/users/{id}",
                  response_model=UsersGetSchema)
async def get_users_by_id(
        _id: int = Path(..., alias='id'),
        db: UsersRepository = Depends(UsersDependencyMarker)
):
    return await db.get_by_id(_id=_id)
