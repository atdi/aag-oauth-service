__author__ = 'aurel'

from .app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
db = SQLAlchemy()
oauth = OAuth2Provider()


def init_app(settings='aag_oauth_service.config.DevelopmentConfig'):
    app.config.from_object(settings)
    db.init_app(app)
    oauth.init_app(app)