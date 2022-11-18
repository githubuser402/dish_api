from utils.database import db
from utils.schema import ma
from models.base import BaseModel


class Picture(db.Model, BaseModel):
    id = db.Column(db.Integer(), primary_key=True)
    path = str


class PictureSchema(ma.Schema):
    pass
