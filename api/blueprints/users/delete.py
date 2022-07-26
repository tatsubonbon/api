import logging

from api.app import db, oauth
from api.blueprints.users import blueprint
from api.common.decorator import logging_api
from api.common.error import forbidden
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import User
from flask import g
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


@blueprint.route("/<user_id>", methods=["DELETE"])
@oauth.login_required
@logging_api(logger)
def delete_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        if g.user != user:
            return forbidden(get_message("CM0004E"))

        db.session.delete(user)
        db.session.commit()

        return make_response(
            get_message("CM0001I", name="ユーザーの削除"),
            StatusCode.SUCCCESS,
            {"user_id": user_id},
        )

    except SQLAlchemyError as e:
        logger.error(e)
        return make_error_response(
            get_message("CM0002E", name="ユーザーの削除"), StatusCode.ERROR
        )
