from utils.database import db
from utils.schema import ma
from models.base import BaseModel


class UserRole(db.Model, BaseModel):
    id = db.Column(db.Integer(), primary_key=True)
    name = str


class User(db.Model, BaseModel):
    id = db.Column(db.Integer(), primary_key=True)
    name = str
    password = str
    role = UserRole


class UserSchema(ma.Schema):
    pass
