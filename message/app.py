#!/usr/bin/python3
"""The app of mail function"""
import models
from os import environ
from message.views import notification, configure_mail
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_mail import Mail
from os import environ


app = Flask(__name__)
app.secret_key = 'Ilovesecret123'


app.register_blueprint(notification)
configure_mail(app)
CORS(app, resources={r"/notify/*": {"origins": ["http://127.0.0.1", "http://0.0.0.0"]}})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    models.storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    host = environ.get('TIME_API_HOST', '0.0.0.0')
    port = environ.get('TIME_API_PORT', '5002')
    app.run(host=host, port=port, threaded=True)
