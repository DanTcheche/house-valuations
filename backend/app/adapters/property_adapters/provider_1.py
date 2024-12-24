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
        property_by_address = super()._get_data_from_provider(
            address, "Provider 1"
        )
        return PropertySchema.from_provider_1(
            Provider1PropertySchema.model_validate(
                property_by_address.get("data")
            )
        )
