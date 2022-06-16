from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.catalogs.schemas import CatalogCreateSchema, CatalogGetSchema, CatalogUpdateSchema
from app.v1.catalogs.crud import CatalogsRepository
from app.v1.catalogs.dependencies import CatalogsDependencyMarker

catalogs_router = APIRouter()


@catalogs_router.post("/catalogs",
                      response_model=CatalogCreateSchema)
async def create_catalog(
        data: CatalogCreateSchema,
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.create(name=data.name)


@catalogs_router.get("/catalogs",
                     response_model=List[CatalogGetSchema])
async def get_catalogs(
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.get_many_catalogs()


@catalogs_router.patch("/catalogs",
                       response_model=List[CatalogUpdateSchema])
async def update_catalog(
        data: CatalogUpdateSchema,
        _id: int = Path(..., alias='id'),
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.update_catalogs(_id=_id, name=data.name)


@catalogs_router.delete("/catalogs/{id}")
async def delete_catalogs(
        _id: int = Path(..., alias='id'),
        db: CatalogsRepository = Depends(CatalogsDependencyMarker)
):
    return await db.delete(_id)
