from fastapi import FastAPI, HTTPException, Depends # HTTPException: pl 404-es error ha a felhasználó updatelni próbál olyat ami nincs # Depends: a session hozzáadásához kell
from sqlalchemy.ext.asyncio import AsyncSession # Nincs szerepe, csak típusmegjelölésre, a kód olvashatóságához és a dokumentációkészítéshez használjuk
from sqlalchemy.future import select # Future?
from uuid import UUID
from contextlib import asynccontextmanager
from models import Staff, StaffRequest, StaffResponse
from database import Base, engine, get_db
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Allows the app to actually run after finish startup tasks

app = FastAPI(lifespan=lifespan)

""" DEPRECATED STARTUP FUNCTION WE USED ON THE LESSON, PLEASE USE lifespan above!
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
"""
# minden termék listázása
@app.get("/market/", response_model=List[StaffResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Staff))
    things = result.scalars().all()
    return things

# egy termék módosítása
@app.post("/market/", response_model=StaffResponse)
async def add_staff(staff: StaffRequest, db: AsyncSession = Depends(get_db)):
    new_staff = Staff(**staff.dict())
    db.add(new_staff)
    await db.commit()
    await db.refresh(new_staff)
    return new_staff

# egy termék listázása id alapján
@app.get("/market/{staff_id}", response_model=StaffResponse)
async def get_staff(staff_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Staff).where(Staff.id == str(staff_id)))
    staff = result.scalar_one_or_none() 
    if not staff: #guard clause
        raise HTTPException(status_code=404, detail=f"Staff id {staff_id} not found")
    return staff

# egy termék módosítása
@app.put("/market/{staff_id}", response_model=StaffResponse)
async def update_staff(staff_id: UUID, staff_update: StaffRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Staff).where(Staff.id == str(staff_id)))
    staff = result.scalar_one_or_none()
    if not staff: #guard clause
        raise HTTPException(status_code=404, detail=f"Staff id {staff_id} not found")

    for key, value in staff_update.model_dump(exclude_unset=True).items(): #instead of model_dump we used dict() on the lesson
        setattr(staff, key, value) # title update: title.value = "New Title" -> meovi.title = "New Title"

    db.add(staff)
    await db.commit()
    await db.refresh(staff)
    return staff

# egy termék törlése
@app.delete("/market/{staff_id}", response_model=StaffResponse)
async def delete_staff(staff_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Staff).where(Staff.id == str(staff_id)))
    staff = result.scalar_one_or_none()
    if not staff: #guard clause
        raise HTTPException(status_code=404, detail=f"Staff id {staff_id} not found")
    
    await db.delete(staff)
    await db.commit()
    return staff
