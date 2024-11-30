from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from contextlib import asynccontextmanager
from models import Movie, MovieRequest, MovieResponse
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

@app.get("/movies/", response_model=List[MovieResponse])
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie)) #SELECT * FROM movies
    movies = result.scalars().all()
    return movies

@app.post("/movies/", response_model=MovieResponse)
async def add_movie(movie: MovieRequest, db: AsyncSession = Depends(get_db)):
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)
    return new_movie

@app.get("/movies/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none() 
    if not movie: #guard clause
        raise HTTPException(status_code=404, detail=f"Movie id {movie_id} not found")
    return movie

@app.put("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: UUID, movie_update: MovieRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none()
    if not movie: #guard clause
        raise HTTPException(status_code=404, detail=f"Movie id {movie_id} not found")

    for key, value in movie_update.model_dump(exclude_unset=True).items(): #instead of model_dump we used dict() on the lesson
        setattr(movie, key, value) # title update: title.value = "New Title" -> meovi.title = "New Title"

    db.add(movie)
    await db.commit()
    await db.refresh(movie)
    return movie

@app.delete("/movies/{movie_id}", response_model=MovieResponse)
async def delete_movie(movie_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == str(movie_id)))
    movie = result.scalar_one_or_none()
    if not movie: #guard clause
        raise HTTPException(status_code=404, detail=f"Movie id {movie_id} not found")
    
    await db.delete(movie)
    await db.commit()
    return movie