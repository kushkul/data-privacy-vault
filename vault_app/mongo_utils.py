from pymongo import MongoClient

def get_mongo_database():
    CONN = 'mongodb://localhost:27017/'
    client = MongoClient(CONN)

    return client['user-vault-data']

