from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from typing import List
from ws_database import engine, get_session
from models import Base, ItemCreate, ItemRead, ItemUpdate, Item

app = FastAPI()

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to actually run after finish startup tasks

app = FastAPI(lifespan=lifespan)

# CRUD endpointjaim

# Terméklistázás
@app.get("/items", response_model=List[ItemRead])
async def list_items(session: AsyncSession = Depends(get_session)):
    # Az összes termék lekérdezése database-ből
    result = await session.execute(select(Item))
    items = result.scalars().all()
    return items

# Terméklistázás ID alapján
@app.get("/items/{item_id}", response_model=ItemRead)
async def get_item(item_id: str, session: AsyncSession = Depends(get_session)):
    # Lekérdezés azonosító alapján
    result = await session.execute(select(Item).filter_by(id=item_id))
    item = result.scalar_one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Termékhozzáadás
@app.post("/items", response_model=ItemRead)
async def create_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    # A hozzáadás:
    new_item = Item(**item.dict())
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item

# Termék adatafrissítés ID alapján
@app.put("/items/{item_id}", response_model=ItemRead)
async def update_item(item_id: str, item: ItemUpdate, session: AsyncSession = Depends(get_session)):
    # A frissítés
    result = await session.execute(select(Item).filter_by(id=item_id))
    existing_item = result.scalar_one_or_none()
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(existing_item, key, value)
    await session.commit()
    await session.refresh(existing_item)
    return existing_item

# Terméktörlés ID alapján
@app.delete("/items/{item_id}", response_model=ItemRead)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_session)):
    # A törlés
    result = await session.execute(select(Item).filter_by(id=item_id))
    item = result.scalar_one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    await session.delete(item)
    await session.commit()
    return item

