/*
 DDL запросы:
 CREATE:
 - Назначение: Создание объектов(Базы данных, Схемы, Таблицы, Индексы и т.д.)
 - Синтаксис: CREATE <название_объекта>(
    Если это таблица, то нужно будет указывать её характеристики здесь
 );
 Создание таблицы: CREATE TABLE <название>(
    <название аттрибута/колонки> <тип данных> <ограничения, если они есть>
 );
*/

-- Пример создания базы данных
CREATE DATABASE "cinema"; -- Создание базы данных кинотеатр

-- Пример создания таблицы
CREATE TABLE "users"(
    id INT,
    full_name VARCHAR(100) NOT NULL,   
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL, -- +7(999)-152 16 71
    age INT,
    usermane VARCHAR(100) NOT NULL UNIQUE,
    "password" VARCHAR(40) NOT NULL     
);

/*
ALTER: 
- Назначение: Редактирование объектов
- Синтаксис: ALTER <объект> <название> <ADD, MODIFY, DROP> COLUMN <Полное описание колонки> 
*/

-- Пример редактирования таблиц
ALTER TABLE users ALTER COLUMN "age" type INT; --  Изменяю поле age: добавляю проверку на возраст
ALTER TABLE users ADD "address" VARCHAR(100) NOT NULL; -- Добавляю поле address 
ALTER TABLE users DROP "address";  -- Удаляю поле address

/*
  DROP:
  - Назначение: Удаление объекта
  - Синтаксис: DROP <объекта> <название>
*/

-- Пример удаления базы данных
DROP DATABASE cinema;

-- Пример удаления таблицы
DROP TABLE users;

-- Пример чистки
TRUNCATE TABLE users; -- Удалятся все записи из таблицы "users"