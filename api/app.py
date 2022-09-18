import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.config import config

db = SQLAlchemy()
oauth = HTTPBasicAuth()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.config[os.getenv("FLASK_TYPE")])

    setup_app(app)

    return app


def setup_app(app):
    from api import blueprints_list

    for module in blueprints_list:
        app.register_blueprint(module.blueprint)

    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
