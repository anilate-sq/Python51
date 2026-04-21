from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Movie, Review
from schemas import MovieCreate
from dependencies import get_db

router = APIRouter(prefix='/movies', tags=['Movies'])

@router.post('/')
def create_movies(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.get('/')
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@router.get('/{movie_id}/reviews')
def get_reviews_by_movie(movie_id: int, db: Session = Depends(get_db)):
    return db.query(Review).filter(Review.movie_id == movie_id).all()