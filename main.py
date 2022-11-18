from config.app_config import DevelopmentConfig
from flask import Flask
from utils.database import db
from utils.schema import ma
from utils.migrate import migrate

# models
from models.dish_recipe_model import DishRecipe
from models.recipe_type_model import RecipeType
from models.product_model import Product
from models.user_model import User, UserRole
from models.picture_model import Picture


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
