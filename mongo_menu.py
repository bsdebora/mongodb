import pymongo
import os

MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "breakfast"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_record():
    print("")
    name = input("Enter item> ")
    try:
        doc = coll.find_one({'first': name.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc

def show_menu():
    print("")
    print("1. Add a name")
    print("2. Find a record by name")
    print("3. Edit a menu")
    print("4. Delete a menu")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def add_record():
    print("")
    category = input("Enter category> ")
    name = input("Enter name > ")
    quantity = input("Enter quantity > ")
    price = input("Enter price > ")
    calories = input("Enter calories > ")
    

    new_doc = {'category': category.lower(), 'name': name.lower(), 'quantity': quantity,
               'price': price, 'calories': calories}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()