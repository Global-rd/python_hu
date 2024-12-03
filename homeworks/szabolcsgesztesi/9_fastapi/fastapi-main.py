from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid1, UUID
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# FastAPI app létrehozása
app = FastAPI()

# SQLite adatbázis kapcsolat
DATABASE_URL = "sqlite:///homeworks/szabolcsgesztesi/9_fastapi/shop.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Adatbázis modell
class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    item_name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=True)

# Az adatbázis táblák létrehozása
Base.metadata.create_all(bind=engine)

# Pydantic modell az API-hoz
class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class ProductResponse(ProductCreate):
    id: UUID

# Helper függvény az adatbázis kezeléshez
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint-ok
@app.get("/products", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return [ProductResponse(**prod.__dict__) for prod in products]

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse(**product.__dict__)

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_id = str(uuid1())
    new_product = Product(id=product_id, **product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductResponse(**new_product.__dict__)

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, product: ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(existing_product, key, value)
    db.commit()
    db.refresh(existing_product)
    return ProductResponse(**existing_product.__dict__)

@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}