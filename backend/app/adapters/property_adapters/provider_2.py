from app.adapters.property_adapters.base_property_adapter import (
    BasePropertyAdapter,
)
from app.core.config import get_settings
from app.schemas.properties.property_schema import PropertySchema

settings = get_settings()


class Provider2PropertyAdapter(BasePropertyAdapter):
    def __init__(self) -> None:
        endpoint = settings.PROVIDER_2_ENDPOINT
        api_key = settings.PROVIDER_2_API_KEY
        super().__init__(endpoint, api_key)

    def get_property_by_address(self, address: str) -> PropertySchema:
        pass
