import requests

# Задать адрес для отправки запросов
BASE_URL = 'https://jsonplaceholder.typicode.com'
response = requests.get(f'{BASE_URL}/posts')

# Проверка
if response.status_code == 200:
    posts = response.json() # Парсим JSON-объект в Python-объект
    print('Количество постов: ', len(posts))
    print('Посты: ', posts)

else:
    print(f'Ошибка {response.status_code}: {response.text}')


post = {
    'title': 'Тестовый пост',
    'body': 'Тестовый контент поста',
    'userId': 1
}

response = requests.post(
    f'{BASE_URL}/posts',
    json=post,
    timeout=10
)

if response.status_code == 201:
    create = response.json()
    print('Создан пост: ', create)

else:
    print(f'Не удалось создавать: {response.status_code}')