import os


class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "sjfsjfskffk3034j4r34anfon"
    SQLALCHEMY_DATABASE_URI = None
    TEMPLATE_FOLDER = os.path.join(os.getcwd(), "templates/")
    STATICFILES_FOLDER = os.path.join(os.getcwd(), "static/")
    MEDIAFILES_FOLDER = os.path.join(os.getcwd(), "media/")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "db.sqlite3")}'