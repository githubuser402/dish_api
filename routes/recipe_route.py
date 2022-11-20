from flask import Blueprint, request
from utils.response import response_with
import utils.response as resp

from models.dish_recipe_model import DishRecipe, DishRecipeSchema

recipe_routes = Blueprint("recipe_routes", __name__)


@recipe_routes.route("/", methods=["GET"])
def get_all_recipes():
    recipe_schema = DishRecipeSchema(many=True)
    recipes = DishRecipe.query.all()
    recipe_json = recipe_schema.dump(recipes)
    
    return response_with(resp.SUCCESS_200, values=recipe_json)


@recipe_routes.route("/<recipe_id>/", methods=["GET"])
def get_recipe(recipe_id):
    recipe_schema = DishRecipeSchema(many=True)
    recipe = DishRecipe.query.filter_by(id=recipe_id).first()
    
    if not recipe:
        return response_with(resp.SERVER_ERROR_404)
    
    recipe_json = recipe_schema.dump(recipe)
    
    return response_with(resp.SUCCESS_200, value=recipe_json)


@recipe_routes.route("/", methods=["POST"])
def create_recipe():
    recipe_schema = DishRecipeSchema(many=True)
    data = request.get_json()
    
    try: 
        cleaned_data = recipe_schema.load(data)
        recipe = DishRecipe(**cleaned_data)
        
        recipe.save()
        
        return response_with(resp.SUCCESS_201, value=recipe_schema.dump(recipe))
    except Exception as ex:
        return response_with(resp.INVALID_INPUT_422)


@recipe_routes.route("/<recipe_id>/", methods=["PATCH"])
def patch_recipe(recipe_id):
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/<recipe_id>/", methods=["DELETE"])
def delete_recipe(recipe_id):
    return response_with(resp.SUCCESS_204)
