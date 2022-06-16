from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.products.dependencies import ProductsDependencyMarker
from app.v1.products.schemas import ProductCreateSchema, ProductUpdateSchema, ProductGetSchema
from app.v1.products.crud import ProductsRepository

products_router = APIRouter()


@products_router.post("/products",
                      response_model=List[ProductCreateSchema])
async def create_product(
        data: ProductCreateSchema,
        db: ProductsRepository = Depends(ProductsDependencyMarker)
):
    return await db.create(name=data.name, description=data.description, price=data.price, available=data.available,
                           catalog_id=data.catalog_id)


@products_router.get("/products",
                     response_model=List[ProductGetSchema]
                     )
async def get_products(
        db: ProductsRepository = Depends(ProductsDependencyMarker)
):
    return await db.get_many_products()


@products_router.patch("/products",
                       response_model=List[ProductUpdateSchema]
                       )
async def patch_products(
        data: ProductUpdateSchema,
        _id: int = Path(..., alias='id'),
        db: ProductsRepository = Depends(ProductsDependencyMarker)
):
    return await db.update_products(_id=_id, name=data.name, description=data.description, price=data.price,
                                    available=data.available)
