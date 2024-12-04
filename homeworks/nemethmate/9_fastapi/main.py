from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from .models import Item, Base
from .schemas import ItemBase, ItemCreate

app = FastAPI()

# Adatbázis kapcsolat létrehozása (példa SQLAlchemy használatával)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///./test.db')
Base.metadata.create_all(bind=engine)

# Endpoint-ok
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate):
    # Új elem létrehozása az adatbázisban
    db_item = Item(item_name=item.item_name, quantity=item.quantity, price=item.price, category=item.category)
    db.session.add(db_item)
    db.session.commit()
    return db_item

@app.get("/items/", response_model=list[Item])
def read_items():
    # Minden elem lekérése az adatbázisból
    items = db.session.query(Item).all()
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # Egy elem lekérése az adatbázisból az ID alapján
    item = db.session.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item