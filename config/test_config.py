from config.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'PASSWORD-SALT'
    MAIL_DEFAULT_SENDER = ''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
