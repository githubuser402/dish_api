from config.app_config import DevelopmentConfig
from config.config import Config
from flask import Flask
from utils.database import db
from utils.schema import ma
from utils.migrate import migrate

from utils.logger import logger

#CORS - Cross Origin Resource Sharing
from flask_cors import CORS

# routes
# from routes.product_route import product_routes
from routes.recipe_route import recipe_routes
from routes.user_route import user_routes
from routes.document_route import document_routes

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


app = create_app()

#CORS setup
CORS(app=app, resources={r'/*': {'origins': '*'}}, headers='Content-Type')

# register blueprints
app.register_blueprint(recipe_routes, url_prefix="/recipes/")
app.register_blueprint(user_routes, url_prefix="/user/")
app.register_blueprint(document_routes, url_prefix=Config.MEDIA_URL)

@app.after_request
def adding_cors_support(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'append,delete,entries,foreach,get,has,keys,set,values,Authorization,content-type,x-access-token'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
