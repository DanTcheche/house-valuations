from backend.app.adapters.property_adapters.base_property_adapter import BasePropertyAdapter
from backend.app.core.config import get_settings
from backend.app.schemas.property_schema import PropertySchema

settings = get_settings()


class Provider1PropertyAdapter(BasePropertyAdapter):

    def __init__(self) -> None:
        endpoint = "https://api.provider1.com"
        api_key = ""
        super().__init__(endpoint, api_key)

    def get_property_by_address(self, address: str) -> PropertySchema:
        pass