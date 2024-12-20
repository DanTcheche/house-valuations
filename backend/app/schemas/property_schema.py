from pydantic import BaseModel

class PropertySchema(BaseModel):
    id: int
    address: str
    square_footage: int
    lot_size: float
    year_built: int
    property_type: str
    bedrooms: int
    bathrooms: int
    room_count: int
    septic_system: bool
    sale_price: float
