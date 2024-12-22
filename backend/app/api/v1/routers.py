from app.api.v1.endpoints import house_valuations
from fastapi import (
    APIRouter,
)

api_router = APIRouter()

api_router.include_router(
    house_valuations.router, prefix="/house-valuations", tags=["house-valuations"]
)
