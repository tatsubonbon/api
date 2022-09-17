from api.app import db, ma, oauth
from api.blueprints.users import user_blueprint
from api.common.error import forbidden
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import User
from flask import g, request
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class RequestSchema(ma.Schema):
    id = ma.Int(required=True)
    user_name = ma.String(required=True)
    email = ma.Email(required=True)


@user_blueprint.route("/", methods=["PUT"])
@oauth.login_required
def update_user():
    try:
        requestSchema = RequestSchema()
        payload = requestSchema.load(request.json)
    except Exception:
        return make_error_response(
            get_message("CM0000I", name="test"), StatusCode.ERROR
        )

    try:
        id = payload.get("id")
        user_name = payload.get("user_name")
        email = payload.get("email")

        user = User.query.filter_by(id=id).first()

        if g.user != user:
            forbidden("Insufficient permissions")

        user.user_name = user_name
        user.email = email

        db.session.add(user)
        db.session.commit()

        return make_response(
            get_message("CM0001I", name="ユーザー更新"),
            StatusCode.SUCCCESS,
            {"user_name": user.user_name},
        )
    except IntegrityError:
        # メールアドレス重複登録
        return make_error_response(
            get_message("CM0003I", name=email), StatusCode.DUPLICATION_ERROR
        )
    except SQLAlchemyError:
        return make_error_response(
            get_message("CM0002E", name="ユーザー更新"), StatusCode.ERROR
        )
