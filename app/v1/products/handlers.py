from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.products.dependencies import ProductsDependencyMarker
from app.v1.products.schemas import ProductCreateSchema, ProductUpdateSchema, ProductGetSchema
from app.v1.products.crud import ProductsRepository

products_router = APIRouter()


@products_router.post("/products")
async def create_product(
        data: ProductCreateSchema,
        db: ProductsRepository
):
    return await db.create(name=data.name, description=data.description, price=data.price, available=data.available)


@products_router.get("/products",
                     response_model=List[ProductGetSchema]
                     )
async def get_products(
        db: ProductsRepository = Depends(ProductsDependencyMarker)
):
    return await db.get_many_products()
