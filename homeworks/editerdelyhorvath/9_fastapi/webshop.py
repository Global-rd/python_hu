# webshop.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from webshop_model import Product, ProductCreate, ProductUpdate, ProductResponse
from webshop_db import AsyncSessionLocal, engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event: create new DB
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown event: close the connection if needed

app = FastAPI(title="Webshop Product Register API", lifespan=lifespan)

# Dependency of a session handling
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# 1. List all prods
@app.get("/products/", response_model=List[ProductResponse])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    products = result.scalars().all()
    return products

# 2. List one prod by its ID
@app.get("/products/{product_id}", response_model=ProductResponse)
async def read_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Termék nem található")
    return product

# 3. Add new product
@app.post("/products/", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    try:
        await db.commit()
        await db.refresh(db_product)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Hiba történt a termék létrehozása során")
    return db_product

# 4. Update a product by its ID
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, product: ProductUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    db_product = result.scalar_one_or_none()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Termék nem található")
    
    for var, value in vars(product).items():
        if value is not None:
            setattr(db_product, var, value)
    
    try:
        await db.commit()
        await db.refresh(db_product)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Hiba történt a termék frissítése során")
    
    return db_product

# 5. Delete a product by its ID
@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    db_product = result.scalar_one_or_none()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Termék nem található")
    
    await db.delete(db_product)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Hiba történt a termék törlése során")
    
    return
