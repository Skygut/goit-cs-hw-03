import os
import logging
import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")
print(os.getenv("POSTGRES_PASSWORD"))


@contextmanager
def create_connect():

    try:
        # conn = psycopg2.connect(
        #     dbname="postgres",
        #     user="postgres",
        #     password="1234",
        #     host="localhost",

        # )

        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )

        try:
            yield conn
            print("Connection successful")
            # return conn

        except:
            conn.close()
    except psycopg2.OperationalError as er:
        print(er)
        print("Connection failed")


if __name__ == "__main__":
    load_dotenv(Path(__file__).parent.parent / ".env")
    # print("Connection successful")

    create_connect()
