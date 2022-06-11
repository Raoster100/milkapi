from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field
from app.v1.delivery.dependencies import DeliveryDependencyMarker
from app.v1.delivery.schemas import DeliveryCreateSchema, DeliveryGetSchema
from app.v1.delivery.crud import DeliveryRepository

delivery_router = APIRouter()


@delivery_router.post("/delivery",
                      response_model=DeliveryCreateSchema)
async def create_delivery(
        data: DeliveryCreateSchema,
        db: DeliveryRepository = Depends(DeliveryDependencyMarker)
):
    return await db.create(street=data.street, house_number=data.house_number, date=data.date, sale_id=data.sale_id)


@delivery_router.get("/delivery")
async def get_delivery(
        db: DeliveryRepository = Depends(DeliveryDependencyMarker)
):
    return await db.get_many_delivery()
