#from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import Document, StringField


class User(Document):
    """ Class to store user objects in mongo
    """
    username = StringField(required=True, unique=True)
    password = StringField(required=True, min_length=6)

    def hash_password(self):
        """ Function to hash the user password
        """
        self.password = generate_password_hash(self.password).decode('utf-8')
    
    def check_password(self, password):
        """ Function to check if the hash of the provided 
        password matches the stored hash
        """
        return check_password_hash(self.password, password)

