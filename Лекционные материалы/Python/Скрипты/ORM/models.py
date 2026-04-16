# Модели для базы данных `kinolib`

# Объекты для создания моделей
from sqlalchemy import(
    Table, Column, String, Integer, Float, Text, DateTime, Date,
    Boolean, ForeignKey, Index, CheckConstraint
)
# Создание отношений
from sqlalchemy.orm import relationship
# Встроенные функции и методы для настройки
from sqlalchemy.sql import func
# Подгружаем движок и подключение
from db import Base


# Пример создания модели
class Movie(Base):
    # Фильмы
    __tablename__ = 'movies'

    # Создаем поля
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    release_year = Column(Integer, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Создаем отношения
    genres = relationship("Genre", secondary="movie_genres", back_populates="movies")
    reviews = relationship("Review", back_populates="movie", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="movie", cascade="all, delete-orphan")

class Genre(Base):
    __table__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    movies = relationship("Movie", secondary='movie_genres', back_populates="genres")

movie_genres = Table(
    "movie_genres", Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id', ondelete='cascade'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id', ondelete='cascade'), primary_key=True),
)

class Review(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="cascade"))
    movie_id = Column(Integer, ForeignKey('movies.id'), ondelete="cascade")
    rating = Column(Integer, CheckConstraint('rating >= 1 and rating <= 10'), nullable=False)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="reviews")
    movie = relationship("Movie", back_populates="reviews")

    __table_args__ = (
        UniqueConstraint("user_id", "movie_id", name='uq_user_movie_review'),
    )

class Favorite(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id', ondelete='cascade'), primary_key=True)

    user = relationship("User", back_populates="favorites")
    movie = relationship("Movie", back_populates="favorites")