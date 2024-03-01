# # -- Створення таблиці Users
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     fullname VARCHAR(100),
#     email VARCHAR(100) UNIQUE
# );

# # -- Створення таблиці Statuses
# CREATE TABLE statuses (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );

# # -- Додавання деяких базових статусів
# # INSERT INTO statuses (name) VALUES ('Нове'), ('В процесі'), ('Завершено');

# # -- Створення таблиці Tasks
# CREATE TABLE tasks (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(255),
#     description TEXT,
#     status_id INTEGER,
#     user_id INTEGER,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (status_id) REFERENCES statuses(id),
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
