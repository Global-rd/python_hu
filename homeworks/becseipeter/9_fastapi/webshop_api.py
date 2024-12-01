from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from webshop_mopdels import Product, ProductBase, ProductResponse
from webshop_database import Base, engine, get_db
from typing import List

app = FastAPI()   

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
   
   
##########################################  Endpoints  ########################################################    

#Listing all products

@app.get("/products/", response_model=List[ProductResponse])
async def get_product(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product)) 
    product = result.scalars().all()
    return product


#List one product by id

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none() 
    if not product: 
        raise HTTPException(status_code=404, detail=f"Product id {product_id} not found")
    return product


#Add a new product

@app.post("/products/", response_model=ProductResponse)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


#Updating the data of one product based on id

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, product: ProductBase, db: AsyncSession = Depends(get_db)):
    existing_product = await db.execute(Product).where(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_product.item_name = product.item_name
    existing_product.quantity = product.quantity
    existing_product.price = product.price
    existing_product.category = product.category
    
    db.add(product)
    await db.commit()
    await db.refresh(existing_product)
    return existing_product


#Delete one product based on id

@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(product)
    await db.commit()
    return {"message": "Product deleted successfully"}