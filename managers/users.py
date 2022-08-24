from werkzeug.exceptions import BadRequest

from db import db
from managers.auth import AuthManager
from models.users import UserModel
from werkzeug.security import generate_password_hash, check_password_hash


class ComplainerManager:
    @staticmethod
    def register(complainer_data):
        complainer_data["password"] = generate_password_hash(complainer_data["password"])
        user = UserModel(**complainer_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        complainer = UserModel.query.filter_by(email=login_data["email"]).first()
        if not complainer:
            raise BadRequest("No such email! Please register!")
        if check_password_hash(complainer.password, login_data["password"]):
            return AuthManager.encode_token(complainer)
        raise BadRequest("Wrong credentials!")
