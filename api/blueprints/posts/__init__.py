from flask import Blueprint

post_blueprint = Blueprint("posts", __name__, url_prefix="/v1/posts")
