from sqlalchemy import Column, String, Integer, Float
from database import Base
from pydantic import BaseModel
from typing import Optional

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)


class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


class ProductResponse(ProductCreate):
    id: str
