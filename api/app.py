import logging
import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.config import config

db = SQLAlchemy()
oauth = HTTPBasicAuth()


def create_app(config_name):
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG)

    app.config.from_object(config.config[config_name])

    setup_app(app)

    return app


def setup_app(app):
    from api.blueprints.oauth import views as oauth_view
    from api.blueprints.users import views as user_view

    app.register_blueprint(user_view.user_blueprint)
    app.register_blueprint(oauth_view.oauth_blueprint)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    Migrate(app, db)


def create_tables(app, configname):
    if not os.path.exists(config.config[configname].SQLALCHEMY_DATABASE_URI):
        db.create_all(app)
