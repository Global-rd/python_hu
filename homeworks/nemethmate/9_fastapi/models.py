from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid1()))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)
