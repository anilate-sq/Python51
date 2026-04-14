# Удаление данных

import psycopg2
from psycopg2 import Error
from db import create_connection

connection = create_connection()
def drop_review(review_id):
    cursor = connection.cursor()
    if connection:
        try:

            # Проверка на наличие отзыва
            query = '''
                select m.title, r.rating, u.username
                from reviews r
                join movies m on r.movie_id = m.id
                join users u on r.user_id = u.id
                where r.id = %s
            '''
            cursor.execute(query, (review_id,))
            review = cursor.fetchone()

            if not review:
                print('Отзыв не найден')
                return False
            
            query = 'delete from reviews where id = %s returning id;'
            cursor.execute(query, (review_id,))
            cursor.fetchone()

            connection.commit()
            return True
        except Error as err:
            print('Ошибка в запросе: ', err)
            connection.rollback()
            return False
        cursor.close()
        connection.close()

drop_review(1) # Удаление отзыва с id = 1

            