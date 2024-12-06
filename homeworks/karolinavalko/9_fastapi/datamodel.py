from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from databaseapiendpoint import Base

class Products(Base):

    __tablename__ = "webshop"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[str] = Column(String, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    category: Mapped[int] = Column(Integer, nullable=False)
    

class ProductsRequest(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[int] = 0

class ProductsResponse(ProductsRequest):
    id: UUID