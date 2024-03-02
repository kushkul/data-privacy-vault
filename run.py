from flask import Flask
from flask import jsonify, request, send_file
from flask import Response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import json

from vault_app.views import api_bp
from resources.auth import auth_bp
from vault_app.db import initialize_db


app = Flask(__name__)
#set ENV_FILE_LOCATION=./.env
app.config.from_envvar('ENV_FILE_LOCATION')

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

if __name__=='__main__':
    # Adding blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    #print(app.url_map)
    
    app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost:27017/user-vault-data'
                                      }
    initialize_db(app)
    app.run(debug=True, port=8000)


