from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class UserRole(db.Model, BaseModel):
    __tablename__ = "user_role"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    users = db.relationship("User", backref="role")


class User(db.Model, BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60))
    role_id = db.Column(db.Integer(), db.ForeignKey("user_role.id"))


class UserSchema(ma.Schema):
    pass
