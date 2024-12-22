from pydantic import BaseModel, ConfigDict


class Provider2PropertySchema(BaseModel):
    model_config = ConfigDict(extra="allow")
    ID: str
    NormalizedAddress: str
    SquareFootage: int
    LotSizeAcres: float
    YearConstructed: int
    ArchitecturalStyle: str
    Bedrooms: int
    Bathrooms: int
    RoomCount: int
    LastSalePrice: int
    SepticSystem: bool
