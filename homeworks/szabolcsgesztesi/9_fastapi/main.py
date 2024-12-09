from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List  # Helyes import a List típushoz
from uuid import uuid1, UUID  # Az UUID importálása
from models import Product, ProductCreate, ProductResponse, SessionLocal

# FastAPI app létrehozása
app = FastAPI()

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
    new_product = Product(id=str(uuid1()), **product.dict())
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
