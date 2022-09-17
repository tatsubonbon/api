from api.app import db, ma
from api.blueprints.users import user_blueprint
from api.common.message import get_message
from api.common.response import make_error_response, make_response
from api.common.setting import StatusCode
from api.db.models.tables import User
from flask import request
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class RequestSchema(ma.Schema):
    user_name = ma.String(required=True)
    email = ma.Email(required=True)
    password = ma.String(required=True)


@user_blueprint.route("/", methods=["POST"])
def create_user():
    try:
        requestSchema = RequestSchema()
        payload = requestSchema.load(request.json)
    except Exception:
        return make_error_response(
            get_message("CM0000I", name="test"), StatusCode.ERROR
        )

    try:
        user_name = payload.get("user_name")
        email = payload.get("email")
        password = payload.get("password")
        print(user_name)

        user = User(user_name=user_name, email=email, role_id=1)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        return make_response(
            get_message("CM0001I", name="ユーザー登録"),
            StatusCode.POST_SUCCESS,
            {"user_name": user_name},
        )
    except IntegrityError:
        # メールアドレス重複登録
        return make_error_response(
            get_message("CM0003I", name=email), StatusCode.DUPLICATION_ERROR
        )
    except SQLAlchemyError:
        return make_error_response(
            get_message("CM0002E", name="ユーザー登録"), StatusCode.ERROR
        )
