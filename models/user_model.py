from utils.database import db
from utils.schema import ma
from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import func
from models.base_model import BaseModel


class UserRole(db.Model, BaseModel):
    __tablename__ = "user_role"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", backref="role")


class UserRoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

    id = ma.Number(dump_only=True)
    name = ma.String()


class User(db.Model, BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer(), db.ForeignKey("user_role.id"))

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(hash, password):
        return sha256.verify(password, hash)

    def __repr__(self):
        return f"<{self.id}, {self.username}>"


class UserSchema(ma.Schema):
    class Meta:
        fileds = ('id', 'name', 'password', 'role')

    id = ma.Number(dump_only=True)
    name = ma.String()
    password = ma.String()
    role = ma.Nested(UserRoleSchema)
