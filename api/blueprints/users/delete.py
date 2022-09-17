from api.app import db, oauth
from api.blueprints.users import user_blueprint
from api.common.message import get_message
from api.common.setting import StatusCode
from api.db.models.users import User
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError


@user_blueprint.route("/<user_id>", methods=["DELETE"])
@oauth.login_required
def delete_user(user_id):
    try:

        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

        return (
            jsonify({"message": get_message("CM0001I", name="ユーザーの削除")}),
            StatusCode.SUCCCESS,
        )
    except SQLAlchemyError:
        return (
            jsonify({"message": get_message("CM0002E", name="ユーザーの削除")}),
            StatusCode.ERROR,
        )
