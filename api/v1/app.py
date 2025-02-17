#!/usr/bin/python3

"""
Creates the app. Lengthy documentation, blah, blah, blah.
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(self):
    """Tears down the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """return 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', '5000'))

    app.run(host=HOST, port=PORT, threaded=True)
