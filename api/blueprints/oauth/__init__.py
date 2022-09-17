from flask import Blueprint

oauth_blueprint = Blueprint("oauth", __name__, url_prefix="/v1/oauth")
