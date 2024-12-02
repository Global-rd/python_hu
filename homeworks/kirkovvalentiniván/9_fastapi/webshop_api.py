from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from contextlib import asynccontextmanager
from webshop_db import Base, engine, get_db
from webshop_models import Product, ProductRequest, ProductResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

# Endpoints
@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductResponse, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@app.get("/products", response_model=list[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, updates: ProductRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    
    await db.commit()
    await db.refresh(product)
    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    await db.delete(product)
    await db.commit()
    return {"message": "Product deleted successfully"}
