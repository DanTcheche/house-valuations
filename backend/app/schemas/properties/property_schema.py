from typing import Self
from app.schemas.properties.provider_1_property_schema import (
    Provider1PropertySchema,
)
from pydantic import BaseModel


class PropertySchema(BaseModel):
    id: str
    address: str
    square_footage: int
    lot_size: int
    year_built: int
    property_type: str
    bedrooms: int
    bathrooms: int
    room_count: int
    septic_system: bool
    sale_price: int

    @classmethod
    def from_provider_1(
        cls, provider_1_response: Provider1PropertySchema
    ) -> Self:
        return PropertySchema(
            id=provider_1_response.id,
            address=provider_1_response.formattedAddress,
            square_footage=provider_1_response.squareFootage,
            lot_size=provider_1_response.lotSizeSqFt,
            year_built=provider_1_response.yearBuilt,
            property_type=provider_1_response.propertyType,
            bedrooms=provider_1_response.bedrooms,
            bathrooms=provider_1_response.bathrooms,
            room_count=provider_1_response.features.roomCount,
            septic_system=provider_1_response.features.septicSystem,
            sale_price=provider_1_response.lastSalePrice,
        )

    @classmethod
    def from_provider_2(cls) -> Self: ...
