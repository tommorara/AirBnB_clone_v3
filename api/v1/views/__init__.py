#!/usr/bin/python3
'''create flash app blueprint'''

from flask import Blueprint
from doc import Blueprint
from api.v1.views.index import *

'''create an instance of the Blueprint class'''

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

