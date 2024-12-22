from abc import ABC, abstractmethod
from backend.app.schemas.property_schema import PropertySchema


class BasePropertyAdapter(ABC):

    def __init__(self, endpoint: str, api_key: str) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    @abstractmethod
    def get_property_by_address(self, address: str) -> PropertySchema:
        pass
