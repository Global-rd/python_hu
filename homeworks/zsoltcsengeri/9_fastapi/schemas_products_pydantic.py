from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID  # `uuid1` generates unique IDs, `UUID` is the type.
from pydantic import BaseModel
from typing import Optional
from database_products_sqlite import Base  # Import the Base class for ORM models.

# DATABASE MODEL: Represents the "products" table in the database.
class Product(Base):
    __tablename__ = "products"  # Name of the table in the database.

    # Columns in the "products" table.
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    # `id` is a primary key stored as a string, generated using UUID v1.
    
    item_name: Mapped[str] = Column(String, nullable=False)
    # Name of the product (cannot be null).
    
    price: Mapped[int] = Column(Integer, nullable=False)
    # Price of the product (must be an integer and cannot be null).
    
    category: Mapped[str] = Column(String, nullable=False)
    # Category of the product (cannot be null).

# REQUEST SCHEMA: Defines the expected structure of the request body for creating/updating products.
class ProductRequest(BaseModel):
    item_name: str  # Required: Name of the product.
    price: int      # Required: Price of the product.
    category: Optional[str]  # Optional: Category of the product.

# RESPONSE SCHEMA: Defines the structure of the response, including the `id`.
class ProductResponse(ProductRequest):
    id: UUID  # The `id` is returned as a UUID.
