from flask import Blueprint, request
from utils.response import response_with
import utils.response as resp

from models.product_model import Product, ProductSchema


product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/", methods=["GET"])
def get_all_products():
    product_schema = ProductSchema(many=True)
    products = Product.query.all()
    products_json = product_schema.dump(products)
    
    return response_with(resp.SUCCESS_200, value=products_json)


@product_routes.route("/<product_id>/", methods=["GET"])
def get_product(product_id):
    product_schema = ProductSchema()
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return response_with(resp.SERVER_ERROR_404)
    
    product_json = product_schema.dump(product)
    print(product_json)

    return response_with(resp.SUCCESS_200, value=product_json)


@product_routes.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema(only=('name', 'description', 'pictures'))
    
    try:
        cleaned_data = product_schema.load(data)
        print(cleaned_data)
        
        product = Product(**cleaned_data)
        product.save()
        
        return response_with(resp.SUCCESS_201, value=product_schema.dump(product))
    except Exception as ex:
        return response_with(resp.INVALID_INPUT_422)


@product_routes.route("/<product_id>/", methods=["PATCH"])
def patch_product(product_id):
    return response_with(resp.SUCCESS_200)


@product_routes.route("/<prouct_id>/", methods=["DELETE"])
def delete_product(product_id):
    return response_with(resp.SUCCESS_204)
