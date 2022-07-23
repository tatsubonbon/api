import time

from api.app import db, oauth
from api.blueprints.models import User
from flask import Blueprint, g, jsonify, session

oauth_path = "/v1/oauth"

oauth_blueprint = Blueprint("oauth", __name__, url_prefix=oauth_path)


@oauth_blueprint.route("/token", methods=["GET"])
@oauth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({"token": token, "duration": 600})
