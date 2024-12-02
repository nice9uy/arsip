import pymongo
# from .settings import settings

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.get_database("arsip")


def get_db_connections():
    return db

