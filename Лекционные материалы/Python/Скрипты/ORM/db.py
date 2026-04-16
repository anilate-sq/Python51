from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


# Base - фундамент модели
Base = declarative_base()

# Строка подключения
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/kinolib'

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_connect():
    db = Session()
    try:
        yield db
    finally:
        db.close()