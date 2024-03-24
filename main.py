from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure, DuplicateKeyError

try:
    client = MongoClient(
        "mongodb+srv://user:user1@cluster0.upgzm2n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi('1')
    )
except ConnectionFailure as e:
    print("Помилка підключення до бази даних:", e)
    exit()

db = client.book

#Читання
def read_all_cats():
    #Вивести всі записи із колекції
    try:
        cats = client.book.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print("Помилка при читанні записів:", e)
        
def read_cat_by_name(name):
    #Вивести інформацію про кота за ім'ям
    try:
        cat = client.book.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кіт з ім'ям {} не знайдений.".format(name))
    except Exception as e:
        print("Помилка при читанні запису за ім'ям {}: {}".format(name, e))
        
#Оновлення
def update_cat_age(name, new_age):
    #Оновити вік кота за ім'ям.
    try:
        client.book.update_one({"name": name}, {"$set": {"age": new_age}})
        print("Вік кота {} оновлено.".format(name))
    except Exception as e:
        print("Помилка при оновленні віку кота {}: {}".format(name, e))

def add_cat_feature(name, new_feature):
    #Додати нову характеристику до списку features кота за ім'ям.
    try:
        client.book.update_one({"name": name}, {"$push": {"features": new_feature}})
        print("Нову характеристику додано до кота {}.".format(name))
    except Exception as e:
        print("Помилка при додаванні характеристики до кота {}: {}".format(name, e))
 
#Видалення
def delete_cat_by_name(name):
    #Видалити запис з колекції за ім'ям тварини.
    try:
        client.book.delete_one({"name": name})
        print("Кота {} видалено з бази даних.".format(name))
    except Exception as e:
        print("Помилка при видаленні кота {}: {}".format(name, e))

def delete_all_cats():
    #Видалити всі записи із колекції.
    try:
        client.book.delete_many({})
        print("Всі коти видалені з бази даних.")
    except Exception as e:
        print("Помилка при видаленні усіх котів: {}".format(e))
   
if __name__ == "__main__":
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_cat_feature("barsik", "любить спати на дивані")
    delete_cat_by_name("barsik")
    delete_all_cats()