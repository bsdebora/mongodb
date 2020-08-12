import pymongo
import os


MONGODB_URI = "mongodb://root:RootUser@myfirstcluster-shard-00-00.zhfps.mongodb.net:27017,myfirstcluster-shard-00-01.zhfps.mongodb.net:27017,myfirstcluster-shard-00-02.zhfps.mongodb.net:27017/myTestDB?ssl=true&replicaSet=atlas-z7d5ni-shard-0&authSource=admin&retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "non_veg_menu"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

'''new_doc = [{'category': 'non_veg_menu', 'name': 'chicken biryani', 'quantity': '150 grams', 'price': '2 dollars', 'calories': '170'}, {'category': 'non_veg_menu', 'name': 'mutton biryani', 'quantity': '2', 'price': '3 dollars', 'calories': '350'}, {'category': 'non_veg_menu', 'name': 'prawns biryani', 'quantity': '3 scoops', 'price': '2 dollars', 'calories': '200'}, {'category': 'non_veg_menu', 'name': 'fish curry', 'quantity': '4', 'price': '3 dollars', 'calories': '450'},{'category': 'non_veg_menu', 'name': 'mutton kima', 'quantity': '1', 'price': '3', 'calories': '300'}, {'category': 'non_veg_menu', 'name': 'chicken 65', 'quantity': '2 scoops and 2 mirchi', 'price': '3', 'calories': '400'}]
coll.insert_many(new_doc)'''

coll.update_many({'category':'non_veg_menu'},{'$set':{'price':'6 dollars'}})

documents = coll.find()

for doc in documents:
    print(doc)