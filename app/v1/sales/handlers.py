from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field

from app.v1.sales.crud import SalesRepository
from app.v1.sales.dependencies import SalesDependencyMarker
from app.v1.sales.schemas import GetSalesSchema, PostSalesSchema

sales_router = APIRouter()


@sales_router.get("/sales",
                  response_model=List[GetSalesSchema]
                  )
async def get_sales(
        db: SalesRepository = Depends(SalesDependencyMarker)
):
    return await db.get_many_sales()


@sales_router.post("/sales",
                   response_model=List[PostSalesSchema])
async def create_sale(
        data: PostSalesSchema,
        db: SalesRepository = Depends(SalesDependencyMarker)
):
    return await db.create(buyer_id=data.buyer_id, product_id=data.product_id)

@sales_router.delete("/sales/{id}")
async def delete_catalogs(
        _id: int = Path(..., alias='id'),
        db: SalesRepository = Depends(SalesDependencyMarker)
):
    return await db.delete(_id)
