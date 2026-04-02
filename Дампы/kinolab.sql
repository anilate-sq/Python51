BEGIN;

-- =========================
-- USERS & AUTH
-- =========================

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE permissions (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE user_roles (
    user_id BIGINT NOT NULL,
    role_id BIGINT NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);

CREATE TABLE role_permissions (
    role_id BIGINT NOT NULL,
    permission_id BIGINT NOT NULL,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(id) ON DELETE CASCADE
);

-- =========================
-- MOVIES CORE
-- =========================

CREATE TABLE movies (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year INTEGER,
    duration_minutes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE genres (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE movie_genres (
    movie_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- =========================
-- REVIEWS
-- =========================

CREATE TABLE reviews (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    movie_id BIGINT NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 10),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,

    UNIQUE (user_id, movie_id) -- один отзыв на фильм
);

-- =========================
-- OPTIONAL: FAVORITES
-- =========================

CREATE TABLE favorites (
    user_id BIGINT NOT NULL,
    movie_id BIGINT NOT NULL,
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
);


-- =========================
-- ROLES
-- =========================

INSERT INTO roles (name) VALUES
('admin'),
('moderator'),
('user');

-- =========================
-- PERMISSIONS
-- =========================

INSERT INTO permissions (name) VALUES
('create_movie'),
('update_movie'),
('delete_movie'),
('create_review'),
('delete_review'),
('ban_user');

-- =========================
-- ROLE PERMISSIONS
-- =========================

-- admin — всё можно
INSERT INTO role_permissions (role_id, permission_id)
SELECT r.id, p.id
FROM roles r, permissions p
WHERE r.name = 'admin';

-- moderator — ограниченно
INSERT INTO role_permissions (role_id, permission_id)
SELECT r.id, p.id
FROM roles r
JOIN permissions p ON p.name IN ('delete_review', 'ban_user')
WHERE r.name = 'moderator';

-- user — только отзывы
INSERT INTO role_permissions (role_id, permission_id)
SELECT r.id, p.id
FROM roles r
JOIN permissions p ON p.name = 'create_review'
WHERE r.name = 'user';

-- =========================
-- USERS
-- =========================

INSERT INTO users (username, email, password_hash) VALUES
('admin', 'admin@mail.com', 'hashed_password'),
('mod1', 'mod@mail.com', 'hashed_password'),
('user1', 'user1@mail.com', 'hashed_password'),
('user2', 'user2@mail.com', 'hashed_password'),
('user3', 'user3@mail.com', 'hashed_password');

-- =========================
-- USER ROLES
-- =========================

INSERT INTO user_roles (user_id, role_id)
SELECT u.id, r.id FROM users u, roles r
WHERE u.username = 'admin' AND r.name = 'admin';

INSERT INTO user_roles (user_id, role_id)
SELECT u.id, r.id FROM users u, roles r
WHERE u.username = 'mod1' AND r.name = 'moderator';

INSERT INTO user_roles (user_id, role_id)
SELECT u.id, r.id FROM users u, roles r
WHERE u.username LIKE 'user%' AND r.name = 'user';

-- =========================
-- GENRES
-- =========================

INSERT INTO genres (name) VALUES
('Action'),
('Drama'),
('Comedy'),
('Sci-Fi'),
('Horror'),
('Thriller');

-- =========================
-- MOVIES
-- =========================

INSERT INTO movies (title, description, release_year, duration_minutes) VALUES
('Inception', 'Dream inside a dream', 2010, 148),
('The Matrix', 'Simulation reality', 1999, 136),
('Interstellar', 'Space and time', 2014, 169),
('The Dark Knight', 'Batman vs Joker', 2008, 152),
('Parasite', 'Social thriller', 2019, 132),
('The Conjuring', 'Horror story', 2013, 112);

-- =========================
-- MOVIE GENRES
-- =========================

INSERT INTO movie_genres VALUES
(1, 1), (1, 4),  -- Inception: Action, Sci-Fi
(2, 1), (2, 4),  -- Matrix
(3, 4), (3, 2),  -- Interstellar: Sci-Fi, Drama
(4, 1), (4, 6),  -- Dark Knight: Action, Thriller
(5, 2), (5, 6),  -- Parasite
(6, 5), (6, 6);  -- Conjuring: Horror, Thriller

-- =========================
-- REVIEWS
-- =========================

INSERT INTO reviews (user_id, movie_id, rating, comment) VALUES
(3, 1, 9, 'Очень сложно, но круто'),
(4, 1, 8, 'Надо пересмотреть'),
(5, 2, 10, 'Классика'),
(3, 3, 9, 'Космос и драма'),
(4, 4, 10, 'Лучший Бэтмен'),
(5, 5, 8, 'Неожиданно сильно'),
(3, 6, 7, 'Страшно, но клишировано');

-- =========================
-- FAVORITES
-- =========================

INSERT INTO favorites VALUES
(3, 1),
(3, 2),
(4, 4),
(5, 2),
(5, 3);

COMMIT;