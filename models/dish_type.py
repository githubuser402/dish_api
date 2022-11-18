from utils.database import db
from utils.schema import ma
from models.base import BaseModel


class DishType(db.Model, BaseModel):
    id = db.Column(db.Integer(), primary_key=True)
    name = str
    description = str


class DishTypeSchema(ma.Schema):
    pass
