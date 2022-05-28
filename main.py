import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.handlers.exceptions import sql_exception_handler
from app.handlers.models import ExceptionSQL
from app.v1.binding import own_router_v1
from app.v1.files import FileRepository, FileDependencyMarker
from app.v1.history.crud import HistoryRepository
from app.v1.history.dependencies import HistoryDependencyMarker
from app.v1.posts.crud import PostRepository
from app.v1.posts.dependencies import PostDependencyMarker
from app.v1.users.crud import UserRepository
from app.v1.users.dependencies import UserDependencyMarker
from misc import async_session





def get_application_v1() -> FastAPI:
    application = FastAPI(
        debug=True,
        title='User Hosting',
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
            FileDependencyMarker: lambda: FileRepository(db_session=async_session),
            PostDependencyMarker: lambda: PostRepository(db_session=async_session),
            UserDependencyMarker: lambda: UserRepository(db_session=async_session),
            HistoryDependencyMarker: lambda: HistoryRepository(db_session=async_session)
        }
    )

    return application


app = get_application_v1()

if __name__ == "__main__":
    uvicorn.run(app)