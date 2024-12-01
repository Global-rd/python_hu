from fastapi import FastAPI, HTTPException, Depends  # Core FastAPI components.
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select  # For SQL SELECT queries.
from uuid import UUID  # UUID type for handling unique identifiers.
from contextlib import asynccontextmanager  # For managing app lifespan events.
from schemas_products_pydantic import Product, ProductRequest, ProductResponse  # Import schemas.
from database_products_sqlite import Base, engine, get_db
from typing import List  # For specifying response models with lists.

# Lifespan manager to handle app startup and shutdown tasks.
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # Create the database tables during app startup.
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to run after finishing startup tasks.

# FastAPI app instance with lifespan manager.
app = FastAPI(lifespan=lifespan)

# Endpoint to list all products.
@app.get("/products/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    # Query the database for all products.
    result = await db.execute(select(Product))  # SELECT * FROM products
    products = result.scalars().all()  # Retrieve all rows as Product objects.
    return products  # Return the list of products.

# Endpoint to add a new product.
@app.post("/products/", response_model=ProductResponse)
async def add_product(product: ProductRequest, db: AsyncSession = Depends(get_db)):
    # Create a new Product object from the request body.
    new_product = Product(**product.model_dump())  # `model_dump` converts Pydantic model to a dictionary.
    db.add(new_product)  # Add the product to the database session.
    await db.commit()  # Commit the transaction to save changes.
    await db.refresh(new_product)  # Refresh the object with database-generated values (e.g., `id`).
    return new_product  # Return the created product.

# Endpoint to fetch a product by ID.
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    # Query the database for the product with the given ID.
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()  # Get one row or return None if not found.
    if not product:  # Guard clause for missing product.
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found"
        )
    return product  # Return the found product.

# Endpoint to update a product by ID.
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID, product_update: ProductRequest, db: AsyncSession = Depends(get_db)
):
    # Query the database for the product with the given ID.
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:  # Guard clause for missing product.
        raise HTTPException(
            status_code=404, detail=f"product id {product_id} not found"
        )

    # Update only the provided fields in the product.
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)  # Dynamically update attributes.

    db.add(product)  # Add the updated product to the session.
    await db.commit()  # Commit the changes.
    await db.refresh(product)  # Refresh the object with the latest data.
    return product  # Return the updated product.

# Endpoint to delete a product by ID.
@app.delete("/products/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    # Query the database for the product with the given ID.
    result = await db.execute(select(Product).where(Product.id == str(product_id)))
    product = result.scalar_one_or_none()
    if not product:  # Guard clause for missing product.
        raise HTTPException(
            status_code=404, detail=f"Product id {product_id} not found"
        )

    await db.delete(product)  # Delete the product from the database.
    await db.commit()  # Commit the changes.
    return product  # Return the deleted product.
