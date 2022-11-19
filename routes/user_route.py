from flask import Blueprint, request
from utils.response import response_with
import utils.response as resp
from models.user_model import User, UserSchema
from utils.token import Token


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/register/", methods=["POST"])
def register_user():
    data = request.get_json()
    user_schema = UserSchema()

    try:
        cleared_data = user_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)

    cleared_data['password'] = User.generate_hash(data['password'])

    try:
        user = User(**cleared_data)
        user.save()

        return response_with(resp.SUCCESS_201, message="User was created successfully.")

    except Exception as ex:
        print(ex)
        return response_with(resp.CONFLICT_409)


@user_routes.route("/login/", methods=["POST"])
def login_user():
    data = request.get_json()
    user_schema = UserSchema()

    try:
        cleared_data = user_schema.load(data)
    except:
        return response_with(resp.INVALID_INPUT_422)

    user =  User.query.filter_by(name=cleared_data['name']).first()

    if not user:
        return response_with(resp.SERVER_ERROR_404, message="user does not exist")

    if not User.verify_hash(user.password, cleared_data['password']):
        return response_with(resp.INVALID_INPUT_422, message="password is wrong")

    token = Token.encode(id=user.id)

    return response_with(resp.SUCCESS_200, value={"token": token})


@user_routes.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    return response_with(resp.SUCCESS_200)