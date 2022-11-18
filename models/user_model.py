from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class UserRole(db.Model, BaseModel):
    __tablename__ = "user_role"

    id = db.Column(db.Integer(), primary_key=True)
    name = str


class User(db.Model, BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    name = str
    password = str
    role = UserRole


class UserSchema(ma.Schema):
    pass
