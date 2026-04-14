# Создание подключения к БД
import psycopg2 # Импорт адаптера
from psycopg2 import Error # Для ошибок

# Строка подключения
def create_connection():
    try:
        connection = psycopg2.connect(
            '''
            Синтаксис:
            database = имя_базы_данных,
            user = имя_пользователя (при работе с локалкой всегда postgres),
            password = ваш_пароль,
            host = адрес_сервера (при работе с локалкой всегда localhost/127.0.0.1),
            port = 5432
            '''

            # Указываем данные для подключения
            database = 'kilolib',
            user = 'postgres',
            password = '123',
            host = 'localhost',
            port = 5432
        )
        return connection

    except Error as err: 
        print('Ошибка: ', err)
        return None
