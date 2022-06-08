from fastapi import APIRouter

from app.v1.users.handlers import users_router
from app.v1.sales.handlers import sales_router
from app.v1.delivery.handlers import delivery_router
from app.v1.catalogs.handlers import catalogs_router
from app.v1.products.handlers import products_router

own_router_v1 = APIRouter()
own_router_v1.include_router(users_router, tags=['Users'])
own_router_v1.include_router(sales_router, tags=['Sales'])
own_router_v1.include_router(delivery_router, tags=['Delivery'])
own_router_v1.include_router(catalogs_router, tags=['Catalogs'])
own_router_v1.include_router(products_router, tags=['Products'])
