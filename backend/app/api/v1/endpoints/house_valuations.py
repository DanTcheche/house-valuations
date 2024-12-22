import logging
from typing import List
from app.core.config import get_settings
from app.schemas.api.get_house_valuations_request import (
    GetHouseValuationsRequest,
)
from app.use_cases.get_house_valuations_use_case import (
    GetHouseValuationUseCase,
)
from app.schemas.properties.property_schema import PropertySchema
from fastapi import (
    APIRouter,
    Depends,
)

settings = get_settings()

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("")
async def get_house_valuations(
    data: GetHouseValuationsRequest = Depends(),
) -> List[PropertySchema]:
    logger.info(f"Getting house valuations for address: {data.address}")
    return GetHouseValuationUseCase().execute(data.address)
