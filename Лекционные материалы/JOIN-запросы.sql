
-- JOIN-запросы

/*

Основные виды:
1. INNER JOIN - возвращает все совпадения;
2. LEFT JOIN - возвращает все совпадения и все данные из левой таблицы(которая перед JOIN);
3. RIGHT JOIN - возвращает все совпадения и все данные из правой таблицы(которая после JOIN);
4. FULL JOIN - возвращает все совпадения и все данные из обоих таблиц(которая после JOIN).

Синтаксис: SELECT <поля> FROM <таблица1(левая)> JOIN <таблица2(правая)> ON <усвловие>;

*/

-- Просмотреть всех пользователей и их роли
SELECT users.id, full_name, name FROM users JOIN roles ON role_id = roles.id; -- INNER JOIN
SELECT u.id, u.full_name, r.name FROM users u LEFT JOIN roles r ON u.role_id = r.id; -- LEFT JOIN
SELECT u.id, u.full_name, r.name FROM users u RIGHT JOIN roles r ON u.role_id = r.id; -- RIGHT JOIN
SELECT u.id, u.full_name, r.name FROM users u FULL OUTER JOIN roles r ON u.role_id = r.id; -- FULL JOIN

-- Каскадное соединение

-- Получение информации о курсах и их преподавателях
SELECT c.name "Название курса", t.full_name "Преподаватель", tca.experience "Стаж преподавателя", c.price "Цена за курс", c.count_hours "Количество часов" FROM courses c
JOIN teacher_course tc ON tc.course_id = c.id
JOIN users t ON t.id = tc.teacher_id
JOIN teacher_card tca ON t.id = tca.user_id;

-- Получение списков предметов у преподавателей
SELECT t.full_name "Автор курса", c.name "Курс" FROM users t 
JOIN teacher_course tc ON tc.teacher_id = t.id
JOIN courses c ON  tc.course_id = c.id;