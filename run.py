from flask import Flask
from flask import jsonify, request, send_file
from flask import Response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import json

from vault_app.api.v1.views import api_bp
from vault_app.api.v1.auth import auth_bp
#from vault_app.db import initialize_db


app = Flask(__name__)
#set ENV_FILE_LOCATION=./.env
app.config.from_envvar('ENV_FILE_LOCATION')

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

if __name__=='__main__':
    # Adding blueprints
    app.register_blueprint(api_bp, url_prefix='/v1')
    app.register_blueprint(auth_bp, url_prefix='/v1')
    
    # Add more blueprints here for different API versions 
    
    app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost:27017/user-vault-data'
                                      }
    #initialize_db(app)
    app.run(debug=True, port=8000)


