from flask import Flask
from flask import jsonify, request, send_file
from flask import Response
import json

from vault_app.views import api_bp


app = Flask(__name__)


# @app.route('/tokenize', methods=['GET','POST'])
# def tokenize_info():
#     # Receiving name from request
#     content = request.json
#     print(content)

#     for key in content['data']:
#         val = content['data'][key]
#         val_token = get_token(val)
#         content['data'][key] = val_token

#     return Response(json.dumps(content), status=201, mimetype='application/json')


# def get_token(data):
#     # Do some processing
#     return data + 'kk'


if __name__=='__main__':
    app.register_blueprint(api_bp)
    print(app.url_map)
    app.run(debug=True, port=8000)


