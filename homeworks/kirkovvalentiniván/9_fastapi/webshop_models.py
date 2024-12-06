from sqlalchemy import Column, String, Integer, Float, Text
from sqlalchemy.orm import Mapped
from webshop_db import Base
from pydantic import BaseModel
from typing import Optional
from uuid import uuid1, UUID

class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[Text] = Column(Text, nullable=True)

class ProductRequest(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[Text] = None

    model_config = {"arbitrary_types_allowed": True}

class ProductResponse(ProductRequest):
    id: UUID

    class Config:
        orm_mode = True 