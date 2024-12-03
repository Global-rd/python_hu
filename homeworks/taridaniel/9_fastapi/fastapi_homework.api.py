from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models import Household_appliances, Household_appliances as Household_appliancesModel
from database import get_db, engine, Base
import uuid
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class HouseholdAppliancesCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class HouseholdAppliancesResponse(HouseholdAppliancesCreate):
    id: str

# List all products
@app.get("/products/", response_model=List[HouseholdAppliancesResponse])
async def read_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Household_appliancesModel).offset(skip).limit(limit))
    products = result.scalars().all()
    return products

# List one product by id
@app.get("/products/{product_id}", response_model=HouseholdAppliancesResponse)
async def read_product(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Household_appliancesModel).filter(Household_appliancesModel.id == product_id))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Add one product
@app.post("/products/", response_model=HouseholdAppliancesResponse)
async def create_product(product: HouseholdAppliancesCreate, db: AsyncSession = Depends(get_db)):
    new_product = Household_appliancesModel(id=str(uuid.uuid1()), **product.dict())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

# Update one product by id
@app.put("/products/{product_id}", response_model=HouseholdAppliancesResponse)
async def update_product(product_id: str, updated_product: HouseholdAppliancesCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Household_appliancesModel).filter(Household_appliancesModel.id == product_id))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in updated_product.dict().items():
        setattr(product, key, value)
    await db.commit()
    await db.refresh(product)
    return product

# Delete one product by id
@app.delete("/products/{product_id}")
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Household_appliancesModel).filter(Household_appliancesModel.id == product_id))
    product = result.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()
    return {"detail": "Product deleted"}


