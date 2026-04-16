from db import Session, engine, Base
from models import Movie, Review, Genre

# Пример ручного создания таблицы
Base.metadata.create_all(bind=engine)

db = Session()

action = db.query(Genre).filter(Genre.name == "Action").first()
# =
# SELECT * from movies m JOIN movie_genres mg
# on mg.movie_id = m.id
# JOIN genres g on mg.genre_id = g.id
# WHERE g.name == "Action" LIMIT 1

scifi = db.query(Genre).filter(Genre.name == 'Sci-fi').first()

new_movie = Movie(
    title="Dune 2",
    description="in next time",
    release_year=2023,
    duration_minutes=175,
    genres=[action,scifi] 
)
db.add(new_movie)
db.commit()