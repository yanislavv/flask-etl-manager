import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from datetime import datetime, timedelta
#from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest, Unauthorized

from models import UserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.email, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key='testsecretkey1234', algorithm="HS256")