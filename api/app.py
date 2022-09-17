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
    from api.blueprints.oauth import get as get_oauth
    from api.blueprints.posts import get as get_posts
    from api.blueprints.posts import post as post_posts
    from api.blueprints.users import delete as delete_user
    from api.blueprints.users import get as get_user
    from api.blueprints.users import post as post_user

    app.register_blueprint(get_user.user_blueprint)
    app.register_blueprint(get_oauth.oauth_blueprint)
    app.register_blueprint(post_posts.post_blueprint)
    app.register_blueprint(get_posts.post_blueprint)
    app.register_blueprint(post_user.user_blueprint)
    app.register_blueprint(delete_user.user_blueprint)

    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
