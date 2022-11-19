import datetime
from types import ClassMethodDescriptorType

import jwt
from itsdangerous import URLSafeTimedSerializer

from config.app_config import DevelopmentConfig



class Token:
    __const = DevelopmentConfig
    @classmethod
    def encode(cls, id):
        token_data = {
            "id": id, 
            "exp": datetime.datetime.now() + cls.__const.TOKEN_LIFE_TIME 
            }
        token = jwt.encode(token_data, cls.__const.SECRET_KEY, cls.__const.ALGORITHM)
        return token

    @classmethod
    def decode(cls, token):
        try:
            token_data = jwt.decode(token, cls.__const.SECRET_KEY, algorithms=[cls.__const.ALGORITHM,])
            return token_data
        except Exception as ex:
            raise ex
