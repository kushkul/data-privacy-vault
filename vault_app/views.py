from flask import Flask
from flask import jsonify, request, send_file, abort
from flask import Response
from flask import Blueprint
import json

api_bp = Blueprint('api', __name__)


#---------------Error Handlers

# Custom Error handler for 404 errors
@api_bp.errorhandler(404)
def not_found_error(error):
    return json.dumps({'error':'Not found lol'}), 404

# Custom error handler for 400 errors
@api_bp.errorhandler(400)
def bad_request_error(error):
    return json.dumps({'error':'Bad Request lol'}), 400

# Custom error handler for 500 errors
@api_bp.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error':'Internal Server Error'}), 500

# Custom handler for specific exceptions
@api_bp.errorhandler(Exception)
def handle_exception(error):
    return jsonify({'error':'An unexpected error has occured'}), 500



# Routes for producing errors
@api_bp.route('/not_found')
def not_found():
    abort(404)

@api_bp.route('/bad_request')
def bad_request():
    abort(400)

@api_bp.route('/internal_server_error')
def internal_server_error_route():
    raise Exception('Something went wrong')




#------------------End points

@api_bp.route('/tokenize', methods=['POST'])
def tokenize_info():
    content = request.json
    print(content)

    for key in content['data']:
        val = content['data'][key]
        val_token = tokenize_data(val)
        content['data'][key] = val_token

    return Response(json.dumps(content), status=201, mimetype='application/json')


@api_bp.route('/detokenize', methods=['POST'])
def detokenize_info():
    content = request.json
    print(content)

    for key in content['data']:
        val_token = content['data'][key]
        status, val = detokenize_data(val_token)

        content['data'][key] = {'found': status,
                                'value': val}

    return Response(json.dumps(content), status=201, mimetype='application/json')


def tokenize_data(data):
    # Do some processing
    return data + 'kk'


def detokenize_data(token):
    # Do some stuff
    status = True
    if status:
        val = token + '_kk'
    else:
        val = ""

    return status, val

