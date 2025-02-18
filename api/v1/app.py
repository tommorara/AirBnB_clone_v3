#!/usr/bin/python3
import os
import sys
from flask import Flask
from models import storage
from api.v1.views import app_views

'''Create a Flask application instance'''
app = Flask(__name__)

'''Register the app_views Blueprint'''
app.register_blueprint(app_views)

'''Define a teardown function to close storage when the app context ends'''
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

'''Run the Flask app with environment-configured host and port'''
if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=HOST, port=PORT, threaded=True)
