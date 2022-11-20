from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel
from models.picture_model import PictureSchema
from models.product_model import  ProductSchema


recipe_product = db.Table(
    "recipe_product",
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("recipe_id", db.Integer(), db.ForeignKey("recipe.id")),
    db.Column("product_id", db.Integer(), db.ForeignKey("product.id"))
)


recipe_picture = db.Table(
    "recipe_picture", 
    db.Column("id", db.Integer(), primary_key=True),
    db.Column("recipe_id", db.Integer(), db.ForeignKey("recipe.id")),
    db.Column("picture_id", db.Integer(), db.ForeignKey("picture.id"))
)

class DishRecipe(db.Model, BaseModel):
    __tablename__ = "recipe"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    recipe = db.Column(db.String(500), nullable=False)
    products = db.relationship("Product", secondary=recipe_product, backref="dish")
    pictures = db.relationship("Picture", secondary=recipe_picture, backref="dish")

    def __repr__(self):
        return f"<{self.id} {self.name}>"


class DishRecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'recipe', 'products', 'pictures')
        
    id = ma.Number(dump_only=True)
    name = ma.String()
    recipe = ma.String()
    products = ma.Nested(ProductSchema, many=True)
    pictures = ma.Nested(PictureSchema, many=True)
    
