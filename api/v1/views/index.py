#!/usr/bin/python3
'''Import app_views Blueprint and jsonify from Flask'''
from api.v1.views import app_views
from flask import jsonify

'''Define a route /status that returns a JSON response'''
@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})
