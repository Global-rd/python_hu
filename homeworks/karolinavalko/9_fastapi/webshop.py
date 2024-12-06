from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from datamodel import Products, ProductsRequest, ProductsResponse
from databaseapiendpoint import Base, engine, get_db
from typing import List



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 

app = FastAPI(lifespan=lifespan)


@app.get("/mainwebshop/", response_model=List[ProductsResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products)) 
    webshop_products = result.scalars().all()
    return webshop_products


@app.post("/mainwebshop/", response_model=ProductsResponse)
async def add_product(product: ProductsRequest, db: AsyncSession = Depends(get_db)):
    new_product = Products(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@app.get("/mainwebshop/{product_id}", response_model=ProductsResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == str(product_id)))
    webshop_products = result.scalar_one_or_none() 
    if not webshop_products: 
        raise HTTPException(status_code=404, detail=f"Product id {product_id} cannot be found")
    return webshop_products

@app.put("/mainwebshop/{product_id}", response_model=ProductsResponse)
async def update_webshop(product_id: UUID, product_update: ProductsRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == str(product_id)))
    webshop_products = result.scalar_one_or_none()
    if not webshop_products: 
        raise HTTPException(status_code=404, detail=f"Product id {product_id} cannot be found")
    
    for key, value in update_webshop.model_dump(exclude_unset=True).items(): 
        setattr(webshop_products, key, value) 

    db.add(webshop_products)
    await db.commit()
    await db.refresh(webshop_products)
    return webshop_products

@app.delete("/mainwebshop/{product_id}", response_model=ProductsResponse)
async def delete_prooduct(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == str(product_id)))
    update_webshop = result.scalar_one_or_none()
    if not update_webshop:
        raise HTTPException(status_code=404, detail=f"Product id {product_id} cannot be found")
    
    await db.delete(update_webshop)
    await db.commit()
    return update_webshop