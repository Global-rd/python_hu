from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL for SQLite, using 'aiosqlite' for asynchronous operations.
DATABASE_URL = "sqlite+aiosqlite:///./products.db"

# Create an asynchronous database engine for connecting to SQLite.
engine = create_async_engine(DATABASE_URL, echo=True)  # `echo=True` logs SQL queries.

# Configure a sessionmaker to manage database sessions. 
# `expire_on_commit=False` ensures data stays accessible after a commit.
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for defining ORM models. All models will inherit from this.
Base = declarative_base()

# Dependency to get a database session for each request.
# Uses a context manager to ensure the session is properly closed.
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
