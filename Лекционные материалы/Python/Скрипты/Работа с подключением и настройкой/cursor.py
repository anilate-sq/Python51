'''
Курсор - это объект, который выполняет SQL-запросы и получать их результаты;
'''

import psycopg2
from create_connect import create_connection

# Создание курсора
connection = create_connection()
cursor = connection.cursor()

# Выполнение запроса
cursor.execute('SELECT title, release_year FROM movies ORDER BY release_year DESC;')

movies = cursor.fetchall() # Преобразование данных в формат list(tuple)
for title, year in movies:
    print(f'{title} - {year}')

# [(title1, year1), (title2, year2), (title3, year3)]

cursor.close()
connection.close()

'''
Ключевые методы получения данных

cursor.fetchone() - возвращает первую попавшуюся запись кортежем
cursor.fetchmany(количесто_записей) - возвращает указанное количество строк списком кортежей
cursor.fetchall() - получение всех строк списком кортежей 
'''