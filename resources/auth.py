from flask import request
from flask import Blueprint
from flask import Response
import json

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

    return Response(json.dumps(content), status=200, mimetype='application/json')




