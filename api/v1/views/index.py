#!/usr/bin/pythons
'''create flash app route'''
from flask import jsonify
from api.v1.views import app_views

'''create a route /status on the object app_views'''
@app_views.route('/status')
def api_status():
    '''return status'''
    return jsonify({"status": "OK"})
