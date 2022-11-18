import unittest2

# from config.app_config import DevelopmentConfig
from config.test_config import TestConfig
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

import tempfile


class BaseTestCase(unittest2.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config.from_object(TestConfig)

        self.test_db_file = tempfile.mkstemp()[1]
        app['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.test_db_file

        db.init_app(app=app)
        migrate.init_app(app=app, db=db)
        ma.init_app(app=app)

        app.app_context().push()

        self.app = app.test_client()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()