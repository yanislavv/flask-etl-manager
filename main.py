from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
db.init_app(app)
app.config.from_object("config.DevelopmentConfig")
migrate = Migrate(app, db)
api = Api(app)
#CORS(app)


[api.add_resource(*route_data) for route_data in routes]


@app.after_request
def return_resp(resp):
    db.session.commit()
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
