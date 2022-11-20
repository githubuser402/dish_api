from utils.database import db
from utils.schema import ma
from models.base_model import BaseModel


class RecipeType(db.Model, BaseModel):
    __tablename__ = "dish_recipe_type"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<{self.id} {self.name}>"


class RecipeTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        
    id = ma.Number(dump_only=True)
    name = ma.String()
    description = ma.String()
