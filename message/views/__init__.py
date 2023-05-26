#!/usr/bin/python3
"""The api initialization"""
from flask import Blueprint
from flask_mail import Mail
from os import environ

notification = Blueprint('notification', __name__, url_prefix='/notify/')

mail = Mail()

from message.views.index import *
from message.views.create import *

def configure_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'oyebamijimustapha44@gmail.com'
    app.config['MAIL_PASSWORD'] = environ.get('password')

    mail.init_app(app)
