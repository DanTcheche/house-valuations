from fastapi import FastAPI
from app.api.v1.routers import api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
)
app.include_router(api_router, prefix=settings.API_V1_STR)