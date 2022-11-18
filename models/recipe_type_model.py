from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class RecipeType(db.Model, BaseModel):
    __tablename__ = "dish_recipe_type"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = str
    description = str


class RecipeTypeSchema(ma.Schema):
    pass
