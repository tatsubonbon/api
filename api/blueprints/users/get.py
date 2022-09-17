from api.app import oauth
from api.blueprints.users import user_blueprint
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import User
from sqlalchemy.exc import SQLAlchemyError


@user_blueprint.route("/", methods=["GET"])
@oauth.login_required
def get_users():
    try:

        users = User.query.all()

        return make_response(
            get_message("CM0001I", name="ユーザーの取得"),
            StatusCode.POST_SUCCESS,
            {"users": [user.to_dict() for user in users]},
        )

    except SQLAlchemyError:
        return make_error_response(
            get_message("CM0002E", name="ユーザーの取得"), StatusCode.ERROR
        )


@user_blueprint.route("/<user_id>", methods=["GET"])
@oauth.login_required
def get_user(user_id):
    try:

        user = User.query.filter_by(id=user_id).first()

        if user:
            return make_response(
                get_message("CM0001I", name="ユーザーの取得"),
                StatusCode.POST_SUCCESS,
                {"user": user.to_dict()},
            )
        return make_error_response(
            get_message("CM0006E", name="ユーザー"), StatusCode.NOT_FOUND_ERROR
        )
    except SQLAlchemyError:
        return make_error_response(
            get_message("CM0002E", name="ユーザーの取得"), StatusCode.ERROR
        )
