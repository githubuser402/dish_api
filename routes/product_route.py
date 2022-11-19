from flask import Blueprint
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
def get_prouct(product_id):
    return response_with(resp.SUCCESS_200)


@product_routes.route("/", methods=["POST"])
def create_product():
    return response_with(resp.SUCCESS_201)


@product_routes.route("/<product_id>/", methods=["PATCH"])
def patch_product(product_id):
    return response_with(resp.SUCCESS_200)


@product_routes.route("/<prouct_id>/", methods=["DELETE"])
def delete_product(product_id):
    return response_with(resp.SUCCESS_204)
