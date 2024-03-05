from connect_db import create_connect
from pymongo import errors
from bson.objectid import ObjectId

client = create_connect()
db = client["db-cats"]
cats_collection = db["cats"]


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


# def create(body: dict) -> dict:
#     try:
#         result_one = cats_collection.insert_one(body)
#         return get_by_id(result_one.inserted_id)
#     except errors.PyMongoError as e:
#         print(f"Помилка при створенні кота: {e}")
#         return None


def create(body: dict) -> ObjectId:
    try:
        result_one = cats_collection.insert_one(body)
        return result_one  # повертаємо ObjectId нового документа
    except errors.PyMongoError as e:
        print(f"Помилка при створенні кота: {e}")
        return None


def get_cat_by_name(name):
    try:
        if name:
            return list(cats_collection.find({"name": {"$regex": name}}))
        return list(cats_collection.find())
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні всіх котів: {e}")
        return []


def update_cat_age(name, new_age):
    try:
        cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота {name}: {e}")


def update_by_id(id: ObjectId, body: dict) -> dict | None:
    try:
        name = body.get("name")
        age = body.get("age")
        features = body.get("features")

        data = dict()

        if not name is None:
            data["name"] = name
        if not age is None:
            data["age"] = age
        if not features is None:
            data["features"] = features

        updated_cat = cats_collection.find_one_and_update(
            {"_id": id},
            {"$set": data},
            return_document=True,
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


if __name__ == "__main__":
    client = create_connect()
    db = client["db-cats"]
    cats_collection = db["cats"]

    cat = {
        "name": "Peter",
        "age": 2,
        "features": ["стрибає на задніх лапах", "багато спить", "хропе"],
    }

    cat1 = {
        "name": "Saschko",
        "age": 3,
        "features": ["не стрибає на задніх лапах", "мало спить", "тихо спить"],
    }

    cat2 = {
        "name": "hans",
        "age": 4,
        "features": ["спить в капці", "п'є пиво", "пухнастий"],
    }

    cat3 = {
        "name": "barsik",
        "age": 6,
        "features": ["не ходить в капці", "дає себе гладити", "білий"],
    }
    id = create(cat).inserted_id
    print(get_by_id(id))

    ######

    print(update_by_id(id, cat2))


    ############

    # id3 = ObjectId("65e61b7b5ef0a82d733d8dc1")
    # cat4 = "бігає швидко, стрибає на 2 метри, рябий"
    # print(add_feature_by_id(id3, cat4))

    #############

    # print(get_all(""))

    #############

    # print(get_all("hans"))

    #############

    # print(delete_by_id(id3))

    ############

    # print(delete_all())


    # def main_menu():
    # while True:
    #     print("\nВиберіть опцію:")
    #     print("1. Створити запис про кота (create)")
    #     print("2. Отримати список всіх котів (get_all)")
    #     print("3. Отримати кота за ID (get_by_id)")
    #     print("4. Отримати кота за ім'ям (get_cat_by_name)")
    #     print("5. Оновити вік кота (update_cat_age)")
    #     print("6. Оновити запис про кота (update_by_id)")
    #     print("7. Додати характеристику коту (add_feature_by_id)")
    #     print("8. Видалити кота за ID (delete_by_id)")
    #     print("9. Видалити всіх котів (delete_all)")
    #     print("10. Вихід (exit)")

    #     choice = input("Ваш вибір: ")

    #     if choice == '1':
    #         # Виклик функції створення запису про кота
    #         pass  # Тут буде код для create
    #     elif choice == '2':
    #         # Виклик функції отримання списку всіх котів
    #         pass  # Тут буде код для get_all
    #     elif choice == '3':
    #         # Виклик функції отримання кота за ID
    #         pass  # Тут буде код для get_by_id
    #     elif choice == '4':
    #         # Виклик функції отримання кота за ім'ям
    #         pass  # Тут буде код для get_cat_by_name
    #     elif choice == '5':
    #         # Виклик функції оновлення віку кота
    #         pass  # Тут буде код для update_cat_age
    #     elif choice == '6':
    #         # Виклик функції оновлення запису про кота
    #         pass  # Тут буде код для update_by_id
    #     elif choice == '7':
    #         # Виклик функції додавання характеристики коту
    #         pass  # Тут буде код для add_feature_by_id
    #     elif choice == '8':
    #         # Виклик функції видалення кота за ID
    #         pass  # Тут буде код для delete_by_id
    #     elif choice == '9':
    #         # Виклик функції видалення всіх котів
    #         pass  # Тут буде код для delete_all
    #     elif choice == '10':
    #         print("Вих
