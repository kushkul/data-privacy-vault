from flask import Flask
from flask import jsonify, request, send_file, abort
from flask import Response
from flask import Blueprint
from flask_jwt_extended import jwt_required
import json

from .db import get_mongo_conn
from mongoengine.connection import disconnect

import datetime
import string
import uuid
from ff3 import FF3Cipher
import traceback

from . import ENCRYPTION_KEY
from . import TWEAK

api_bp = Blueprint('api', __name__)


#------------------End points

@api_bp.route('/tokenize', methods=['POST'])
#@jwt_required
def tokenize_info():
    """
    """
    content = request.json
    try:
        for key in content['data']:
            val = content['data'][key]
            val_token = tokenize_data(val)
            content['data'][key] = val_token
    except Exception as e:
        print(e)
        print(traceback.print_exc())
    print(content)

    return Response(json.dumps(content), status=201, mimetype='application/json')


@api_bp.route('/detokenize', methods=['POST'])
#@jwt_required
def detokenize_info():
    """
    """
    try:
        content = request.json
        print(content)

        for key in content['data']:
            val_token = content['data'][key]
            status, val = detokenize_data(val_token)

            content['data'][key] = {'found': status,
                                    'value': val}
    except Exception as e:
        print(e)

    return Response(json.dumps(content), status=201, mimetype='application/json')


def tokenize_data(data):
    """
    """
    # Encrypt data here
    encrypted_token = encrypt_data(data)

    # Connect to mongo database
    #TODO: Put database connection in context operator
    conn = get_mongo_conn()
    collection_name = conn['user-vault-data']['data-tokens']
    
    # Save the items to database
    item_to_save = {
        "_id" : uuid.uuid4().hex,
        "value" : data,
        "token" : encrypted_token,
        "added" : datetime.datetime.now()
    }
    
    try:
        collection_name.insert_one(item_to_save)
    except Exception as e:
        print(e)

    disconnect('user-vault-data')
    return encrypted_token


def detokenize_data(token):
    """
    """
    # Connect to mongo database
    #TODO: Put database connection in context operator
    conn = get_mongo_conn()
    collection_name = conn['user-vault-data']['data-tokens']

    status = 'Invalid'
    value = 'Invalid'

    print('Value to find: {}'.format(token))
    try:
        item_details = collection_name.find_one({'token':token})
        print(item_details)
        val = decrypt_data(item_details['token'])
        status = True
    except Exception as e:
        print(e)
        status = False
        val = ""
    
    disconnect('user-vault-data')

    return status, val


def encrypt_data(data):
    c = FF3Cipher.withCustomAlphabet(ENCRYPTION_KEY, TWEAK, string.ascii_letters+' ')
    encrypted_data = c.encrypt(data)
    return encrypted_data


def decrypt_data(token):
    try:
        c = FF3Cipher.withCustomAlphabet(ENCRYPTION_KEY, TWEAK, string.ascii_letters+' ')
        print(token)
        return c.decrypt(token)
    except Exception as e:
        print(e)



#---------------Error Handlers

# # Custom Error handler for 404 errors
# @api_bp.errorhandler(404)
# def not_found_error(error):
#     return json.dumps({'error':'Not found lol'}), 404

# # Custom error handler for 400 errors
# @api_bp.errorhandler(400)
# def bad_request_error(error):
#     return json.dumps({'error':'Bad Request lol'}), 400

# # Custom error handler for 500 errors
# @api_bp.errorhandler(500)
# def internal_server_error(error):
#     return jsonify({'error':'Internal Server Error'}), 500

# # Custom handler for specific exceptions
# #@api_bp.errorhandler(Exception)
# #def handle_exception(error):
# #    return jsonify({'error':'An unexpected error has occured'}), 500



# # Routes for producing errors
# @api_bp.route('/not_found')
# def not_found():
#     abort(404)

# @api_bp.route('/bad_request')
# def bad_request():
#     abort(400)

# #@api_bp.route('/internal_server_error')
# #def internal_server_error_route():
# #    raise Exception('Something went wrong')

