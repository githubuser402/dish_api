from flask import request
from utils.response import response_with
import utils.response as resp
from functools import wraps
from models.user_model import User
from utils.token import Token


def token_required(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.get("x-access-token"):
            return response_with(resp.UNAUTHORIZED_403)

        token = request.headers.get("x-access-token")

        try:
            # token_data = jwt.decode(token, key=Constants.secret_key, algorithms=[Constants.algorithm,])
            token_data = Token.decode(token)
        except Exception as ex:
            return response_with(resp.UNAUTHORIZED_401)

        user = User.query.filter_by(id=token_data['id']).first()

        if not user:
            return response_with(resp.CONFLICT_409, message="user was deleted")

        return func(user, *args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper