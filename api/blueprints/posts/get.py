from pathlib import Path

from api.app import oauth
from api.blueprints.posts import post_blueprint
from api.common.message import get_message
from api.common.response import make_response
from api.common.setting import StatusCode
from api.db.columns.postsCol import PostColumns
from api.db.models.image import Image, ImageSchema
from api.db.models.posts import Post, PostSchema
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError


@post_blueprint.route("/<post_id>", methods=["GET"])
@oauth.login_required
def get_post(post_id):
    try:

        post = Post.query.filter_by(id=post_id).first()
        post = PostSchema().dump(post)

        images = Image.query.filter_by(post_id=post[PostColumns.ID]).first()
        images = ImageSchema().dump(images)

        image_path = Path(images["image_path"])

        with open(image_path, mode="r") as f:
            data = f.read()
        return make_response(
            get_message("CM0006E", name="ユーザー"), StatusCode.SUCCCESS, data
        )
    except IOError:
        return (
            jsonify({"message": get_message("CM0002E", name="投稿の取得")}),
            StatusCode.ERROR,
        )
    except SQLAlchemyError:
        return (
            jsonify({"message": get_message("CM0002E", name="投稿の取得")}),
            StatusCode.ERROR,
        )
    except Exception:
        return (
            jsonify({"message": get_message("CM0002E", name="投稿の取得")}),
            StatusCode.ERROR,
        )