from pydantic import BaseModel, ConfigDict


class Provider1PropertySchemaFeatures(BaseModel):
    roomCount: int
    septicSystem: bool


class Provider1PropertySchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    formattedAddress: str
    squareFootage: int
    lotSizeSqFt: int
    yearBuilt: int
    propertyType: str
    bedrooms: int
    bathrooms: int
    features: Provider1PropertySchemaFeatures
    lastSalePrice: int
