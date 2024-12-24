from abc import ABC, abstractmethod
from app.schemas.properties.property_schema import PropertySchema
from app.clients.request_client import RequestClient


class BasePropertyAdapter(ABC):
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    @abstractmethod
    def get_property_by_address(self, address: str) -> PropertySchema:
        pass

    def _get_data_from_provider(self, address: str) -> dict | None:
        return RequestClient().make_request(
            endpoint=self.endpoint,
            method="GET",
            headers={"X-API-KEY": self.api_key},
            params={"address": address},
        )
