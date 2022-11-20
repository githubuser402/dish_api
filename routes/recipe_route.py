from flask import Blueprint, request, url_for
from utils.response import response_with
import utils.response as resp
from utils.logger import logger
from utils.document_filter import is_allowed_file, generate_filename
from utils.database import db
from werkzeug.utils import secure_filename
import os

from config.config import Config

from models.dish_recipe_model import DishRecipe, DishRecipeSchema
from models.picture_model import Picture, PictureSchema

recipe_routes = Blueprint("recipe_routes", __name__)


@recipe_routes.route("/", methods=["GET"])
def get_all_recipes():
    recipe_schema = DishRecipeSchema(many=True)
    recipes = DishRecipe.query.all()
    recipe_json = recipe_schema.dump(recipes)

    return response_with(resp.SUCCESS_200, value=recipe_json)


@recipe_routes.route("/<recipe_id>/", methods=["GET"])
def get_recipe(recipe_id):
    recipe_schema = DishRecipeSchema()
    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if not recipe:
        return response_with(resp.SERVER_ERROR_404)

    recipe_json = recipe_schema.dump(recipe)

    return response_with(resp.SUCCESS_200, value=recipe_json)


@recipe_routes.route("/", methods=["POST"])
def create_recipe():
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
def patch_recipe(recipe_id):
    return response_with(resp.SUCCESS_200)


@recipe_routes.route("/<recipe_id>/", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if recipe:
        logger.info(f"deleted recipe {recipe}")
        recipe.delete()
    return response_with(resp.SUCCESS_204)


@recipe_routes.route("/<recipe_id>/pictures/", methods=["GET"])
def get_recipe_pictures(recipe_id):
    picture_schema = PictureSchema(many=True)

    recipe = DishRecipe.query.filter_by(id=recipe_id).first()

    if not recipe:
        return response_with(resp.SERVER_ERROR_404)

    logger.debug(recipe.pictures)

    pictures_json = picture_schema.dump(recipe.pictures)

    return response_with(resp.SUCCESS_200, pictures_json)


@recipe_routes.route("/<recipe_id>/pictures/", methods=["POST"])
def upload_recipe_picture(recipe_id):
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
def delete_recipe_picture(product_id, picture_id):
    # recipe = DishRecipe.query.filter_by(id=product_id).first()

    # if not recipe:
    #     return response_with(resp.SERVER_ERROR_404)

    # try: 
    #     picture_to_delete = list(filter(lambda picture: picture.id == picture_id, recipe.pictures))[0]
    # except Exception as ex:
    #     logger.warning(f"picture not found")
    #     return response_with(resp.SERVER_ERROR_404)

    # logger.debug("delete: ", type(picture_to_delete))
    
    # if not picture_to_delete:
    #     return response_with(resp.SERVER_ERROR_404)

    # logger.debug(f"deleting picture: {picture_to_delete}")

    # filename = os.path.basename(picture_to_delete.path)

    # try:
    #     os.remove(
    #         os.path.join(Config.MEDIAFILES_FOLDER, filename)
    #     )
    #     picture_to_delete.delete()
        
    #     recipe.save()
        
    #     logger.info(f"deleted picture: {filename}")

    #     return response_with(resp.SUCCESS_204)
    # except Exception as ex:
    #     logger.error(ex)
    #     return response_with(resp.SERVER_ERROR_500)
    pass