from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID # egyedi azonosító, akkor is ha több szerveren fut több alkalmazáspéldány
from pydantic import BaseModel #
from typing import Optional #
from database import Base

#DATABASE MODEL

class Staff(Base):

    __tablename__ = "market"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    category: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[int] = Column(Integer, nullable=False)
    
class StaffRequest(BaseModel): # pydentic
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = ""

class StaffResponse(StaffRequest):
    id: UUID