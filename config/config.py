import os
import datetime

class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_ECHO = False
    BASE_DIR = os.getcwd()
    TEMPLATE_FOLDER = os.path.join(os.getcwd(), "templates/")
    STATICFILES_FOLDER = os.path.join(os.getcwd(), "static/")
    MEDIAFILES_FOLDER = os.path.join(os.getcwd(), "media/")
    MEDIA_URL = "/media/"
    SECURITY_PASSWORD_SALT = None
    TOKEN_LIFE_TIME = datetime.timedelta(hours=1)
    ALGORITHM = "HS256"