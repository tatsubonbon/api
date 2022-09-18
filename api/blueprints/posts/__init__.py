from flask import Blueprint

blueprint = Blueprint("posts", __name__, url_prefix="/v1/posts")
