from pymongo import errors
from bson.objectid import ObjectId


def get_all(name: str | None = None) -> list[dict]:
    try:
        if name:
            return list(cats_collection.find({"name": {"$regex": name}}))
        return list(cats_collection.find())
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні всіх котів: {e}")
        return []


def get_by_id(id: ObjectId) -> dict | None:
    try:
        return cats_collection.find_one({"_id": id})
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні кота за ID {id}: {e}")
        return None


def create(body: dict) -> dict:
    try:
        result_one = cats_collection.insert_one(body)
        return get_by_id(result_one.inserted_id)
    except errors.PyMongoError as e:
        print(f"Помилка при створенні кота: {e}")
        return None


def update_by_id(id: ObjectId, body: dict) -> dict | None:
    try:
        data = {k: v for k, v in body.items() if v is not None}
        updated_cat = cats_collection.find_one_and_update(
            {"_id": id}, {"$set": data}, return_document=True
        )
        return updated_cat
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні кота з ID {id}: {e}")
        return None


def add_feature_by_id(id: ObjectId, new_feature: str) -> dict | None:
    try:
        updated_cat = cats_collection.find_one_and_update(
            {"_id": id}, {"$addToSet": {"features": new_feature}}, return_document=True
        )
        return updated_cat
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики до кота з ID {id}: {e}")
        return None


def delete_by_id(id: ObjectId) -> ObjectId | None:
    try:
        result = cats_collection.delete_one({"_id": id})
        return id if result.deleted_count == 1 else None
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота з ID {id}: {e}")
        return None


def delete_all() -> None:
    try:
        cats_collection.delete_many({})
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")


def create(body: dict) -> ObjectId:
    try:
        result_one = cats_collection.insert_one(body)
        return result_one.inserted_id  # повертаємо ObjectId нового документа
    except errors.PyMongoError as e:
        print(f"Помилка при створенні кота: {e}")
        return None


def get_cat_by_name(name):
    try:
        return collection.find_one({"name": name})
    except errors.PyMongoError as e:
        print(f"Помилка при пошуку кота з ім'ям {name}: {e}")
        return None


def update_cat_age(name, new_age):
    try:
        collection.update_one({"name": name}, {"$set": {"age": new_age}})
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота {name}: {e}")
