from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import AsyncGenerator


# Adatbázis URL beállítása (SQLite használata)
DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

# Aszinkron adatbázis engine létrehozás
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

# Aszinkron session létrehozás
LocalSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base osztály adatbázis modellekhez
Base = declarative_base()

# Aszinkron session függvény
async def get_session() ->  AsyncGenerator[AsyncSession, None]:
    async with LocalSession() as session:
        yield session