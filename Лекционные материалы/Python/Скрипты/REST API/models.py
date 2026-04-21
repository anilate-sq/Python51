# Модели для базы данных `kinolib`

# Объекты для создания моделей
from sqlalchemy import(
    Table, Column, String, Integer, Float, Text, DateTime, Date,
    Boolean, ForeignKey, Index, CheckConstraint, UniqueConstraint
)
# Создание отношений
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

# Пример создания модели
class Movie(Base):
    # Фильмы
    __tablename__ = 'movies'

    # Создаем поля
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    description = Column(Text)
    release_year = Column(Integer)

    # Создаем отношения
    reviews = relationship("Review", back_populates="movie")

class Review(Base):
    # Отзывы
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer)
    comment = Column(Text)

    movie = relationship("Movie", back_populates="reviews")