import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.handlers.exceptions import sql_exception_handler
from app.handlers.models import ExceptionSQL
from app.v1.binding import own_router_v1
from app.v1.catalogs.crud import CatalogsRepository
from app.v1.catalogs.dependencies import CatalogsDependencyMarker
from app.v1.products.dependencies import ProductsDependencyMarker
from app.v1.products.crud import ProductsRepository
from app.v1.sales.crud import SalesRepository
from app.v1.sales.dependencies import SalesDependencyMarker
from app.v1.users.crud import UsersRepository
from app.v1.users.dependencies import UsersDependencyMarker
from app.v1.delivery.crud import DeliveryRepository
from app.v1.delivery.dependencies import DeliveryDependencyMarker
from misc import async_session





def get_application_v1() -> FastAPI:
    application = FastAPI(
        debug=True,
        title='MilkBot',
        version='1.2.15',
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=['*']
    )
    application.include_router(own_router_v1)
    application.add_exception_handler(ExceptionSQL, sql_exception_handler)
    application.dependency_overrides.update(
        {
            CatalogsDependencyMarker: lambda: CatalogsRepository(db_session=async_session),
            ProductsDependencyMarker: lambda: ProductsRepository(db_session=async_session),
            UsersDependencyMarker: lambda: UsersRepository(db_session=async_session),
            SalesDependencyMarker: lambda: SalesRepository(db_session=async_session),
            DeliveryDependencyMarker: lambda: DeliveryRepository(db_session=async_session)
        }
    )

    return application


app = get_application_v1()

if __name__ == "__main__":
    uvicorn.run(app)