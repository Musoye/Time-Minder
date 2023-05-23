#!/usr/bin/python3
"""The api initialization"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/')

from api.views.index import *
from api.views.users import *
from api.views.projects import *
from api.views.tasks import *
