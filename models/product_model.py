from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class Product(db.Model, BaseModel):
    __tablename__  = "product"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(250))
    pictures = db.relationship("Picture", cascade="all,delete")


class ProductSchema(ma.Schema):
    pass
