from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models import Products, ProductsRequest, ProductsResponse 
from database import get_db, engine 



from database import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



app = FastAPI(on_startup=[init_db])

# 1.
@app.get("/products/", response_model=list[ProductsResponse])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products))
    products = result.scalars().all()
    return products

# 2.
@app.get("/products/{product_id}", response_model=ProductsResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Products).filter(Products.id == product_id))
        product = result.scalar_one()
        return product
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Product not found")

# 3.
@app.post("/products/", response_model=ProductsResponse)
async def create_product(product: ProductsRequest, db: AsyncSession = Depends(get_db)):
    new_product = Products(
        item_name=product.item_name,
        quantity=product.quantity,
        price=product.price,
        category=product.category
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

# 4.
@app.put("/products/{product_id}", response_model=ProductsResponse)
async def update_product(product_id: str, product_data: ProductsRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Products).filter(Products.id == product_id))
        product = result.scalar_one()
        product.item_name = product_data.item_name
        product.quantity = product_data.quantity
        product.price = product_data.price
        product.category = product_data.category
        await db.commit()
        await db.refresh(product)
        return product
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Product not found")

# 5.
@app.delete("/products/{product_id}", response_model=dict)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Products).filter(Products.id == product_id))
        product = result.scalar_one()
        await db.delete(product)
        await db.commit()
        return {"detail": "Product deleted successfully"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Product not found")
    