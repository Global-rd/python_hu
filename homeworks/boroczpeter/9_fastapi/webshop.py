from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel, UUID4
from database import get_db, engine
from product_models import Product

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Product.metadata.create_all, checkfirst=True)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = "Uncategorized"

class ProductCreate(ProductBase):
    quantity: int
    price: float

    @classmethod
    def validate(cls, value):
        assert value.quantity >= 0, "Quantity cannot be negative."
        assert value.price >= 0, "Price cannot be negative."

class ProductResponse(ProductBase):
    id: UUID4

    class Config:
        orm_mode = True

@app.get("/products", response_model=List[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product))
    products = result.scalars().all()
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID4, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter_by(id=product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID4, updated_product: ProductCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter_by(id=str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in updated_product.dict(exclude_unset=True).items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: UUID4, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).filter_by(id=str(product_id)))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()
    return {"message": "Product deleted successfully"}