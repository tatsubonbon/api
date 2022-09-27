import logging

from api.app import db, ma, oauth
from api.blueprints.posts import blueprint
from api.common.decorator import logging_api
from api.common.error import forbidden
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.schemas import ImageSchema
from api.db.models.tables import Image, Post
from flask import g, request
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class RequestSchema(ma.Schema):
    post_id = ma.String(required=True)
    title = ma.String(required=True)
    text = ma.String(required=True)
    images = ma.Dict(keys=ma.String(), values=ma.String())


@blueprint.route("/", methods=["PUT"])
@oauth.login_required
@logging_api(logger)
def update_post():
    try:
        request_schema = RequestSchema()
        payload = request_schema.load(request.json)
    except Exception as e:
        logger.info(e)
        return make_error_response(
            get_message("CM0000I", name="test"), StatusCode.ERROR
        )

    try:
        post_id = payload.get("post_id")
        title = payload.get("title")
        text = payload.get("text")
        images_dict = payload.get("images")

        post = Post.query.filter_by(id=post_id).first()
        images = Image.query.filter_by(post_id=post_id).all()
        if g.user != post.author:
            return forbidden(get_message("CM0004E"))

        post.title = title
        post.text = text

        for image in images:
            image = ImageSchema().dump(image)
            if image["id"] in images_dict.keys():
                with open(image["image_path"], mode="w") as f:
                    f.write(images_dict.get(image["id"]))

        db.session.add(post)
        db.session.commit()

        return make_response(
            get_message("CM0001I", name="投稿の更新"),
            StatusCode.SUCCCESS,
            {"post_id": post_id},
        )
    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の更新"), StatusCode.ERROR
        )
    except Exception as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="投稿の更新"), StatusCode.ERROR
        )
