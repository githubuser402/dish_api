from utils.database import db
from utils.schema import ma
from models.base import BaseModel


class DishRecipe(db.Model, BaseModel):
    id = db.Column(db.Integer(), primary_key=True)
    name = str
    dish_type = str
    recipe = str
    products = list
    pictures = list 

class DishRecipeSchema(ma.Schema):
    pass
