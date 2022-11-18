from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class Picture(db.Model, BaseModel):
    __tablename__ = "picture"
    
    id = db.Column(db.Integer(), primary_key=True)
    path = str


class PictureSchema(ma.Schema):
    pass
