import random
import logging
import os
import psycopg2
from faker import Faker
from contextlib import contextmanager
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

# Ініціалізація Faker
fake = Faker()


@contextmanager
def create_connect():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
        )

        # conn = psycopg2.connect(
        #     host=os.getenv("POSTGRES_HOST"),
        #     database=os.getenv("POSTGRES_DB"),
        #     user=os.getenv("POSTGRES_USER"),
        #     password=os.getenv("POSTGRES_PASSWORD"),
        # )
        try:
            yield conn
        except:
            conn.close()
    except psycopg2.OperationalError:
        print("Connection failed")


if __name__ == "__main__":
    try:
        with create_connect() as conn:
            # Підключення до бази даних
            cur = conn.cursor()

            # Генерація даних для таблиці users
            for _ in range(10):
                fullname = fake.name()
                email = fake.email()
                cur.execute(
                    "INSERT INTO users (fullname, email) VALUES (%s, %s)",
                    (fullname, email),
                )

            # Генерація даних для таблиці tasks
            for _ in range(30):
                title = fake.sentence(nb_words=5)
                description = fake.text()
                status_id = random.randint(1, 3)  # Припустимо, що у нас є 3 статуси
                user_id = random.randint(
                    1, 10
                )  # Припустимо, що у нас є 10 користувачів
                cur.execute(
                    "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                    (title, description, status_id, user_id),
                )

    except RuntimeError as er:
        logging.error(f"Runtime error: {er}")
    except DatabaseError as er:
        logging.error(f"Database error: {er}")
    # finally:
    #     # Збереження змін та закриття з'єднання
    #     conn.commit()
    #     cur.close()
    #     conn.close()
