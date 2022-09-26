import logging
import os

from api.app import db, oauth
from api.blueprints.posts import blueprint
from api.common.decorator import logging_api
from api.common.error import forbidden
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.schemas import ImageSchema
from api.db.models.tables import Image, Post
from flask import g
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


@blueprint.route("/<post_id>", methods=["DELETE"])
@oauth.login_required
@logging_api(logger)
def delete_post(post_id):
    try:
        post = Post.query.filter_by(id=post_id).first()
        images = Image.query.filter_by(post_id=post_id).all()

        if g.user != post.author:
            return forbidden(get_message("CM0004E"))

        db.session.delete(post)

        for image in images:
            db.session.delete(image)
            image = ImageSchema().dump(image)
            image_path = image["image_path"]
            if os.path.exists(image_path):
                os.remove(image_path)

        db.session.commit()

        return make_response(
            get_message("CM0001I", name="投稿の削除"),
            StatusCode.SUCCCESS,
            {"post_id": post_id},
        )

    except IOError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の削除"), StatusCode.ERROR
        )
    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の削除"), StatusCode.ERROR
        )
