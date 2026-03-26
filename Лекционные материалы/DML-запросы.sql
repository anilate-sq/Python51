/*
DML(Data Manipulation Language) - запросы для управления данными внутри БД.

Основные запросы:
1. SELECT:
    - Назначение: Просмотр/Выборка данных;
    - Синтаксис:  SELECT <поля> FROM <таблица>.
2. INSERT:
    - Назначение: Добавление данных/записей;
    - Синтаксис: INSERT INTO <таблица> VALUES(<поле_1>, <поле_2>, ..., <поле_n>);

3. UPDATE:
    - Назначение: Обновление/Редактирование данных
    - Синтаксис: UPDATE <таблица> SET <колонка> = <значение> WHERE <условия для обновления>;

4. DELETE:
    - Назначение: Удаление записей;
    - Синтаксис: DELETE FROM <таблица> WHERE <условие для удаления>
*/

-- Пример просмотра данных
SELECT name, price FROM items; -- Получение информации о названии и цене продуктов
SELECT name, price, category FROM items; -- Получение информации о названии, цене и категории продуктов
SELECT * FROM items; -- Получение всей информации о продуктах

-- Примеры добавления данных

-- Добавляем данные в каждое поле в таблице users в порядке
INSERT INTO users VALUES (1, 'Петров Иван Сергеевич', 'vanya@yandex.ru', '+7(912)-342 17 12', 14, 'vanya', 'qwe');

INSERT INTO users(full_name, id, age, username, password, email, phone) VALUES('Степанов Григорий Олегович', 2, 17 ,'grisha', '123', 'grisha@gmail.com', '+7(922)-645 19 21')

-- INSERT INTO users(full_name, username, password, phone) VALUES ...; - можно заполнять только определенные поля

-- Примеры редактирования/обновления данных
UPDATE users SET email = 'vanya@gmail.com' WHERE username = 'vanya'; -- Обновление почты у пользователя с логином "vanya"

UPDATE users SET email = 'grisha@yandex.ru', age = age + 1 WHERE full_name = 'Степанов Григорий Олегович'; -- Обновление почты и возраста пользователя с именем "Степанов Григорий Олегович"

-- Примеры удаления данных

DELETE FROM users WHERE username = 'vanya'; -- Удаление пользователя с логином 'vanya'

DELETE FROM users; -- Удаление всех пользователей
TRUNCATE TABLE users; -- Чистка таблицы