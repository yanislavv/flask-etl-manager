import factory

from db import db
from models import UserModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object


class UserFactoryAdmin(BaseFactory):
    class Meta:
        model = UserModel
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = 'admin'


class UserFactoryDeveloper(BaseFactory):
    class Meta:
        model = UserModel
    email = factory.Faker("email")
    password = factory.Faker("password")
    role = 'develope'