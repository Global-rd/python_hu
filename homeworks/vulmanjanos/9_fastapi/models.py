import uuid
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional  # Importáljuk az Optional típust
from ws_database import Base

Base = declarative_base()

# Adatbázis modell

class Item(Base):
    __tablename__ = "items"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))   # Primary key beállítása
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String, index=True, nullable=True)  # Opcionális mező

# Pydantic modellek
class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None  # Opcionális mező

class ItemRead(ItemCreate):
    id: str

class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None  # Opcionális mező
