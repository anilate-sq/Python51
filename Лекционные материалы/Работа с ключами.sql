-- Создание ключей и соединение таблиц

CREATE DATABASE 'online-courses';

/*
    Первичный ключ(PK) - ключевое поле и идентификатор записи, всегда уникальное;
    Способы создание:
    1. Напрямую в настройках поля;  
    2. Добавление в конце таблицы.

    P.s SERIAL - тип данных "счетчик", на 1 увеличивает значение в каждой новой записи
*/

BEGIN;

CREATE TABLE roles(
    id SERIAL PRIMARY KEY,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    password VARCHAR(45) NOT NULL,
    role_id INT REFERENCES roles(id) ON DELETE SET NULL -- Внешний ключ
    -- FOREIGN KEY(role_id) REFERENCES roles(id) -- Второй способ
);

INSERT INTO roles(name) VALUES ('Пользователь'), ('Преподаватель'), ('Администратор');
INSERT INTO users(full_name, email, password, role_id) VALUES('Соколов Иван Павлович', 'ivan@yandex.ru', '123', 1),
('Соколинский Владимир Олегович', 'vova@outlook.com', '123', 1),
('Соловьев Матвей Степанович', 'matvey@gmail.com', '123', 1),
('Бурлаков Никита Николаевич', 'nikita@gmail.com', '123', 2),
('Матвеева Дарья Сергеевная', 'dasha@outlook.com', '123', NULL),
('Григорьев Камиль Эдуардович', 'coma@yandex.ru', '123', 3);

COMMIT;