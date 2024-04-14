from fastapi import FastAPI

from .common import Settings
from .router import include 

from .connection.postgres.conn import test_db

async def lifespan(app: FastAPI):
    ml_models = {}

    await test_db()
    
    yield ml_models


def api_factory() -> FastAPI:
    app = FastAPI(
        **Settings().fastapi,
        lifespan=lifespan,
    )

    include(app)
    
    return app
