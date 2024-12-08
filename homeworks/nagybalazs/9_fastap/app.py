from fastapi import FastAPI, HTTPException, Depends
from typing import List
from uuid import uuid1
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
from modell import Product, ProductCreate, ProductResponse


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(on_startup=[init_db])


@app.get("/products", response_model=List[ProductResponse])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.dict(), id=str(uuid1()))
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product: ProductCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    existing_product = result.scalars().first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict().items():
        setattr(existing_product, key, value)

    await db.commit()
    await db.refresh(existing_product)
    return existing_product


@app.delete("/products/{product_id}")
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(product)
    await db.commit()
    return {"detail": "Product deleted successfully"}
