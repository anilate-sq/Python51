from database import SessionLocal

# Создаем соединение с базой
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()