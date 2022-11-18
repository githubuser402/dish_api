from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class Product(db.Model, BaseModel):
    __tablename__  = "product"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = str
    description = str
    pictures = list


class ProductSchema(ma.Schema):
    pass
