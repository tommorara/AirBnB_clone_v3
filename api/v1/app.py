#!/usr/bin/python3

'''create flash app'''

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

'''create an instance of the Flask class'''

app = Flask(__name__)

'''register the blueprint'''

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', '5000'))
    app.run(host=HOST, port=PORT, threaded=True)
