from flask import Flask
from flask import jsonify, request, send_file
from flask import Response
import json

from vault_app.views import api_bp


app = Flask(__name__)


if __name__=='__main__':
    app.register_blueprint(api_bp)
    print(app.url_map)
    app.run(debug=True, port=8000)


