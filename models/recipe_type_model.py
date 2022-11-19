from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class RecipeType(db.Model, BaseModel):
    __tablename__ = "dish_recipe_type"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))


class RecipeTypeSchema(ma.Schema):
    pass
