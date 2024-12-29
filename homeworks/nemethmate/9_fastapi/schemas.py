from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str

    class Config:
        orm_mode = True
