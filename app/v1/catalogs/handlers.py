from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.catalogs.schemas import CatalogCreateSchema, CatalogGetSchema
from app.v1.catalogs.crud import CatalogsRepository
from app.v1.catalogs.dependencies import CatalogsDependencyMarker

catalogs_router = APIRouter()


@catalogs_router.post("/catalogs")
async def create_catalog(
        data: CatalogCreateSchema,
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.create(name=data.name)


@catalogs_router.get("/catalogs")
async def get_catalogs(
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.get_many_catalogs()
