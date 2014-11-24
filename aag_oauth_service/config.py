__author__ = 'aurel'

# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    OAUTH2_PROVIDER_TOKEN_EXPIRES_IN=36000
    USER_SERVICE_URL = 'http://localhost:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    USER_SERVICE_URL='http://localhost:5000'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/oauth'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



