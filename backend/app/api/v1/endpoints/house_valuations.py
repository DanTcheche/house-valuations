from app.core.config import get_settings
from fastapi import (
    APIRouter,
)
from app.main import app

settings = get_settings()

router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Hello World"}