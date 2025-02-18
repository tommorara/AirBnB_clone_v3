#!/usr/bin/python3
'''create flash app blueprint'''
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

'''Import all routes from index (PEP8 warning expected but acceptable)'''
from api.v1.views.index import *
