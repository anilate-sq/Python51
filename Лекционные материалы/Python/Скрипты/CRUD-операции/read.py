# Операции чтения данных

import psycopg2
from psycopg2 import Error
from db import create_connection

# Функция для получения всех фильмов
def select_movies():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
                select id, title, release_year, duration_minutes
                from movies
                order by release_year desc; 
            '''

            cursor.execute(query)
            movies = cursor.fetchall()
            for movie in movies:
                print(f'{movie[0]} {movie[1]}, {movie[2]}, {movie[3]}')

            return movies
        
        except Error as err:
            print('Ошибка запроса: ', err)
        
        cursor.close()
        connection.close()

def get_user_reviews(user_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
                select m.title, r.rating, r.comment, r.created_at
                from reviews r
                join movies m on r.movie_id = m.id
                where r.user_id = %s
                order by r.created_at desc;
            '''
            
            cursor.execute(query, (user_id,))
            reviews = cursor.fetchall()

            # Получение имени пользователя
            cursor.execute('select username from users where id = %s', (user_id))
            username = cursor.fetchone()

            if username:
                print('Отзыв пользователя: ', {username[0]})

                if reviews:
                    for review in reviews:
                        print(f'Фильм: {review[0]}')
                        print(f'Оценка: {review[1]}/10')
                        print(f'Комментарий: {review[2]}')
                        print(f'Дата: {review[3]}')

                else:
                    print('Отзывов пока что нету')

            return reviews
        
        except Error as err:
            print('Ошибка запроса: ', err)

        cursor.close()
        connection.close()


get_user_reviews(4)