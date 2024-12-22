from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
from typing import List

from app.adapters.property_adapters.base_property_adapter import (
    BasePropertyAdapter,
)
from app.adapters.property_adapters.provider_1 import Provider1PropertyAdapter
from app.adapters.property_adapters.provider_2 import Provider2PropertyAdapter
from app.schemas.properties.property_schema import PropertySchema

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GetHouseValuationUseCase:
    def __init__(self) -> None:
        self.adapters = [
            Provider1PropertyAdapter(),
            Provider2PropertyAdapter(),
        ]

    def execute(self, house_address: str) -> List[PropertySchema]:
        results = []
        with ThreadPoolExecutor() as executor:
            future_to_adapter = {
                executor.submit(
                    self.__fetch_data_from_adapter, adapter, house_address
                ): adapter
                for adapter in self.adapters
            }
            for future in as_completed(future_to_adapter):
                adapter = future_to_adapter[future]
                try:
                    data = future.result()
                    if data:
                        results.append(data)
                except Exception as exc:
                    logger.info(f"{adapter} generated an exception: {exc}")
        return results

    def __fetch_data_from_adapter(
        self, adapter: BasePropertyAdapter, house_address: str
    ) -> PropertySchema:
        return adapter.get_property_by_address(house_address)
