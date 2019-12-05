import os
import sys


class Config(object):
    DEBUG = False
    TESTING = False
    IMAGE_UPLOADS = "/app/static/uploads"

    try:
        SECRET_KEY = 5
    except KeyError:
        print("Session secret key is not defined!")
        sys.exit(1)

class ProductionConfig(Config):
    IMAGE_UPLOADS = "/app/static/uploads"

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
