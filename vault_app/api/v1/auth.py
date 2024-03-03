from flask import request
from flask import Blueprint
from flask import Response, request
from flask_jwt_extended import create_access_token

import json
import datetime

from vault_app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup_api():
    """ API to signup a new user
    """
    body = request.json

    user = User(**body)
    user.hash_password()
    user.save()
    user_name = user.username

    content = {'id':str(user_name)}

    return Response(json.dumps(content), status=201, mimetype='application/json')


@auth_bp.route('/login', methods=['POST'])
def login_api():
    """ API for user login using JWT Token
    """
    body = request.json
    user = User.objects.get(username=body.get('username'))
    
    authorized = user.check_password(body.get('password'))
    if not authorized:
        content = {'error':'Could not validate the username!'}
        return Response(json.dumps(content), status=401, mimetype='application/json')
    else:
        # Add jwt token 
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=str(user.username),
                                           expires_delta=expires)
        content = {'token': access_token}
        return Response(json.dumps(content), 200, mimetype='application/json')





