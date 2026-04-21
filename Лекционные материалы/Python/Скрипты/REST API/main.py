from fastapi import FastAPI, Depends
from routers import movies, reviews
app = FastAPI()

app.include_router(movies.router)
app.include_router(reviews.router)