from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Ws_item, WebshopRequest, WebshopResponse
from database import Base, engine, get_db
from typing import List

@asynccontextmanager

async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to actually run after finish startup tasks

app = FastAPI(lifespan=lifespan)

# --------------------------------------------------------------------------------------
@app.get("/t_webshop/", response_model=List[WebshopResponse])

async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Ws_item)) #SELECT * FROM 
    L_items = result.scalars().all()
    return L_items

# --------------------------------------------------------------------------------------
@app.post("/t_webshop/", response_model=WebshopResponse)

async def add_product(L_item: WebshopRequest, db: AsyncSession = Depends(get_db)):
    new_item = Ws_item(**L_item.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item

# --------------------------------------------------------------------------------------
@app.get("/t_webshop/{item_id}", response_model=WebshopResponse)

async def get_product(item_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Ws_item).where(Ws_item.id == str(item_id)))
    L_item = result.scalar_one_or_none() 
    if not L_item: #guard clause
        raise HTTPException(status_code=404, detail=f"Product:{item_id} not found")
    return L_item

# --------------------------------------------------------------------------------------
@app.put("/t_webshop/{item_id}", response_model=WebshopResponse)

async def update_item(item_id: UUID, item_update: WebshopRequest, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Ws_item).where(Ws_item.id == str(item_id)))
    L_item = result.scalar_one_or_none()
    if not L_item: #guard clause
        raise HTTPException(status_code=404, detail=f"Product:{item_id} not found")

    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(L_item, key, value)

    db.add(L_item)
    await db.commit()
    await db.refresh(L_item)
    return L_item

# --------------------------------------------------------------------------------------
@app.delete("/t_webshop/{item_id}", response_model=WebshopResponse)

async def delete_product(item_id: UUID, db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Ws_item).where(Ws_item.id == str(item_id)))
    L_item = result.scalar_one_or_none()
    if not L_item: #guard clause
        raise HTTPException(status_code=404, detail=f"Product:{item_id} not found")

    await db.delete(L_item)
    await db.commit()
    return L_item

# cd python_hu\homeworks\valitothattila\9_fastapi
# uvicorn webshop_api:app --reload