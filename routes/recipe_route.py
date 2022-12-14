from flask import Blueprint, request, url_for
from utils.response import response_with
import utils.response as resp
from utils.logger import logger
from utils.document_filter import is_allowed_file, generate_filename
from utils.database import db
from utils.decorators import token_required
from werkzeug.utils import secure_filename
import os
from flask_cors import cross_origin

from config.config import Config

from models.dish_recipe_model import DishRecipe, DishRecipeSchema
from models.picture_model import Picture, PictureSchema

recipe_routes = Blueprint("recipe_routes", __name__)


@recipe_routes.route("/", methods=["GET"])
@cross_origin()
# @token_required
def get_all_recipes():
    recipe_schema = DishRecipeSchema(many=True)
    recipes = DishRecipe.query.all()
    recipe_json = recipe_schema.dump(recipes)

    return response_with(resp.SUCCESS_200, value=recipe_json)


@recipe_routes.route("/<recipe_id>/", methods=["GET"])
@cross_origin()
def get_recipe(recipe_id):
    recipe_schema = DishRecipeSchema()
    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if not recipe:
        return response_with(resp.SERVER_ERROR_404)

    recipe_json = recipe_schema.dump(recipe)

    return response_with(resp.SUCCESS_200, value=recipe_json)


@recipe_routes.route("/", methods=["POST"])
@cross_origin()
@token_required
def create_recipe(user):
    recipe_schema = DishRecipeSchema()
    data = request.get_json()

    try:
        cleaned_data = recipe_schema.load(data)
        logger.debug(cleaned_data)

        recipe = DishRecipe(**cleaned_data)

        recipe.save()
        logger.info(f"saved recipe: {recipe}")

        return response_with(resp.SUCCESS_201, value=recipe_schema.dump(recipe))
    except Exception as ex:
        return response_with(resp.INVALID_INPUT_422)


@recipe_routes.route("/<recipe_id>/", methods=["PATCH"])
@cross_origin()
def patch_recipe(recipe_id):
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/<recipe_id>/", methods=["DELETE"])
@cross_origin()
def delete_recipe(recipe_id):
    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if recipe:
        logger.info(f"deleted recipe {recipe}")
        recipe.delete()
    return response_with(resp.SUCCESS_204)


@recipe_routes.route("/<recipe_id>/pictures/", methods=["GET"])
@cross_origin()
def get_recipe_pictures(recipe_id):
    picture_schema = PictureSchema(many=True)

    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if not recipe:
        return response_with(resp.SERVER_ERROR_404)

    logger.debug(recipe.pictures)

    pictures_json = picture_schema.dump(recipe.pictures)

    return response_with(resp.SUCCESS_200, pictures_json)


@recipe_routes.route("/<recipe_id>/pictures/", methods=["POST"])
@cross_origin()
@token_required
def upload_recipe_picture(user, recipe_id):
    picture_schema = PictureSchema(many=True)

    try:
        file = request.files['picture']

        recipe = DishRecipe.query.filter_by(id=recipe_id).first()

        if not recipe:
            return response_with(resp.SERVER_ERROR_404)

        logger.debug(recipe)

        if file and not is_allowed_file(file.content_type):
            logger.info(f"document with invalid extension: {file.filename}")
            return response_with(resp.INVALID_INPUT_422, message="document has invalid extension")

        filename = generate_filename(secure_filename(file.filename))

        logger.debug(f"filename: {filename}")

        file.save(os.path.join(Config.MEDIAFILES_FOLDER, filename))

        picture = Picture()
        picture.path = url_for(
            "document_routes.get_document", filename=filename)
        picture.save()

        recipe.pictures.append(picture)
        recipe.save()

        pictures_json = picture_schema.dump(recipe.pictures)

        logger.debug(pictures_json)

        return response_with(resp.SUCCESS_201, value=pictures_json)

    except Exception as ex:
        logger.warning(ex)
        return response_with(resp.BAD_REQUEST_400)


@recipe_routes.route("/<product_id>/pictures/<picture_id>/", methods=["DELETE"])
@cross_origin()
def delete_recipe_picture(product_id, picture_id):
    picture = db.session.query(Picture).filter(Picture.id == picture_id).\
    join(Picture.dish).filter(DishRecipe.id == product_id).first()

    if not picture:
        return response_with(resp.SERVER_ERROR_404)
    
    picture_path = picture.path
    picture.delete()

    logger.debug("picture record in db deleted")
    
    try:
        
        logger.info(f"deleting picture: {picture}")
        
        logger.debug(f"{Config.BASE_DIR + picture_path} exists: {bool(os.path.isfile(Config.BASE_DIR + picture_path))}")

        os.remove(Config.BASE_DIR + picture_path)

        logger.info("picture deleted")

        return response_with(resp.SUCCESS_204)
    except Exception as ex:
        logger.error(ex)        
        return response_with(resp.SERVER_ERROR_500)
