from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine # sqlalchemy.ext.asyncio: az adatbázis műveletek (pl. request) teljesen külön session-ben kerülnek lekezelésre, nem fog összeakadni mással
from sqlalchemy.orm import sessionmaker, declarative_base # sqlalchemy.orm: object relational mapping -> azét felel, hogy object-ek automatikusan bekerüljenek az adatbázisba mint sorok és oszlopok # declarative_base: ahhoz kell, hogy a modell a pydentic validation-től örökölni tudjon

DATABASE_URL = "sqlite+aiosqlite:///./market.db"

engine = create_async_engine(DATABASE_URL, echo=True) # létrehozza az adatbázis connection-t # echo=True: visszajelzi a futtatott querry-ket a terminálon
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False) # expire_on_commit=False: miután kommitltunk, az adatok benne maradnak a memóriában és tudjuk őket használni
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session