from sqlalchemy import Column, String, Integer, Float, Text
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from webshop_database import Base

# Database modell

class Product(Base):

    __tablename__ = "products"
    id: Mapped[str]= Column(String, primary_key=True, default=lambda: str(uuid1())) 
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[Text] = Column(Text, nullable=False)

# Pydentic modell

class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = 0

class ProductResponse(ProductBase):
    id: UUID