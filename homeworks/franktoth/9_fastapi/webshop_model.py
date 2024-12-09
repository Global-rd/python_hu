from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from webshop_db import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)


class ItemRequest(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


class ItemResponse(ItemRequest):
    id: UUID