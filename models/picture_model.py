from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class Picture(db.Model, BaseModel):
    __tablename__ = "picture"
    
    id = db.Column(db.Integer(), primary_key=True)
    path = db.Column(db.String(140), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey("product.id"))


class PictureSchema(ma.Schema):
    class Meta:
        fields = ('id', 'path')
    
    id =  ma.Number(dump_only=True)
    path = ma.String()
