import logging
import os

from api.app import oauth
from api.blueprints.posts import blueprint
from api.common.decorator import logging_api
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.columns.postsCol import PostColumns
from api.db.models.schemas import ImageSchema, PostSchema
from api.db.models.tables import Image, Post
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


@blueprint.route("/<post_id>", methods=["GET"])
@oauth.login_required
@logging_api(logger)
def get_post(post_id):
    try:

        post = Post.query.filter_by(id=post_id).first()
        post = PostSchema().dump(post)

        images = Image.query.filter_by(post_id=post[PostColumns.ID]).all()

        image_list = []
        for image in images:
            image = ImageSchema().dump(image)
            if os.path.exists(image["image_path"]):
                with open(image["image_path"], mode="r") as f:
                    data = f.read()
                    image_list.append({image["id"]: data})
        return make_response(
            get_message("CM0001I", name="投稿の取得"),
            StatusCode.SUCCCESS,
            {"title": post["title"], "text": post["text"], "images": image_list},
        )
    except IOError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
    except Exception as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の取得"), StatusCode.ERROR
        )
