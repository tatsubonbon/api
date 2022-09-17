from api.app import oauth
from api.blueprints.oauth import oauth_blueprint
from flask import g, jsonify


@oauth_blueprint.route("/token", methods=["GET"])
@oauth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({"token": token, "duration": 600})
