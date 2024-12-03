from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

#DATABASE MODEL

class Household_appliances(Base):

    __tablename__ = "household appliances"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    title: Mapped[str] = Column(String, nullable=False)
    genre: Mapped[str] = Column(String, nullable=False)
    year: Mapped[int] = Column(Integer, nullable=False)
    length_in_mins: Mapped[int] = Column(Integer, nullable=False)
    rating: Mapped[int] = Column(Integer, nullable=False)

class Household_appliances(BaseModel):
    title: str
    genre: str
    year: int
    length_in_mins: int
    rating: Optional[int] = 0

class Household_appliances(ApplianceRequest):
    id: UUID
