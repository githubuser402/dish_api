from config.settings import DevelopmentConfig
from flask import Flask
from utils.database import db
from utils.schema import ma
from utils.migrate import migrate
from pprint import pprint

# models
from models.dish import Dish
from models.product import Product
from models.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    ma.init_app(app=app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
