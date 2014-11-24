__author__ = 'aurel'

# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/users'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
OAUTH2_PROVIDER_TOKEN_EXPIRES_IN=36000
USER_SERVICE_URL = 'http://localhost:5000'
