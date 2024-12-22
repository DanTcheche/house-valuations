from abc import ABC, abstractmethod
from app.schemas.properties.property_schema import PropertySchema


class BasePropertyAdapter(ABC):
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    @abstractmethod
    def get_property_by_address(self, address: str) -> PropertySchema:
        pass
