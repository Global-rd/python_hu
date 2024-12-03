from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

# DATABASE MODEL


class Product(Base):
    __tablename__ = "products"
    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[Optional[str]] = mapped_column(String, nullable=True)


class ProductRequest(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


class ProductResponse(ProductRequest):
    id: UUID
