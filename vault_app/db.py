from flask_mongoengine import MongoEngine
from mongoengine import connect
#from pymongo import MongoClient

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)

def get_mongo_conn():
    conn = connect('user-vault-data')
    #collection = conn['user-vault-data']['data-tokens']
    return conn

#CONN = 'mongodb://localhost:27017/'
#client = MongoClient(CONN)
#return client['user-vault-data']
