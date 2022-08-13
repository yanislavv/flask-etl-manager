from models.enums import UserRole
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
