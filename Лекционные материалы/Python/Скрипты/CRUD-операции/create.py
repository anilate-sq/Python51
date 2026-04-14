# Добавление данных в БД

import psycopg2
from psycopg2 import Error
from db import create_connection

# Функция для добавления нового пользователя
def add_user(username, email, password_hash):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Запрос на добавление
            query = '''
                insert into users(username, email, password_hash) values (%s, %s, %s)
                RETURNING id, username, email, created_at;
                '''
            cursor.execute(query, (username, email, password_hash))

            # Получение информации о добавленном пользователе
            new_user = cursor.fetchone()

            connection.commit() # Фиксируем обновления в БД

        except Error as err:
            print(f'Ошибка в запросе: ', err)
            connection.rollback() # Откат изменений

        cursor.close()
        connection.close()

# Реализация добавления
add_user('user_name', 'user_email@mail.r', 'hashed_password_123')

# Функция для добавления фильма с жанрами
def add_movie_with_genre(title, description, release_year, duration_minutes, genre_names):
    connection = create_connection()

    if connection:
        try:
            cursor = connection.cursor()

            # Добавление фильма
            movie_query = '''
                insert into movies (title, description, release_year, duration_minutes)
                values(%s, %s, %s, %s)
                RETURNING id;
            '''

            cursor.execute(movie_query, (title, description, release_year, duration_minutes))
            movie_id = cursor.fetchone()[0] # Получаю значение id

            # Связь с жанрами
            genre_query = '''
                insert into movie_genre(movie_id, genre_id)
                select %s, id from genres where name = %s
            '''

            for genre_name in genre_names:
                cursor.execute(genre_query, (movie_id, genre_name))
            
            connection.commit()
            print(f'Фильм {title}, добавлен с id: {movie_id}')
            return movie_id
        
        except Error as err:
            print('Ошибка выполнения запроса: ', {err})
            connection.rollback()

        cursor.close()
        connection.close

# Добавление фильма с жанрами
add_movie_with_genre(
    'Tenet',
    'Time inversion',
    2020,
    150,
    ['Action', 'Sci-Fi', 'Thriller']
)

# Добавление нескольких записей на примере таблицы `users`

users = [
    ('user_name_1', 'user_email@mail.ru_1', 'hashed_password_123'),
    ('user_name_2', 'user_email@mail.ru_2', 'hashed_password_123'),
    ('user_name_3', 'user_email@mail.ru_3', 'hashed_password_123'),
]
