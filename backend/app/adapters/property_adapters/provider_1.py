import logging
from app.adapters.property_adapters.base_property_adapter import (
    BasePropertyAdapter,
)
from app.clients.request_client import RequestClient
from app.core.config import get_settings
from app.schemas.properties.property_schema import PropertySchema
from app.exceptions.external_provider_exception import (
    ExternalProviderException,
)
from app.schemas.properties.provider_1_property_schema import (
    Provider1PropertySchema,
)

settings = get_settings()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Provider1PropertyAdapter(BasePropertyAdapter):
    def __init__(self) -> None:
        endpoint = settings.PROVIDER_1_ENDPOINT
        api_key = settings.PROVIDER_1_API_KEY
        super().__init__(endpoint, api_key)

    def get_property_by_address(self, address: str) -> PropertySchema:
        logger.info(f"Fetching property data from Provider 1 for address: {address}")
        property_by_address = RequestClient().make_request(
            endpoint=self.endpoint,
            method="GET",
            headers={"X-API-KEY": self.api_key},
            params={"address": address},
        )
        if not property_by_address or not property_by_address.get("data"):
            logger.warning("Provider 1 failed to return data.")
            raise ExternalProviderException(
                "Provider 1 failed to return data."
            )
        logger.info(f"Property data fetched from Provider 1: {property_by_address}")
        return PropertySchema.from_provider_1(
            Provider1PropertySchema.model_validate(
                property_by_address.get("data")
            )
        )
