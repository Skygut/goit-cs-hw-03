from faker import Faker
import psycopg2
import random

# Ініціалізація Faker
fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
)

cur = conn.cursor()

# Генерація даних для таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Генерація даних для таблиці tasks
for _ in range(30):
    title = fake.sentence(nb_words=5)
    description = fake.text()
    status_id = random.randint(1, 3)  # Припустимо, що у нас є 3 статуси
    user_id = random.randint(1, 10)  # Припустимо, що у нас є 10 користувачів
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id),
    )

# Збереження змін та закриття з'єднання
conn.commit()
cur.close()
conn.close()
