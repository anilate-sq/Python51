# Создание подключения к БД
import psycopg2 # Импорт адаптера
from psycopg2 import Error # Для ошибок

# Строка подключения
def create_connection():
    try:
        connection = psycopg2.connect(
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
