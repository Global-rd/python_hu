from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import Mapped
from uuid import uuid1, UUID
from pydantic import BaseModel
from typing import Optional
from database import Base

#DATABASE MODEL

class Ws_item(Base):

    __tablename__ = "t_webshop"
    id: Mapped[str] = Column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = Column(String, nullable=False)
    quantity: Mapped[int] = Column(Integer, nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[str] = Column(String, nullable=True)

class WebshopRequest(BaseModel):
    item_name: str
    category: str
    quantity: int
    price: int
    category: Optional[str] = ""

class WebshopResponse(WebshopRequest):
    id: UUID
