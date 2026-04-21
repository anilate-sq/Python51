from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Review
from schemas import ReviewCreate
from dependencies import get_db

router = APIRouter(prefix='/reviews', tags=['Reviews'])

@router.get('/')
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()

@router.post('/')
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review