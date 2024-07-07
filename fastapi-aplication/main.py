from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router as api_router
from core.config import settings

from core.models import db_helper, User

from api.api_v1 import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(User.metadata.drop_all)
    
    yield
    await db_helper.dispose() # Закрытие сессии посли завершения прогргаммы

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(api_router, prefix=settings.api.prefix)
main_app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True) 
