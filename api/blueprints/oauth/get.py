from api.app import oauth
from api.blueprints.oauth import oauth_blueprint
from api.common.error import unauthorized
from api.common.message import get_message
from flask import g, jsonify


@oauth_blueprint.route("/token", methods=["GET"])
@oauth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({"token": token, "duration": 600})


@oauth.error_handler
def auth_error():
    return unauthorized(get_message("CM0005E"))
