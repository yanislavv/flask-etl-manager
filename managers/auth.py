import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from datetime import datetime, timedelta
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest, Unauthorized

from models import UserModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.email, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify(token):
    user_id = AuthManager.decode_token(token)
    return UserModel.query.filter_by(email=user_id).first()
