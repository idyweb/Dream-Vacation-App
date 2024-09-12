from pymongo import MongoClient
from decouple import config

def get_database(db_name, collection_name):
    CONNECTION_STRING = config("MONGO_URL")
    client = MongoClient(CONNECTION_STRING)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def get_users_collection():
    return get_database('your_db_name', 'users')

