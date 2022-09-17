from api.app import oauth
from api.blueprints.users import user_blueprint
from api.common.message import get_message
from api.common.response import make_error_response
from api.common.setting import StatusCode
from api.db.models.users import User
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError


@user_blueprint.route("/", methods=["GET"])
@oauth.login_required
def get_users():
    try:

        users = User.query.all()

        return (
            jsonify({"users": [user.to_dict() for user in users]}),
            StatusCode.SUCCCESS,
        )
    except SQLAlchemyError:
        return (
            jsonify({"message": get_message("CM0002E", name="ユーザーの取得")}),
            StatusCode.ERROR,
        )


@user_blueprint.route("/<user_id>", methods=["GET"])
@oauth.login_required
def get_user(user_id):
    try:

        user = User.query.filter_by(id=user_id).first()

        if user:
            return jsonify({"user": user.to_dict()}), StatusCode.SUCCCESS
        return make_error_response(
            get_message("CM0006E", name="user"), StatusCode.NOT_FOUND_ERROR
        )
    except SQLAlchemyError:
        return (
            jsonify({"message": get_message("CM0002E", name="ユーザーの取得")}),
            StatusCode.ERROR,
        )
