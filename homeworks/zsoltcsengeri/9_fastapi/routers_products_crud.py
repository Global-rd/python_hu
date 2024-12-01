from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from schemas_products_pydantic import Product, ProductRequest, ProductResponse
from database_products_sqlite import Base, engine, get_db
from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to actually run after finish startup tasks


app = FastAPI(lifespan=lifespan)


@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))  # SELECT * FROM products
    products = result.scalars().all()
    return products


@app.post("/products/", response_model=ProductResponse)
async def add_product(product: ProductRequest, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:  # guard clause
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found"
        )
    return product


@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID, product_update: ProductRequest, db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:  # guard clause
        raise HTTPException(
            status_code=404, detail=f"product id {product_id} not found"
        )

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not print: #guard clause
        raise HTTPException(status_code=404, detail=f"Product id {product_id} not found")
    
    await db.delete(product)
    await db.commit()
    return product
