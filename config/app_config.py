import os
from config.config import Config


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "db.sqlite3")}'
    SQLALCHEMY_ECHO = False
    SECURITY_PASSWORD_SALT = 'IJI39dk39r'
    SECRET_KEY = "OIOSHd30j3e03w0"
