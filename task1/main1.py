import logging
import psycopg2


def execute_query(sql, params=None):
    conn_params = {
        "host": "ваш_host",
        "database": "назва_вашої_бази_даних",
        "user": "ваш_username",
        "password": "ваш_password",
    }

    with psycopg2.connect(**conn_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if cursor.description:
                return cursor.fetchall()


def get_tasks_by_user_id(user_id):
    sql = "SELECT * FROM tasks WHERE user_id = %s"
    return execute_query(sql, (user_id,))


def get_tasks_by_status(status):
    sql = "SELECT * FROM tasks WHERE status = %s"
    return execute_query(sql, (status,))


def update_task_status(task_id, new_status):
    sql = "UPDATE tasks SET status = %s WHERE id = %s"
    execute_query(sql, (new_status, task_id))


def get_users_with_no_tasks():
    sql = """
    SELECT * FROM users 
    WHERE id NOT IN (
        SELECT DISTINCT user_id FROM tasks
    )
    """
    return execute_query(sql)


if __name__ == "__main__":
    # Тестування функцій
    print(get_tasks_by_user_id(1))  # Замініть 1 на реальний user_id
    print(get_tasks_by_status("new"))  # Замініть 'new' на реальний статус
    update_task_status(10, "in progress")  # Замініть 10 на реальний id завдання
    print(get_users_with_no_tasks())
