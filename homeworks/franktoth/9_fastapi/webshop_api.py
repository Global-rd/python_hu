from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Item, ItemRequest, ItemResponse
from database import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to actually run after finish startup tasks

app = FastAPI(lifespan=lifespan)


@app.get("/items/", response_model=List[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    items = result.scalars().all()
    return items


@app.post("/items/", response_model=ItemResponse)
async def add_item(item: ItemRequest, db: AsyncSession = Depends(get_db)):
    new_item = Item(**item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == str(item_id)))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")
    return item


@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: UUID, item_update: ItemRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == str(item_id)))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    for key, value in item_update.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/items/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == str(item_id)))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    await db.delete(item)
    await db.commit()
    return item