from api.app import db
from api.blueprints.models import Image, Post, User
from flask import Blueprint, jsonify, request

post_blueprint = Blueprint("crud", __name__, url_prefix="/v1/posts")


@post_blueprint.route("/<user_id>", methods=["GET"])
def get_posts(user_id):
    try:
        from sqlalchemy.exc import SQLAlchemyError

        posts = Post.query.all(User.id=user_id)

        return jsonify({"posts": [post.to_dict() for post in posts]}), 200
    except SQLAlchemyError:
        return jsonify({"message": "Fail get posts"}), 400
