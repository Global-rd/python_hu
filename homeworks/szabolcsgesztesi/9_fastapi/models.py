from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite adatbázis kapcsolat
DATABASE_URL = "sqlite:///homeworks/szabolcsgesztesi/9_fastapi/shop.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy adatbázis modell
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)

# Az adatbázis táblák létrehozása
Base.metadata.create_all(bind=engine)

# Pydantic modellek
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class ProductResponse(ProductCreate):
    id: str
