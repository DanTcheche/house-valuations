import logging
from app.adapters.property_adapters.base_property_adapter import (
    BasePropertyAdapter,
)
from app.core.config import get_settings
from app.schemas.properties.property_schema import PropertySchema
from app.clients.request_client import RequestClient
from app.exceptions.external_provider_exception import (
    ExternalProviderException,
)
from app.schemas.properties.provider_2_property_schema import (
    Provider2PropertySchema,
)

settings = get_settings()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Provider2PropertyAdapter(BasePropertyAdapter):
    def __init__(self) -> None:
        endpoint = settings.PROVIDER_2_ENDPOINT
        api_key = settings.PROVIDER_2_API_KEY
        super().__init__(endpoint, api_key)

    def get_property_by_address(self, address: str) -> PropertySchema:
        logger.info(
            f"Fetching property data from Provider 2 for address: {address}"
        )
        property_by_address = super()._get_data_from_provider(address)
        if not property_by_address or not property_by_address.get("data"):
            logger.warning("Provider 2 failed to return data.")
            raise ExternalProviderException(
                "Provider 2 failed to return data."
            )
        logger.info(
            f"Property data fetched from Provider 2: {property_by_address}"
        )
        return PropertySchema.from_provider_2(
            Provider2PropertySchema.model_validate(
                property_by_address.get("data")
            )
        )
