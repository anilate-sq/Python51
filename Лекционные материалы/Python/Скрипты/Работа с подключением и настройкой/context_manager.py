# Работа с контекстным менеджером
import psycopg2 # Импорт адаптера
from psycopg2 import Error # Для ошибок
from contextlib import contextmanager # Для работы с менеджером контекстов

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
        yield connection

        print('Потключение к базе данных установлено')
    except Error as err: 
        print('Ошибка: ', err)
        return None

    finally:
        if connection:
            connection.close()

# Использование контекстного менеджера        
with create_connection() as conn:
    # Тут выполняем запросы и проводим ключевые операции
    pass