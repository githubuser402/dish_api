from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel
from models.picture_model import PictureSchema

product_picture = db.Table(
    "product_picture",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("product_id", db.ForeignKey("product.id")),
    db.Column("picture_id", db.ForeignKey("picture.id"))
) 

class Product(db.Model, BaseModel):
    __tablename__  = "product"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    pictures = db.relationship("Picture", secondary=product_picture, cascade="all,delete")
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<{self.id} {self.name}>"


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'pictures')
        
    id = ma.Number(dump_only=True)
    name = ma.String()
    description = ma.String()
    pictures = ma.Nested(PictureSchema, many=True)
