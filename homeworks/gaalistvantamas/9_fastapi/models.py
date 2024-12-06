"""
Author: Gaál István Tamás
Task: Homework-9
"""

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

#DATABASE Model

class Product(Base):
    
    __tablename__ = "Products"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)
    
class ProductRequest(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = "Not indentify"
    
class ProductResponse(ProductRequest):
    id: UUID

