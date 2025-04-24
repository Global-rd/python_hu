from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from webshop_db import Base

# DataBase model

class Product(Base):

    __tablename__ = "products"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[Optional[str]] = Column(String, nullable=True)

class ProductBase(BaseModel):
    item_name: str 
    quantity: int 
    price: float 
    category: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    item_name: Optional[str] 
    quantity: Optional[int]
    price: Optional[float] 
    category: Optional[str] = "BaseCategory"

class ProductResponse(ProductBase):
    id: UUID

    class Config:
        orm_mode = True
