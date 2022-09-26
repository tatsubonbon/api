import logging
import os
import uuid
from pathlib import Path

from api.app import db, ma, oauth
from api.blueprints.posts import blueprint
from api.common.decorator import logging_api
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import Image, Post
from flask import current_app, request
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class RequestSchema(ma.Schema):
    user_id = ma.Int(required=True)
    title = ma.String(required=True)
    text = ma.String(required=True)
    images = ma.List(ma.String())


@blueprint.route("/", methods=["POST"])
@oauth.login_required
@logging_api(logger)
def create_post():
    try:
        request_schema = RequestSchema()
        payload = request_schema.load(request.json)
    except Exception as e:
        logger.info(e)
        return make_error_response(
            get_message("CM0000I", name="test"), StatusCode.ERROR
        )

    try:
        post_id = uuid.uuid4()
        user_id = payload.get("user_id")
        title = payload.get("title")
        text = payload.get("text")
        images = payload.get("images")

        post = Post(id=str(post_id), user_id=int(user_id), title=title, text=text)
        db.session.add(post)
        db.session.commit()

        image_path = Path(current_app.config["UPLOAD_DIR"] + str(user_id))
        if not os.path.isdir(image_path):
            os.mkdir(image_path)

        if images:
            for image in images:
                id = str(uuid.uuid4())
                file_path = os.path.join(image_path, id)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(image)
                image = Image(id=id, post_id=str(post_id), image_path=file_path)
                db.session.add(image)
        db.session.commit()

        return make_response(
            get_message("CM0001I", name="投稿"),
            StatusCode.POST_SUCCESS,
            {"post_id": post_id},
        )

    except IOError as e:
        logger.error(e)
        return make_error_response(get_message("CM0002E", name="投稿"), StatusCode.ERROR)
    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(get_message("CM0002E", name="投稿"), StatusCode.ERROR)
    except Exception as e:
        logger.error(e)
        return make_error_response(get_message("CM0002E", name="投稿"), StatusCode.ERROR)
