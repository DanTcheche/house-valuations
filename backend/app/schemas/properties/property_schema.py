from typing import Self
from app.schemas.properties.provider_1_property_schema import (
    Provider1PropertySchema,
)
from app.schemas.properties.provider_2_property_schema import (
    Provider2PropertySchema,
)
from pydantic import BaseModel


ACRES_IN_FEET = 43560


class PropertySchema(BaseModel):
    id: str
    provider: str
    address: str
    square_footage: int
    lot_size_acres: float
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
            provider="Provider 1",
            address=provider_1_response.formattedAddress,
            square_footage=provider_1_response.squareFootage,
            lot_size_acres=provider_1_response.lotSizeSqFt / ACRES_IN_FEET,
            year_built=provider_1_response.yearBuilt,
            property_type=provider_1_response.propertyType,
            bedrooms=provider_1_response.bedrooms,
            bathrooms=provider_1_response.bathrooms,
            room_count=provider_1_response.features.roomCount,
            septic_system=provider_1_response.features.septicSystem,
            sale_price=provider_1_response.lastSalePrice,
        )

    @classmethod
    def from_provider_2(
        cls, provider_2_response: Provider2PropertySchema
    ) -> Self:
        return PropertySchema(
            id=provider_2_response.ID,
            provider="Provider 2",
            address=provider_2_response.NormalizedAddress,
            square_footage=provider_2_response.SquareFootage,
            lot_size_acres=provider_2_response.LotSizeAcres,
            year_built=provider_2_response.YearConstructed,
            property_type=provider_2_response.PropertyType,
            bedrooms=provider_2_response.Bedrooms,
            bathrooms=provider_2_response.Bathrooms,
            room_count=provider_2_response.RoomCount,
            septic_system=provider_2_response.SepticSystem,
            sale_price=provider_2_response.LastSalePrice,
        )
