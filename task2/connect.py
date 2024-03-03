import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from pathlib import Path


ENV_PATH = Path(__file__).parent.parent / ".env"


def create_connect() -> MongoClient:
    load_dotenv(ENV_PATH)

    client = MongoClient(
        # os.getenv("MONGO_DB_HOST"),
        # "mongodb+srv://catuser:3USCNHSKqiQ8bagO@cluster0.subb4se.mongodb.net/cats_db?retryWrites=true&w=majority&appName=Cluster0",
        "mongodb+srv://chubvova7:5iwhTfMLSNQUlJRp@cluster0.subb4se.mongodb.net/cats_db?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi("1"),
    )

    return client


if __name__ == "__main__":
    client = create_connect()
    db = client["cats_db"]
    collection = db["cats"]
    cats = collection.find()
    # print(cats)
    for cat in cats:
        print(cat)
