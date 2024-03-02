import logging
from psycopg2 import DatabaseError
from connect import create_connect


"""
1. Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.

SELECT *
FROM users u 
WHERE id = 5;

2. Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.

SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM tasks WHERE name = 'new');

3.  Oновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;

4. Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.

SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);

5. Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ("Назва завдання", "Опис завдання", (SELECT id FRFOM status WHERE name = "new"),1);


6. Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.

SELECT *
FROM tasks
WHERE status != 'completed';


7. Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.

DELETE FROM tasks
WHERE id = 2;

8. Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.

SELECT *
FROM users
WHERE email LIKE '%@example.net';

9. Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.

UPDATE users
SET name = 'new name'
WHERE id = 2;

10. Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.

SELECT status, COUNT(*) AS task_count
FROM tasks
GROUP BY status;

11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').

SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.net';

12. Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.

SELECT *
FROM tasks
WHERE description IS NULL OR description = '';

13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.

SELECT users.*, tasks.*
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status = 'in progress';

14. Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.

SELECT users.id, users.name, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.name;

"""


def get_task_by_id(conn, task_id):
    sql = """
    select * from tasks
    where id = %s;
    """

    return get_data(conn, sql, (task_id,))


if __name__ == "__main__":
    try:
        with create_connect() as conn:
            """
            Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
            """
            pprint(get_tasks_by_user_id(conn, 1))

    except RuntimeError as er:
        logging.error(f"Runtime error: {er}")
    except DatabaseError as er:
        logging.error(f"Database error: {er}")
