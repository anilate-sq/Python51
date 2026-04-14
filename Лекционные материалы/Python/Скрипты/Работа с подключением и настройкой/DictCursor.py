# Настройка курсора
import psycopg2 # Импорт адаптера
import psycopg.extras # Для настройки курсора

connection = psycopg2.connect(
    # Указываем данные для подключения
    database = 'kilolib',
    user = 'postgres',
    password = '123',
    host = 'localhost',
    port = 5432
)

# Создаем курсор с DictCursor
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('SELECT title, release_year FROM movies WHERE id = 4;')
movie = cursor.fetchone()
print(f'Название: {movie['title']}\nГод выпуска: {movie['release_year']}')