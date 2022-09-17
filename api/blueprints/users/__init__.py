from flask import Blueprint

user_blueprint = Blueprint("users", __name__, url_prefix="/v1/users")
