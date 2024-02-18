from flask import Flask
from flask import jsonify, request, send_file, abort
from flask import Response
import json

if __name__=='__main__':
    app = Flask(__name__)


    #---------------Error Handlers

    # Custom Error handler for 404 errors
    @app.errorhandler(404)
    def not_found_error(error):
        return json.dumps({'error':'Not found lol'}), 404

    # Custom error handler for 400 errors
    @app.errorhandler(400)
    def bad_request_error(error):
        return json.dumps({'error':'Bad Request lol'}), 400

    # Custom error handler for 500 errors
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({'error':'Internal Server Error'}), 500

    # Custom handler for specific exceptions
    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({'error':'An unexpected error has occured'}), 500


    # Routes for producing errors

    @app.route('/not_found')
    def not_found():
        abort(404)

    @app.route('/bad_request')
    def bad_request():
        abort(400)

    @app.route('/internal_server_error')
    def internal_server_error_route():
        raise Exception('Something went wrong')




    @app.route('/my-first-api', methods=['GET'])
    def hello():
        # Receiving name from request
        name = request.args.get('name')
        if name is None:
            text = 'Hello World!'
        else:
            text = 'Hello ' + name + ' !'

        return jsonify({'message':text})




    app.run(debug=True, port=8000)

