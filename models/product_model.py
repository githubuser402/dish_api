from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel
from models.picture_model import PictureSchema

class Product(db.Model, BaseModel):
    __tablename__  = "product"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    pictures = db.relationship("Picture", cascade="all,delete")


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'pictures')
        
    id = ma.Number(dump_only=True)
    name = ma.String()
    description = ma.String()
    pictures = ma.Nested(PictureSchema, many=True)
