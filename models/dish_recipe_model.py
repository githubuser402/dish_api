from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel

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
    name = db.Column(db.String(80), required=True)
    recipe = db.Column(db.String())
    products = db.relationship("Product", secondary=recipe_product, backref="dishes")
    pictures = db.relationship("Picture", secondary=recipe_picture)


class DishRecipeSchema(ma.Schema):
    pass
