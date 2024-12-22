from pydantic import BaseModel

class GetHouseValuationsRequest(BaseModel):
    address: str
