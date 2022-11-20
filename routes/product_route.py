from flask import Blueprint, request, send_from_directory
from utils.response import response_with
import utils.response as resp

from utils.logger import logger

from models.product_model import Product, ProductSchema
from models.picture_model import Picture, PictureSchema


product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/", methods=["GET"])
def get_all_products():
    product_schema = ProductSchema(many=True)
    products = Product.query.all()
    products_json = product_schema.dump(products)
    
    logger.info("listed all products")
        
    return response_with(resp.SUCCESS_200, value=products_json)


@product_routes.route("/<product_id>/", methods=["GET"])
def get_product(product_id):
    product_schema = ProductSchema()
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return response_with(resp.SERVER_ERROR_404)
    
    product_json = product_schema.dump(product)

    logger.info(f"queried product: {product_id}")
    return response_with(resp.SUCCESS_200, value=product_json)


@product_routes.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema(only=('name', 'description',))
    
    try:
        cleaned_data = product_schema.load(data)
        print(cleaned_data)
        
        product = Product(**cleaned_data)
        
        product.save()
        logger.info(f"saved product: {product.name}")
        
        return response_with(resp.SUCCESS_201, value=product_schema.dump(product))
    except Exception as ex:
        logger.warning(f"wrong data: {ex}")
        return response_with(resp.INVALID_INPUT_422)


@product_routes.route("/<product_id>/", methods=["PATCH"])
def path_product(product_id):
    return response_with(resp.SUCCESS_200)


@product_routes.route("/<product_id>/", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    
    if product:
        logger.info(f"deleted product: {product}")
        product.delete()
   
    return response_with(resp.SUCCESS_204)


@product_routes.route("/<product_id>/pictures/", methods=["GET"])
def get_product_pictures_list(product_id):
    pass


@product_routes.route("/<product_id>/pictures/", methods=["POST"])
def upload_product_picture(product_id):
    pass


@product_routes.route("/<product_id>/pictures/<picture_id>/", methods=["DELETE"])
def delete_product_picture(product_id, picture_id):
    pass
