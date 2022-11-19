from flask import Blueprint
from utils.response import response_with
import utils.response as resp


recipe_routes = Blueprint("recipe_routes", __name__)


@recipe_routes.route("/", methods=["GET"])
def get_all_recipes():
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/<recipe_id>/", methods=["GET"])
def get_recipe(recipe_id):
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/", methods=["POST"])
def create_recipe():
    return response_with(resp.SUCCESS_201)


@recipe_routes.route("/<recipe_id>/", methods=["PATCH"])
def patch_recipe(recipe_id):
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/<recipe_id>/", methods=["DELETE"])
def delete_recipe(recipe_id):
    return response_with(resp.SUCCESS_204)
