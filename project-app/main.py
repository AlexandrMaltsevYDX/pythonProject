from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.db.helper import db_helper
from core.router import main_router
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001, ANN201
    # startup
    yield
    # shutdown
    print('dispose engine')  # noqa: T201
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
