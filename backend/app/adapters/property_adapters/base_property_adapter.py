from abc import ABC, abstractmethod
from venv import logger
from app.schemas.properties.property_schema import PropertySchema
from app.clients.request_client import RequestClient
from app.exceptions.external_provider_exception import (
    ExternalProviderException,
)


class BasePropertyAdapter(ABC):
    def __init__(self, endpoint: str, api_key: str) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    @abstractmethod
    def get_property_by_address(self, address: str) -> PropertySchema:
        pass

    def _get_data_from_provider(
        self, address: str, provider_name: str
    ) -> dict:
        logger.info(
            f"Fetching property data from {provider_name} for address: {address}"
        )
        property_by_address = RequestClient().make_request(
            endpoint=self.endpoint,
            method="GET",
            headers={"X-API-KEY": self.api_key},
            params={"address": address},
        )
        if not property_by_address or not property_by_address.get("data"):
            logger.warning(f"{provider_name} failed to return data.")
            raise ExternalProviderException(
                f"{provider_name} failed to return data."
            )
        logger.info(
            f"Property data fetched from {provider_name}: {property_by_address}"
        )
        return property_by_address
