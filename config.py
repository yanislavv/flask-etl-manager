from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes


class DevelopmentConfig:
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (config('SQLALCHEMY_DATABASE_URI'))


class TestConfig:
    FLASK_ENV = "test"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (config('TEST_SQLALCHEMY_DATABASE_URI'))


def create_app(config="config.DevelopmentConfig"):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config)
    migrate = Migrate(app, db)
    CORS(app)
    api = Api(app)
    [api.add_resource(*route_data) for route_data in routes]
    return app