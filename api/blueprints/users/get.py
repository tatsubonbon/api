import logging

from api.app import oauth
from api.blueprints.users import blueprint
from api.common.decorator import logging_api
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import User
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


@blueprint.route("/", methods=["GET"])
@oauth.login_required
@logging_api(logger)
def get_users():
    try:
        users = User.query.all()

        return make_response(
            get_message("CM0001I", name="ユーザーの取得"),
            StatusCode.SUCCCESS,
            {"users": [user.to_dict() for user in users]},
        )

    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="ユーザーの取得"), StatusCode.ERROR
        )


@blueprint.route("/<user_id>", methods=["GET"])
@oauth.login_required
@logging_api(logger)
def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        if user:
            return make_response(
                get_message("CM0001I", name="ユーザーの取得"),
                StatusCode.SUCCCESS,
                {"user": user.to_dict()},
            )
        return make_error_response(
            get_message("CM0006E", name="ユーザー"), StatusCode.NOT_FOUND_ERROR
        )
    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="ユーザーの取得"), StatusCode.ERROR
        )
