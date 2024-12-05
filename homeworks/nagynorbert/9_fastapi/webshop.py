#Homework - Nagy Norbert
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from webshop_model import WebShopItem, WebShopItemRequest, WebShopItemResponse
from webshop_database import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/webshopitems/", response_model=List[WebShopItemResponse])
async def get_webshopitems(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShopItem))
    webshopitems = result.scalars().all()
    return webshopitems

@app.post("/webshopitems/", response_model=WebShopItemResponse)
async def add_webshopitem(item: WebShopItemRequest, db: AsyncSession = Depends(get_db)):
    new_item = WebShopItem(**item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

@app.get("/webshopitems/{item_id}", response_model=WebShopItemResponse)
async def get_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShopItem).where(WebShopItem.id == str(item_id)))
    item = result.scalar_one_or_none() 
    if not item:
        raise HTTPException(status_code=404, detail=f"Webshop itemid {item_id} is not found.")
    return item

@app.put("/webshopitems/{item_id}", response_model=WebShopItemResponse)
async def update_item(item_id: UUID, item_update: WebShopItemRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShopItem).where(WebShopItem.id == str(item_id)))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Webshop itemid {item_id} is not found.")

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

@app.delete("/webshopitems/{item_id}", response_model=WebShopItemResponse)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WebShopItem).where(WebShopItem.id == str(item_id)))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail=f"Webshop itemid {item_id} is not found.")
    
    await db.delete(item)
    await db.commit()
    return item