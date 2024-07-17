

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017/')
db = client['cats_database']  # Назва бази даних
collection = db['cats']  # Назва колекції



def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Додано новий документ з _id: {result.inserted_id}")


# читання всіх записів у колекції
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)


# читання кота за ім'ям
def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений.")


# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    if result.modified_count > 0:
        print(f"Оновлено документ з ім'ям '{name}'.")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений.")


# features кота за ім'ям
def add_feature_to_cat(name, new_feature):
    result = collection.update_one(
        {"name": name},
        {"$push": {"features": new_feature}}
    )
    if result.modified_count > 0:
        print(f"Додано нову характеристику до кота '{name}'.")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений.")


# видалення запису за ім'ям кота
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Видалено документ з ім'ям '{name}'.")
    else:
        print(f"Кіт з ім'ям '{name}' не знайдений.")


# видалення записів 
def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} документів.")


if __name__ == '__main__':
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "муркотить")
    delete_cat_by_name("barsik")
    delete_all_cats()
