import os

class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_ECHO = False
    TEMPLATE_FOLDER = os.path.join(os.getcwd(), "templates/")
    STATICFILES_FOLDER = os.path.join(os.getcwd(), "static/")
    MEDIAFILES_FOLDER = os.path.join(os.getcwd(), "media/")
    SECURITY_PASSWORD_SALT = None