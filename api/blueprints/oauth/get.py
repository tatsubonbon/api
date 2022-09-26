import logging

from api.app import oauth
from api.blueprints.oauth import blueprint
from api.common.decorator import logging_api
from api.common.error import unauthorized
from api.common.message import get_message
from flask import g, jsonify

logger = logging.getLogger(__name__)


@blueprint.route("/token", methods=["GET"])
@oauth.login_required
@logging_api(logger)
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({"token": token.decode("utf-8"), "duration": 600})


@oauth.error_handler
def auth_error():
    return unauthorized(get_message("CM0005E"))
