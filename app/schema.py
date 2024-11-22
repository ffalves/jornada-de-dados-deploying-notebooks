from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float

class ErrorResponse(BaseModel):
    Status: int
    Message: str
