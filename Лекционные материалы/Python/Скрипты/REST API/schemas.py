from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    description: str
    release_year: int

class ReviewCreate(BaseModel):
    user_id: int
    movie_id: int
    rating: int
    comment: str | None = None