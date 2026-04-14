# Обновление данных

import psycopg2
from psycopg2 import Error
from db import create_connection

def update_review(review_id, new_rating=None, new_comment=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Проверка на существование отзыва
            cursor.execute('select rating, comment form reviews where id = %s', (review_id, ))
            existing = cursor.fetchone()

            if not existing:
                print('Отзыв не найден')
                return None

            # Формирование новых значений
            rating = new_rating if new_rating is not None else existing[0]
            comment = new_comment if new_comment is not None else existing[1]

            query = '''
                update reviews
                set rating = %s, comment = %s
                where id = %s
                returning id, rating, comment;
            '''

            cursor.execute(query, (new_rating, new_comment, review_id))
            updated = cursor.fetchone()

            connection.commit()

        except Error as err:
            print('Ошибка в запросе: ', err)
            connection.rollback()

        cursor.close()
        connection.close()